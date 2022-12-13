from flask import Blueprint, jsonify, request, redirect, url_for, current_app
from flaskext.mysql import MySQL
import random
from src import db

# blueprint allows you to modulize your code
# add routes to blueprint here -> add blueprint to app.py
realtor = Blueprint('realtor', __name__)



# returns all apartments so realtors can see all other openings
@realtor.route('/realtor/allApartments', methods=['GET'])
def get_all_apartments():
    cur = db.get_db().cursor()

    cur.execute('select * from apartment natural join utilities')
    col_headers = [x[0] for x in cur.description]
    # creates container
    json_data = []
    the_data = cur.fetchall()
    for row in the_data:
        json_data.append(dict(zip(col_headers, row)))
    return jsonify(json_data)


# get the data about the other realtors using this application and
# the information about the company
# they work for
@realtor.route('/realtorInformation', methods=['GET'])
def get_all_realtors():
    cur = db.get_db().cursor()

    # get all data from db
    cur.execute('select * from realtor')
    col_headers = [x[0] for x in cur.description]
    # creates container
    json_data = []
    the_data = cur.fetchall()
    for row in the_data:
        json_data.append(dict(zip(col_headers, row)))
    return jsonify(json_data)


@realtor.route('/realtorPutInformation', methods=['POST'])
def realtor_form():
    current_app.logger.info(request.form)
    cursor = db.get_db().cursor()

    # post request: what should computer do after it gets data
    # get variables from post request
    email = request.form['email']
    phone = request.form['phone']
    salary = request.form['salary']
    neighborhood = request.form['neighborhood']
    companyName = request.form['companyName']
    companyApartments = request.form['companyApartments']
    companyRating = request.form['companyRating']
    companySize = request.form['companySize']
    companyPhone = request.form['companyPhone']
    numID = random.randint(0, 1000)

    query1 = f'Insert Into realEstateCompany Values (\"{companyName}\", \"{companyRating}\", \
            \"{companyApartments}\", \"{companySize}\", \"{companyPhone}\")'
    cursor.execute(query1)

    query2 = f'Insert Into realtor Values \
         (\"{numID}\", \"{phone}\", \"{email}\", \
         \"{neighborhood}\", \"{salary}\", \"{companyName}\")'

    cursor.execute(query2)
    db.get_db().commit()
    cursor.connection.commit()
    return "success"
