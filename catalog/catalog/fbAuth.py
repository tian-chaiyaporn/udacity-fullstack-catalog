from flask import request, redirect, flash, make_response
from catalog import app, login_session
from helpersFunctions import createUser, getUserID
import httplib2
import json


# This method is called when user login
@app.route('/fbconnect', methods=['POST'])
def fbconnect():
    # make sure that the state is the same as the login state token issued
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    access_token = request.data

    # take app_id and app_secret from fb_secret.json file and construct url
    app_id = json.loads(open('fb_secret.json', 'r').read())[
        'web']['app_id']
    app_secret = json.loads(
        open('fb_secret.json', 'r').read())['web']['app_secret']
    url = 'https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id=%s&client_secret=%s&fb_exchange_token=%s' % (
        app_id, app_secret, access_token)
    # make http request with the url to authenticate the user
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]

    # Use token to get user info from API
    userinfo_url = "https://graph.facebook.com/v2.4/me"
    # strip expire tag from access token
    token = result.split("&")[0]
    url = 'https://graph.facebook.com/v2.4/me?%s&fields=name,id,email' % token
    h = httplib2.Http()
    # make http request and store the returned data into login session
    result = h.request(url, 'GET')[1]
    data = json.loads(result)
    login_session['username'] = data["name"]
    login_session['email'] = data["email"]
    login_session['facebook_id'] = data["id"]
    # store token for to be used when disconnecting from facebook (logout)
    stored_token = token.split("=")[1]
    login_session['access_token'] = stored_token

    # see if user exists
    user_id = getUserID(login_session['email'])
    # create new user if user doesn't already exist
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    flash("Now logged in as %s" % login_session['username'])
    return output


# This function is called when user logout
@app.route('/fbdisconnect')
def fbdisconnect():
    facebook_id = login_session['facebook_id']
    access_token = login_session['access_token']
    url = 'https://graph.facebook.com/%s/permissions?access_token=%s' % (
        facebook_id, access_token)
    h = httplib2.Http()
    # make http request to delete token
    h.request(url, 'DELETE')[1]
    # delete all stored data of user from browser
    del login_session['facebook_id']
    del login_session['username']
    del login_session['email']
    del login_session['user_id']
    return redirect('/')
