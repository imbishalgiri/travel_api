from flask import Blueprint

# controllers import
from app.controllers.AuthController import login_page, signup, add_to_db

# Initializing blueprint to separate route
travel_app = Blueprint('travel_app', __name__)

# Auth Routes
travel_app.route('/login', methods=['GET'])(login_page)
travel_app.route('/signup', methods=['GET', 'POST'])(signup)
travel_app.route('/db', methods=['GET','POST'])(add_to_db)

