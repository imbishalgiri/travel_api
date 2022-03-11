from flask import Blueprint
from flasgger.utils import swag_from

# controllers import
from app.controllers.AuthController import login, signup, add_to_db
from app.controllers.destinationController import add_trek_destination, single_trek_controller
from flasgger.utils import swag_from

# Initializing blueprint to separate route
travel_app = Blueprint('travel_app', __name__)

# Auth Routes
@travel_app.route('/login', methods=['GET'])
@swag_from('documentation/auth.yml')
def do_login():
    return login()

@travel_app.route('/signup', methods=[ 'POST'])
@swag_from('documentation/signup.yml')
def do_signup():
    return signup()

travel_app.route('/db', methods=['GET','POST'])(add_to_db)

# destination routes
travel_app.route('/trek', methods=['GET', 'POST'])(add_trek_destination)

@travel_app.route('/trek/<id>', methods=['GET', 'DELETE', 'PUT'])
def get_trek(id):
    return single_trek_controller(id)