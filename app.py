# Entry point for the project
# Main file
# Everything will be included here

from distutils.log import debug
from app import app

if __name__ == '__main__':
    app.run(debug=True)


















# @app.route("/db")
# def check_db():
#     cnx = MySQLdb.connect(user="root",password="Root@123",host="localhost",database="db_travel")
#     if cnx:
#         return "connection was successful"

#     return "db connection screwed"

