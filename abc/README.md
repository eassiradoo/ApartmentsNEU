# MySQL + Flask Boilerplate Project

This repo contains a boilerplate setup for spinning up 2 docker containers: 
1. A MySQL 8 container for obvious reasons
1. A Python Flask container to implement a REST API

## How to setup and start the containers
**Important** - you need Docker Desktop installed

1. Clone this repository.  
1. Create a file named `db_root_password.txt` in the `secrets/` folder and put inside of it the root password for MySQL. 
1. Create a file named `db_password.txt` in the `secrets/` folder and put inside of it the password you want to use for the `webapp` user. 
1. In a terminal or command prompt, navigate to the folder with the `docker-compose.yml` file.  
1. Build the images with `docker compose build`
1. Start the containers with `docker compose up`.  To run in detached mode, run `docker compose up -d`. 

## For setting up a Conda Web-Dev environment:

1. `conda create -n webdev python=3.9`
1. `conda activate webdev`
1. `pip install flask flask-mysql flask-restful cryptography flask-login`




# ApartmentsNEU is an online application used for students, advertisers, and realtors to look for apartments, post available apartments, and view the market, respectively. Users who are looking for a roommate or have an empty living space to fill out a form and connect to other users who are searching for a place to live through an expanding database of users. Users who are searching for a place to live can then filter through various inputs and contact those whose available space matches their needs. Realtors can observe general real estate rent trends for apartments, viewing specific details about the size and amenities of the living spaces.

This application utilizes bootstrap, MySQL, flask, and python to produce a comprehensive system.

We utilize 4 post requests and 4 get requests. 
We have two post requests for advertisers, including personal information and apartment details, a request for realtor information, and one for student information.
As for get requests, we have ones for apartment information, realtor details, the retrieval of all students, and another for apartment details.

# Link to Video: 
https://www.youtube.com/watch?v=-bn__Ai1YTQ&ab_channel=EmmaA
