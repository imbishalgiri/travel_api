from flask import Flask, render_template,jsonify
from flask_mysqldb import MySQL
from os import environ

app = Flask(__name__)


# Database Configuration
app.config['MYSQL_HOST'] = environ.get('db_host')
app.config['MYSQL_USER'] = environ.get('db_user')
app.config['MYSQL_PASSWORD'] = environ.get('db_password')
app.config['MYSQL_DB'] = environ.get('db_name')

mysql = MySQL(app)
# Routes Imports Here 
from app.routes import travel_app
# ----------------------- End Of Imports

# Registering Routes Of Our App
app.register_blueprint(travel_app)


# Landing Page In Here
@app.route("/")
def landing_page():
    return jsonify(("message", "welcome to the app man ..."))

