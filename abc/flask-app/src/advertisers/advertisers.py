from flask import Blueprint, request, current_app
import random
from src import db

# blueprint allows you to modulize your code
# add routes to blueprint here -> add blueprint to app.py
advertiser = Blueprint('advertiser', __name__)


# what shows up after user submits form
# puts the students information into the database
@advertiser.route('/advertiserForm', methods=['POST'])
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
    college = request.form['college']
    social = request.form['social']
    neat = request.form['neat']
    gender = request.form['gender']
    age = request.form['age']
    email = request.form['email']
    numID = random.randint(0, 10000)

    query1 = f'Insert Into trait Values (\"{numID}\", \"{early}\", \"{smoker}\", \"{college}\", \
            \"{gender}\", \"{neat}\", \"{social}\", \"{pet}\", \"{age}\")'
    cursor.execute(query1)

    query2 = f'Insert Into advertiser(advertiserID, traitHas, firstName, lastName, email) Values (\"{numID}\", \
     \"{numID}\", \"{first_name}\", \"{last_name}\", \"{email}\")'
    cursor.execute(query2)
    db.get_db().commit()
    cursor.connection.commit()
    return "success"


# what shows up after user submits form
# puts the students information into the database
@advertiser.route('/advertiserHouseForm', methods=['POST'])
def post_house():
    current_app.logger.info(request.form)
    cursor = db.get_db().cursor()

    # post request: what should computer do after it gets data
    # get variables from post request
    monthlyRent = request.form['monthlyRent']
    squareFootage = request.form['squareFootage']
    streetAddress = request.form['streetAddress']
    neighborhood = request.form['neighborhood']
    numberOfBedrooms = request.form['numberOfBedrooms']
    availableBedrooms = request.form['bedroomsAvailable']
    numberOfBathrooms = request.form['numberOfBathrooms']

    carpeted = request.form['carpeted']
    pool = request.form['pool']
    post = request.form['post']
    laundry = request.form['laundry']
    gym = request.form['gym']
    ac = request.form['ac']
    gas = request.form['gas']
    electric = request.form['electric']
    water = request.form['water']

    numID = random.randint(0, 1000)

    query4 = f'Insert Into apartment(apartmentID, numberOfBedrooms, numberOfBedroomsForLease, \
            numberOfBathrooms, monthRate, carpeted, squareFootage) \
            Values (\"{numID}\", \"{numberOfBedrooms}\", \"{availableBedrooms}\", ' \
             f'\"{numberOfBathrooms}\", \"{monthlyRent}\", \"{carpeted}\", \"{squareFootage}\")'
    cursor.execute(query4)

    query1 = f'Insert Into utilities Values (\"{numID}\", \"{water}\", \"{gas}\", \"{electric}\",  \"{ac}\")'
    cursor.execute(query1)

    query2 = f'Insert Into generalAmenities Values (\"{numID}\", \"{pool}\", \"{laundry}\", \"{post}\",  \"{gym}\")'
    cursor.execute(query2)

    query3 = f'Insert Into locationTable(apartmentID, neighborhood, streetAddress) Values (\"{numID}\", \"{neighborhood}\", \"{streetAddress}\")'
    cursor.execute(query3)


    db.get_db().commit()
    cursor.connection.commit()
    return "Success"
