from crypt import methods
from flask import Flask,jsonify
from flask_mysqldb import MySQL
from os import environ
from flasgger import Swagger
from flasgger.utils import swag_from


app = Flask(__name__)

# Database Configuration
app.config['MYSQL_HOST'] = environ.get('db_host')
app.config['MYSQL_USER'] = environ.get('db_user')
app.config['MYSQL_PASSWORD'] = environ.get('db_password')
app.config['MYSQL_DB'] = environ.get('db_name')
mysql = MySQL(app)

# Swagger configuration 
base = {
    "swagger": "2.0",
    "info": {
        "title": "Travel API",
        "description":"Api documentation for Travel App (COLLEGE INTERNAL PROJECT)",
    },
    "host": "127.0.0.1:5000/",
    "schemes": ["http", "https"]
    
}
swagger = Swagger(app, template=base)

# Routes Imports Here 
from app.routes import travel_app
# ----------------------- End Of Imports

# Registering Routes Of Our App
app.register_blueprint(travel_app)


# Landing Page In Here
@app.route("/", methods=['get'])
@swag_from("documentation/landing.yml")
def landing_page():
    return jsonify(title = "Landing page", des = "Welcome")



