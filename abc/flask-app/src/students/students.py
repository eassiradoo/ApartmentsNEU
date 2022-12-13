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


# what shows up after user submits form
# puts the students information into the database
@student.route('/studentsForm', methods=['POST'])
def post_form():
    current_app.logger.info(request.form)
    cursor = db.get_db().cursor()

    # post request: what should computer do after it gets data
    # get variables from post request
    first_name = request.form['first']
    last_name = request.form['last']
    smoker = request.form['smoker']
    pet = request.form['pet']
    early = request.form['early']
    college = 1
    social = request.form['social']
    neat = request.form['neat']
    gender = request.form['gender']
    age = request.form['age']


    eFirst = request.form['efirst']
    eLast = request.form['elast']
    eNumber = request.form['number']
    eRelationship = request.form['relationship']
    numID = random.randint(0, 10000)

    query1 = f'Insert Into trait Values ( \"{early}\", \"{smoker}\", \
            \"{gender}\", \"{neat}\", \"{social}\", \"{pet}\", \"{age}\")'

    query2 = f'Insert Into student(nuID, firstName, lastName) Values (\
    \"{first_name}\", \"{last_name}\")'

    query3 = f'Insert Into emergencyContact Values (\"{eFirst}\", \"{eLast}\", \
    \"{eNumber}\", \"{eRelationship}\")'

    cursor.execute(query1)
    cursor.execute(query2)
    cursor.execute(query3)

    db.get_db().commit()
    cursor.connection.commit()
    return "success"