from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# __name__ is the name of the module where flask will look for 
# routes and templates, it is also the name of the current module
app = Flask(__name__)

app.config['SECRET_KEY'] = 'cd9c483fb7b4027e6b6fc2df9e813af8'
# Database configuration and initialization
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///planeador.db'
db = SQLAlchemy(app)

# This imports are made at the end of the file to avoid 
# circular imports
from planeador.api.routes import mod
from planeador.site.routes import mod

# Registration of the routes for the application
app.register_blueprint(site.routes.mod)
app.register_blueprint(api.routes.mod, url_prefix='/api')