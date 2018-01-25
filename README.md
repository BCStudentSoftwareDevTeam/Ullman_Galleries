# Ullman Galleries Ullman Galleries is a management tool for application entries. It provides an easy way to accept applications. Our main purpose for the system is to accept applications from artists that want to show their work in a Berea College Gallery Showing.
  

## Getting Started
The intial step of setting up a development environment is choosing the appropriate tool to complete the application setup.
This application requires you to have a linux environment specifically an Ubuntu.
However, if you are working out of a windows operating system during development we would recommend you use [cloud9](https://c9.io/)

### Cloud9 Setup Guide (Optional)
You can find the instruction to setting up c9 at https://docs.c9.io/docs/create-a-workspace. You should use python as the template.

### Setting up the Application

After you have accessed your environment, we have built some scripts into the system that will get the application up and running for you. 

1. ```python3 setup.py install```
2. ```. venv/bin/activate```
3. ``` mysql-ctl install ```
4. ``` python scripts/ConfigureApp.py ``` 
4. ``` Use:
          host - localhost
          username - Given by mysql-ctl
          password - empty
          database name  - Given by mysql-ctl
   ```
5. ```Follow the prompts:
      1. Enter anything for the secret key
      2. make sure to create the database```
6. ``` It seems everyone is getting an error, on the first run. Please re-run the program to have it setup properly```
7. ```python app.py```

>***Note***: To start and stop mysql  in cloud9 use ```mysql-ctl [start|stop|restart]``` 

>***Note***: If you working inside of your own linux environment you may need to change the port and host information inside of ```app.py`` the default is setup up for working inside of cloud9

>***Note***: You may also need to setup mysql on your own if you are not using cloud9

### Starting the application after inital setup
1. ```source venv/bin/activate```
2. ```mysql-ctl start ```
3. ```python app.py```

## Adding dummy data
1. ```
      Add dummy data to the scripts/dummy_data.py file
      Please note that due to the forigen keys, the order does matter!
      Please order them as: Users, Files,Galleries,Forms,Images
   ```
2. ```python scripts/dummy_data.py```

## Source Structure and Guidelines
### Structure
The follow is an outline of the structure of the program along with a brief 
description of each folder.


```
app/
├── __init__.py 
├── allImports.py
├── config                      <--- Houses all *.yaml files, which are used for configuration
│   ├── __init__.py
│   ├── config.yaml             <--- Default Config File
│   ├── loadConfig.py           
│   └── secret.yaml             <--- Stores any sensitive infomation, including database passwords, and session secret key
│
├── controllers                 <--- Stores all the controllers (controllers and views should have matching names)
│   ├── __init__.py
│   ├── hello.py                <--- A single controller, in this case it is a single page (hello)
│
├── logic                       <--- Stores files that are used throughout the application for validation, and authentication. ALL FILES HERE MUST BE DOcumented  
│   ├── __init__.py
│   ├── absolute_path.py        <--- Solution to relative path issue
├── models                      <--- Stores the database models
│   └── util.py                 <--- Database related models
├── static                      <--- Static content (css/js) is stored here, the filename should match the controller/view/url that is being styled
│   ├── css                     <--- Stores css
│   │   ├── ext                 <--- External css libraries
│   │   ├── fonts               <--- Fonts
│   │   └── local               <--- Locally developed css functions
│   └── js                      <--- Stores Javascript
│       ├── ext                 <--- External javascript libraries
│       └── local               <--- Locally developed javascript, the filename should match the contoller/view/url that the function operates on
└── templates                   <--- Stores all html content
    ├── snips                   <--- Useful bytes of html that are used thorughout the project
    │   ├── base.html           <--- The base template that is inhereted by every page
    │   ├── contributors.html   <--- Template housing all the contributors to the project
    │   ├── footer.html         <--- Template used for the footer on all pages
    └── views                   <--- Stores all pages, an effort should be made to match contoller/views/urls with the same name
        ├── hello.html          <--- View for the hello controller
```

## Style
- All code should be comment, in particular any code added to the logic folder must have documentation
- Any code added should follow the pip8 standard

## Built With

* [Flask](http://flask.pocoo.org/docs/0.11/)  - Python Based Web Framework Used
* [Jinja2](http://jinja.pocoo.org/docs/dev/) - HTML Templating Language for Python
* [Peewee](http://docs.peewee-orm.com/en/latest/index.html) - A small, expressive ORM used for database communications
* [SQLite](https://sqlite.org/) - SQL database engine

## Deploying on a Server
### Dependencies
1. [Apache2](https://help.ubuntu.com/lts/serverguide/httpd.html) - `sudo apt-get install apache2`
2. [Python-Pip](https://pip.pypa.io/en/stable/) - `sudo apt-get install python-pip`
3. [Virtualenv](https://virtualenv.pypa.io/en/stable) - `sudo apt install virtualenv`
4. [WSGI](http://flask.pocoo.org/docs/0.11/deploying/mod_wsgi/) - `sudo apt-get install libapache2-mod-wsgi`
5. [Flask](http://flask.pocoo.org/docs/0.11/) - `sudo pip install Flask`

### Additional Server Setup:
These tools will require additional steps by your server admin in order to get the application running. 

1. [WSGI & Apache2 Sites-Enabled](http://flask.pocoo.org/docs/0.12/deploying/mod_wsgi/#installing-mod-wsgi)
2. [Logrotate](https://docs.google.com/document/d/1xtV__kmA8p0uTg_4TtbzYYLtqX5eZGckotQSmAvuCVA/edit?usp=sharing)
3. Shibboleth (Optional)

## Contributing
Contributions of all kinds are welcome, not only in the form of code. We openly
embrace that the systems were built with the intention of teaching Berea College 
students how to develop software. Therefore, if you believe that you could help 
us with our structure or coding standards feel free to contribute in that manner,
or by helping other users or our students within the issue queue. 

Additionally if you think something is bad about our documentation the way it is,
please feel free to help us make it better. We are new to the world of Open Source
after all. 

We do ask that you review the [CONTRIBUTING.md](CONTRIBUTING.md) before submitting
any pull request. We look forward to adding you to our community.

## Versioning
The versioning scheme that we use is [SemVer](http://semver.org/).

## Authors
1. [Cody Myers](http://github.com/myersCody)


## License

## Acknowledgments
* [Berea College](https://www.berea.edu/) for providing us the opportunity to have a student software developers group.
* [Our Community](CONTRIBUTORS.md) 
