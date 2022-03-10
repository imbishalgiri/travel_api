from dotenv import get_key
from flask import render_template, request, flash, jsonify
from app.models.auth import add_user, get_single_user, verify_password
from app.controllers.constants import VALIDATION_ERR, CREATED, SUCCESS
from os import environ
from app.utils.decorators import token_required

# it is being imported but idk why my vscode throws this linting error
import jwt
# ----------------------------------------------------------

#  ------- Login Controller Right here
def login():
    try:
        data = request.get_json()
        if data['email'] and data['password']:
            # if email and password matched, create a token and send back to the user
            if verify_password(data['email'], data['password']):
                token = jwt.encode({"email": data['email']},environ.get('JWT_SECRET'))
                return jsonify({"token": token})
            return jsonify({"Message": "Password did not match"}), VALIDATION_ERR
    except KeyError as err:
        return {"error": "You forgot {" + str(err) + "}"}, VALIDATION_ERR 

# --------- SIGNUP Controller Right here
def signup():
    try:
        data = request.get_json()
        if data['first_name'] and data['last_name'] and data['email'] and data['password']:
            # if user already exists in database return valid error message
            if get_single_user(data['email']):
                return jsonify(message = "This user already exists"), VALIDATION_ERR
            # in case there is no user, add em to the database and return their cred.
            if add_user(data['first_name'], data['last_name'], data['email'], data['password']):
                return jsonify(
                        message="succesfully signed up", 
                        data={
                                "first_name": data['first_name'],
                                "last_name": data['last_name'], 
                                "email": data['email']
                            }
                    ), CREATED
    except KeyError as err:
        return {"error": "You forgot {" + str(err) + "}"}, VALIDATION_ERR

@token_required
def add_to_db(user):
    return jsonify({"user": user})


