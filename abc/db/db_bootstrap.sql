CREATE DATABASE apartmentsNEU;

GRANT ALL PRIVILEGES ON apartmentsNEU.* TO 'webapp'@'%';
FLUSH PRIVILEGES;

use apartmentsNEU;


CREATE TABLE ageRange (
    ageRangeID INTEGER UNIQUE NOT NULL PRIMARY KEY,
    maximumAge INTEGER CHECK (maximumAge > 0),
    minimumAge INTEGER CHECK (minimumAge > 0)
);

INSERT INTO ageRange
VALUES (1, 21, 25), 
       (2, 18, 20),
       (3, 26, 150);


CREATE TABLE trait (
    traitID INTEGER UNIQUE NOT NULL PRIMARY KEY,
    earlyRiser BOOLEAN,
    smoker BOOLEAN,
    collegeStudent BOOLEAN,
    gender varchar(10),
    neatness INTEGER,
    social INTEGER,
    pets BOOLEAN,
    ageRangeID INTEGER NOT NULL,
    FOREIGN KEY (ageRangeID) REFERENCES ageRange(ageRangeID)
);

INSERT INTO trait
VALUES (1, 1, 1, 1, 'F', 1, 3, 0, 1),
       (2, 0, 1, 0, 'M', 4, 1, 1, 2),
       (3, 3, 1, 1, 'O', 0, 3, 2, 3);




CREATE TABLE realEstateCompany (
    companyName varchar(50) UNIQUE NOT NULL PRIMARY KEY,
    rating INTEGER,
    numberOfApartmentsOpenForRent INTEGER,
    companySize INTEGER,
    customerServiceNumber BIGINT
);

INSERT INTO realEstateCompany
VALUES ("The Company", 1, 13, 5, 834),
       ("Another Company", 4, 27, 15, 384),
       ("Third   Company", 2, 32, 23, 344);

CREATE TABLE realtor (
    realtorID INTEGER UNIQUE NOT NULL PRIMARY KEY,
    phoneNumber BIGINT,
    emailAddress varchar(100),
    neighborHoodOfConcentration varchar(100),
    yearlySalary BIGINT,
    companyName varchar(50),
    FOREIGN KEY (companyName) REFERENCES realEstateCompany(companyName)
);


INSERT INTO realtor
VALUES (1, 5593, "hello@gmail.com", "Fenway", 1234, "The Company"),
       (2, 5534, "anemail@gmail.com", "Jamaica Plain", 1234, "The Company"),
       (3, 3534, "goodbye@gmail.com", "Brookline", 1234, "Another Company");




CREATE TABLE apartment (
    apartmentID INTEGER UNIQUE NOT NULL PRIMARY KEY,
    realtorID INTEGER,
    FOREIGN KEY (realtorID) REFERENCES realtor(realtorID),
    numberOfBedrooms INTEGER,
    numberOfBedroomsForLease INTEGER,
    numberOfBathrooms INTEGER,
    monthRate INTEGER,
    carpeted BOOLEAN,
    squareFootage INTEGER
);

INSERT INTO apartment
VALUES (1, 2, 3, 0, 2, 2000, TRUE, 750),
       (2, 1, 13, 5, 1, 1234, TRUE, 413),
       (3, 2, 3, 1, 1, 3944, FALSE, 2343),
       (4, 3, 7, 3, 5, 3233, TRUE, 3413);



CREATE TABLE advertiser (
    advertiserID INTEGER UNIQUE NOT NULL PRIMARY KEY,
    traitHas INTEGER,
    FOREIGN KEY (traitHas) REFERENCES trait(traitID),
    firstName varchar(50),
    lastName varchar(50),
    email varchar(100),
    apartmentID INTEGER,
    FOREIGN KEY (apartmentID) REFERENCES apartment(apartmentID)
);


INSERT INTO advertiser
VALUES (1, 1, "maya", "zeldin", "mayazeldin@email.com", 1),
       (2, 2, "emma", "assaridoo", "emmasemail@yahoo.com", 2),
       (3, 3, "talia", "berdichevsky", "taliasemail@hotmail.com", 3);




CREATE TABLE availabilityTable (
    apartmentID INTEGER UNIQUE NOT NULL PRIMARY KEY,
    FOREIGN KEY (apartmentID) REFERENCES apartment(apartmentID),
    startMonth INTEGER,
    startYear INTEGER,
    endMonth INTEGER,
    endYear INTEGER
);


INSERT INTO availabilityTable
VALUES (1, 2, 2022, 12, 2022),
       (2, 4, 2023, 6, 2025),
       (3, 7, 2024, 2, 2027);


CREATE TABLE student (
    nuID INTEGER UNIQUE NOT NULL PRIMARY KEY,
    traitHas INTEGER NOT NULL,
    FOREIGN KEY (traitHas) REFERENCES trait(traitID),
    apartmentID INTEGER,
    FOREIGN KEY (apartmentID) REFERENCES apartment(apartmentID),
    firstName varchar(50),
    lastName varchar(50),
    budget BIGINT
);

INSERT INTO student
VALUES (1, 1, 1, "dina", "zeldin", 3434),
       (2, 2, 2, "ilana", "klaudia", 4000),
       (3, 3, 3, "maggie", "boston", 1050);





CREATE TABLE emergencyContact (
    studentID INTEGER NOT NULL PRIMARY KEY,
    FOREIGN KEY (studentID) REFERENCES student(nuID),
    firstName varchar(50),
    lastName varchar(50),
    phoneNumber BIGINT,
    relationship varchar(50)
);


INSERT INTO emergencyContact
VALUES (1, "olga", "zeldin", 6037, "mother"),
       (3, "boris", "zeldin", 7703, "father"),
       (2, "asder", "goldstein", 5545, "legal gaurdian");



CREATE TABLE utilities (
    apartmentID INTEGER UNIQUE NOT NULL PRIMARY KEY,
    FOREIGN KEY (apartmentID) REFERENCES apartment(apartmentID),
    water BOOLEAN,
    gas BOOLEAN,
    electric BOOLEAN,
    centralAir BOOLEAN
);

INSERT INTO utilities
VALUES (1, 1, 1, 0, 1),
       (2, 1, 0, 0, 1),
       (3, 0, 1, 0, 0);

CREATE TABLE generalAmenities (
    apartmentID INTEGER UNIQUE NOT NULL PRIMARY KEY,
    FOREIGN KEY (apartmentID) REFERENCES apartment(apartmentID),
    swimmingPool BOOLEAN,
    postOffice BOOLEAN,
    laundry BOOLEAN,
    gym BOOLEAN
);

INSERT INTO generalAmenities
VALUES (1, 1, 1, 0, 1), 
       (2, 1, 0, 0, 1),
       (3, 0, 1, 0, 0);




CREATE TABLE locationTable (
    apartmentID INTEGER UNIQUE NOT NULL PRIMARY KEY,
    FOREIGN KEY (apartmentID) REFERENCES apartment(apartmentID),
    neighborhood varchar(100),
    streetAddress varchar(100),
    zipCode INTEGER,
    floorNumber INTEGER
);

INSERT INTO locationTable
VALUES (1, "Fenway", "6 Bracebridge Rd", 02459, 2), 
       (2, "Jamaica Plain", "50 Leon St", 02114, 20),
       (3, "Roxbury", "73 Crossing Avenue", 02234, 7);




