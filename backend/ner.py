
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import nltk
from nltk import word_tokenize
from nltk.util import ngrams
from nltk.corpus import wordnet as WN
from nltk.corpus import stopwords, words
import warnings
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import NMF
import re

#Run them once to download the dependencies
nltk.download('stopwords')
nltk.download('punkt')

# warnings.filterwarnings('ignore')

#Reading the dataset into a dataframe
#Download the dataset from kaggle and place it into the data subdirectory
raw_data_csv = pd.read_csv('./data/Review_db.csv')
raw_data_csv.to_pickle('./data/Review_db.pkl')   
raw_data = pd.read_pickle('./data/Review_db.pkl') 

# The dataset used consists of cleaned (lemmatised, stemmed) review data, hence there is no need for preprocessing
cleaned_data = raw_data[['City','Place','Review','Raw_Review','Rating']]
cleaned_data.dropna(inplace = True)

#Extracting only the positive reviews from the dataset
#Considering obly 5 star rated places due to vastness of dataset
positive_review_data=cleaned_data[cleaned_data['Rating'] == 5 ]

#Creating a copy of the data susbset 
copy_data=positive_review_data.copy()

#Function for tokenizing dataset reviews
def tokenize(df):
    df["tokens"] = df["Review"].apply(lambda row: word_tokenize(row))
    return df

positive_review_data = positive_review_data.head(40000)

#Calling the tokenization function to tokenize the cleaned positive dataset review
# positive_review_data = tokenize(positive_review_data)

#Using TFIDF vectorizer to generate numerical vectors for the tokens
vectorizer = TfidfVectorizer(analyzer = 'word')
vectorizer.fit(positive_review_data['Review'])

#Alternative approach using NMF for topic modelling
tem_doc = vectorizer.fit_transform(positive_review_data['Review'].to_list())
num_topics = 10
nmf = NMF(num_topics)
doc_topic = nmf.fit_transform(tem_doc)

def docs_with_topics(doc_topic,name,num_topics):
    return pd.DataFrame(doc_topic.round(5), index = name, columns = ["Topic "+str(i) for i in range(num_topics)])

nmf_results = docs_with_topics(doc_topic,positive_review_data['Place'].to_list(),num_topics)

#Function for NMF approach 
def new_f(user_input):
    
    user_input_array = vectorizer.transform(user_input)
    user_topics = nmf.transform(user_input_array)
    cosines = cosine_similarity(user_topics, nmf_results)
    idx = cosines[0].argsort()[-3:][::-1]
    print(idx)
    score = np.max(cosines[0])
    for i in range(len(idx)):
        print(f"Place #{i}", positive_review_data["Place"][idx[i]])
        # print("Read what a guest wrote: ", pos.iloc[idx[i],:].content)
    
    return score
      
#Function for calculating similarity between user input and the dataset reviews
def cos_similarity(user_input, data=positive_review_data):
        
	# Getting vector for the user input 
	user_input_array = vectorizer.transform(user_input).toarray()
    
	# Storing cosine similarity for each row of the dataset in thie list
	sim = []
	
	for idx,row in data.iterrows():
		review = row['Review']

		# Getting vector for dataset reviews
		dataset_review_array = vectorizer.transform(
			data[data['Review'] == review]['Review']).toarray()

		# Calculating cosine similarities
		cos_sim = cosine_similarity(user_input_array, dataset_review_array)[0][0]
                
		sim.append(cos_sim)

	return sim

#Function for generating recommendations of places
def recommend_place(user_input, data=positive_review_data):
        
	user_input = clean_single(user_input).split(maxsplit=0)
    
	#For NMF approach, uncomment the following
	# user_input = clean_single(user_input) 
        
	data['cos_sim'] = cos_similarity(user_input)
    
	data.sort_values(by=['cos_sim'], ascending=False, inplace=True)
    
	data=data.drop_duplicates(subset='Place')
    
	data=data.reset_index()

	# print(data[['City', 'Place', 'Raw_Review']].head(10))
        
	recommendations = []

	for i in range(10):
        	recommendations.append({'Place': data['Place'][i],
            							'City': data['City'][i],
            							'Raw_Review': data['Raw_Review'][i]})
    
	print(recommendations)
	return recommendations

#Function for removing the punctions and abbrevations from user input
def punctuations(text):
    text = re.sub(r"[^a-z0-9(),!.?\'`]", " ", text)
    text = re.sub(r"\'s", "", text)
    text = re.sub(r"\'ve", " have", text)
    text = re.sub(r"\'re", " are ", text)
    text = re.sub(r"\'d", " would ", text)
    text = re.sub(r"\'ll", " will ", text)
    text = re.sub(r"[(),!.?\'`]", "", text)
    text = re.sub(r"\s{2,}", " ", text)
    text = re.sub(r"\s[a-z]{1,2}\s", " ", text)
    return text

#Function for cleaning user input
def clean_single(row):
    row = row.strip().lower()
    return punctuations(row)

# user_input = 'I want to go to a place with a lot of caves'
# user_input = 'I want to go to an old garden'

# recommend_place(user_input)

# new_f(user_input)

#For NMF approach, uncomment the following
# if __name__ == '__main__':
#     print(new_f("I want to go an old temple"))


if __name__ == '__main__':
    print(recommend_place("I want to go an old temple"))