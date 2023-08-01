# JTP_TechnicalProject
 
This project uses Vue JS for the front end wherein user input is taken to understand the user's location of travel destination, their place of search and the number of options to be displayed. 

The frontend is connected to a backend powered by flask, using APIs from Geoapify.com. 

Two APIs are used - the first retrieves a place(id for the location inputted, and the second retrieves the places of interest as per the place_id abding by the limit opted by the user. 

The project has two separate docker containers - one for the backend running on node and the other for the front end running on flask. 

RUn "docker compose up" on the working directory to run the containers and view the project live on the local machine.
