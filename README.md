
# README
# Catalog Project
### Full Stack Developer Nanodegree @ Udacity
----


## Description
----

This is an item catalog storage app. User can add, edit, delete items according to a fixed category. It as a fulfillment for the project's rubik in the Full Stack Developer Nanodegree by Udacity in March 2017. The project is run on Vagrant in VM Box, using sqlite database and sqlalchemy library. The project is structured according to Flask recommendation: http://flask.pocoo.org/docs/0.12/patterns/packages/ which should make the code more maintainable.


## Configuration Instruction
----
For configuration, please locate the requirement.txt file in /catalog_project. To install it, launch the Vagrant VM and use the following command to install all the dependencies:

```shell
	pip install -r requirements.txt
```


## Installation for Vagrant
----
A Vagrant file is provided with relevant libraries/imports installed

If you don't have Vagrant installed, first download and install Vagrant and VM Box at:
- https://www.vagrantup.com/
- https://www.virtualbox.org/

Then navigate to this folder and into the directory called "vagrant" and launch Vagrant VM using the following commands on terminal:
```shell
	vagrant up
	vagrant ssh
```


## Instruction for Running Project Locally
----
When inside vagrant, first navigate to vagrant directory using the command line: `cd /vagrant` in terminal, then navigate to the tournament directory using the command line: `cd /catalog`.

To initialize the database, use the following command to set up the database:
```shell
	python db_setup.py
```

To populate initial data for testing, type:
```shell
	python populateData.py
```

To run the app, type:
```shell
	python run.py
```

The app should now be hosted on http//localhost:8800


## Author
----
Code base provided by Udacity Full Stack Nanodegree Team.
Added by Chaiyaporn Chinotaikul as student of the Nanodegree Program
contact: tian_chaiya12@hotmail.com


## License
----
No license. This project is for the purpose of self-education under Udacity's guidance.
