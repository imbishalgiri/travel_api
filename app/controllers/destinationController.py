from flask import request, jsonify
from app.models.destinations import add_trek
from app.controllers.constants import VALIDATION_ERR, CREATED, SUCCESS

from app.utils.decorators import token_required



@token_required
def add_trek_destination(user):
    data = request.get_json()
    try:
        title = data['title']
        days = data['days']
        total_cost = data['total_cost']
        difficulty = data['difficulty']
        # user id is optional to this endpoint
        user_id = None
        if 'uId' in data:
            user_id =  data['uId']

        if title and days and total_cost and difficulty:
            if add_trek(title, days, difficulty, total_cost, user_id):
                return jsonify(
                    message = "Successfully added trek destination", 
                    data = {
                        "title": title,
                        "days": days,
                        "total_cost": total_cost,
                        "difficulty": difficulty,
                        "user_id": user_id
                        }
                    ), SUCCESS

    except KeyError as err:
        return {"error": "You forgot {" + str(err) + "}"}, VALIDATION_ERR 
    