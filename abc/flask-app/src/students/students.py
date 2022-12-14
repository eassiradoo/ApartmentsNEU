from flask import Blueprint, jsonify, request, redirect, url_for, current_app
from src import db
import random

# blueprint allows you to modulize your code
# add routes to blueprint here -> add blueprint to app.py
student = Blueprint('stud', __name__)


# returns all of the apartments are posted on the site
@student.route('/students/all', methods=['GET'])
def get_all_apartments():
    cur = db.get_db().cursor()

    # get all data from db
    cur.execute('select * from apartment natural join utilities')
    col_headers = [x[0] for x in cur.description]
    # creates container
    json_data = []
    the_data = cur.fetchall()
    for row in the_data:
        json_data.append(dict(zip(col_headers, row)))
    return jsonify(json_data)




# returns only the apartments that currently have openings
@student.route('/students/availableApartments', methods=['GET'])
def get_available():
    cur = db.get_db().cursor()

    # get all data from db
    cur.execute('select * from apartment where numberOfBedroomsForLease > 0')
    col_headers = [x[0] for x in cur.description]
    # creates container
    json_data = []
    the_data = cur.fetchall()
    for row in the_data:
        json_data.append(dict(zip(col_headers, row)))
    return jsonify(json_data)


# returns on the apartments that have central air in order to attract
# a more high-class clientelle
@student.route('/students/centralAir', methods=['GET'])
def get_all_utilities():
    cur = db.get_db().cursor()

    # get all data from db
    cur.execute('select * from apartment natural join utilities where centralAir = 1')
    col_headers = [x[0] for x in cur.description]
    # creates container
    json_data = []
    the_data = cur.fetchall()
    for row in the_data:
        json_data.append(dict(zip(col_headers, row)))
    return jsonify(json_data)