from dotenv import get_key
from flask import render_template, request, flash, jsonify
from app.models.auth import add_user, get_single_user, verify_password
from app.controllers.constants import VALIDATION_ERR, CREATED, SUCCESS
from app import app


#  ------- Login Controller Right here
def login():
    try:
        data = request.get_json()
        if data['email'] and data['password']:
            if verify_password(data['email'], data['password']):
                return "password matched", SUCCESS
            return "password did not match", VALIDATION_ERR
    except KeyError as err:
        return {"error": "You forgot {" + str(err) + "}"}, VALIDATION_ERR 

# --------- SIGNUP Controller Right here
def signup():
    
    try:
        data = request.get_json()
        if data['first_name'] and data['last_name'] and data['email'] and data['password']:
            if get_single_user(data['email']):
                return jsonify(message = "This user already exists"), VALIDATION_ERR
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

    
def add_to_db():
    return None