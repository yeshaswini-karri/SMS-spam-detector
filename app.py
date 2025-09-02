import streamlit as st
import pandas as pd 
import pickle
import warnings
from sklearn.exceptions import InconsistentVersionWarning
import nltk
nltk.download('stopwords')
nltk.download('punkt')


warnings.filterwarnings("ignore", category=InconsistentVersionWarning)
import nltk
import os
os.environ["SSL_CERT_FILE"]= "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/certifi/cacert.pem"


from nltk.corpus import stopwords

st.header("SMS Spam Detection")

input = st.text_input("Enter the SMS", "Hey! You are using a streamlit application created by Yeshaswini.")


stop_words = set(stopwords.words('english'))

def splitinwords(message):
    answer = []
    words = message.split()
    for word in words:
        j = len(word)-1
        word = word.lower()
        while(j>= 0 and (word[j]==',' or word[j]=='.')):
            j = j-1
        result = word[0:j+1]
        if result not in stop_words:
            answer.append(result)
    return_answer = ' '.join(answer)
    return return_answer     

input = splitinwords(input)


with open('model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)
    loaded_count_vec = loaded_model['count_vec']
    loaded_logistic_model = loaded_model['logistic_model']
    input = loaded_count_vec.transform([input])
    output = loaded_logistic_model.predict(input)
    if(output=='ham'):
        st.subheader("Probably a Safe SMS!")
    else:
        st.subheader("Probably a SPAM SMS")
    y_pred_proba = loaded_logistic_model.predict_proba(input)
    st.subheader("")
    st.subheader("The prediction probabilities are:")
    st.write(y_pred_proba)

