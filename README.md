# JTP_TechnicalProject

## Project Overview
This is a travel destination recommendation webapp. 

It asks the user to describe the kind of place they wish to visit within India; the input is used to query a subset database (~40000 records) of Indian destinations rated and reviewed by travellers, providing the user with top 10 recommendations. 

The project uses Natural Language Processing for the recommendation process, tokenising the reviews made by travellers, applying TFIDF vectorisation and then comparing the cosine similarity with the user input which is similarly processed. 

The database used is from https://www.kaggle.com/datasets/ritvik1909/indian-places-to-visit-reviews-data . However, only reviews with ratings of 5 stars were extracted and the dataset was limited to the top 40000 indices (ordered lexicographically), hence the recommendation engine would have a major regional bias. 

Furthermore, since the database contains cleaned data, preprocessing such as lemmatisation, stemming and removal of stopwords need not be done. However, certain level of preprocessing has to be performed for the user input. Additionally, an approach of topic modelling using Non-negative Matrix Factorisation (NMF) had been attempted, however it has been commented out. 

The project has been organised into the backend and frontend directories. Flask has been utilised for implementing the backend while VueJS/Node has been chosen for the frontend. Axios has been used for the HTTP requests and separate docker containers have been built for each directory linked through docker compose.  

## Running the Project

Download the project (as a zip file) or fork it to your own repository. Place it an appropriate local directory.

Due to size constraints (>540mb) the dataset has not been uploaded to github. The dataset can be downloaded from the aforementioned kaggle link and placed in ./backend/data/ as Review_db.csv to run the code. 

Navigate to the directory where the project has been downloaded/forked. Run "docker-compose up -d --build" from the main directory. 

Run "docker compose up" in the same working directory. This would run the containers and the project would be made live on the local machine. Ports 5001(flask) and 5173(node) are set by default.

Navigate to the url http://0.0.0.0:5173/nlp on your browser to view the project. 

NOTE 1: On submitting the input on http://0.0.0.0:5173/nlp, the user must click the "Submit" button and then click on the "Get Results" button. This would redirect the user to http://0.0.0.0:5173/places. However, due to the size of the dataset and the lack of optimisations, it takes a few minutes for the results to load. The same can be observed by inspecting the elements of the page via the developer console. 

## Project Images

![image](https://github.com/TheAnishSudhan/JTP_TechnicalProject_TravelDestination_Recommendation/assets/64979922/308d00f3-08c1-4ef2-8942-9b642dde8a7c)

![image](https://github.com/TheAnishSudhan/JTP_TechnicalProject_TravelDestination_Recommendation/assets/64979922/faf2f490-33e7-4f48-8c4a-d3e924680322)

![Screenshot 2023-08-17 at 4 03 31 AM](https://github.com/TheAnishSudhan/JTP_TechnicalProject_TravelDestination_Recommendation/assets/64979922/b4fd9f37-a89f-4899-913c-3cf18fecc341)

