from catalog import app

if __name__ == "__main__":
    app.secret_key = 'super_secret_key'
    app.run(
        host="http://34.204.53.135/"
    )
