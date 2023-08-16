# JTP_TechnicalProject

This is a travel destination recommendation webapp. 

It asks the user to describe the kind of place they wish to visit, and on querying a subset database (~40000 records) of rated places in India, it provides the user with the top 10 recommendations. 

The project uses NLP for the recommendation process, tokenising the reviews made by travellers for various popular destinations, applying TFIDF vectorisation and then comparing the cosine similarity with the user input post similar processing. 

The database used is from https://www.kaggle.com/datasets/ritvik1909/indian-places-to-visit-reviews-data . However, only reviews with ratings of 5 stars were extracted and the dataset was limited to the top 40000 indices (ordered lexicographically), hence the recommendation engine would have a major regional bias. 

Furthermore, since the database contains cleaned data, preprocessing such as lemmatisation, stemming and removal of stopwords need not be done. However, certain level of preprocessing has to be done for the user input. 

Additionally, an approach of topic modelling using Non-negative Matrix Factorisation (NMF) had been attempted, however it has been commented out. 

The project has been primarily organised into the backend and frontend directories. Flask has been utilised for implementing the backend while VueJS/Node has been chosen for the frontend. Axios has been used for the HTTP requests and separate docker containers have been built for each directory linked through docker compose.  

Run "docker compose up" on the working directory to run the containers and view the project live on the local machine. Ports 5001 and 5173 are set by default. 

NOTE: The dataset can be downloaded from the kaggle link and placed in ./backend/data/ as Review_db.csv to run the code. Due to size constraints (>540mb) the same was not uploaded. 

NOTE 2: Due to development on Apple silicon, lot of dependencies had to be installed through conda. As such, these when listed in the requirements.txt file break the docker image from building. The problem persists and the recourse seems to be raising warnings or exceptions when encountering these packages. 

https://github.com/ploomber/soopervisor/issues/67 Mentions a potential workflow workaround. 
