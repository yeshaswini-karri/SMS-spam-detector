# SMS-spam-detector-Streamlit
This repository contains the code for an SMS Spam Detector built using Python, NLTK, and scikit-learn. The application preprocesses SMS messages to remove stopwords, vectorizes the text using CountVectorizer, and uses a trained logistic regression model to predict whether a message is spam or not.

#Features

Text Preprocessing: Tokenizes SMS messages, removes punctuation, and filters out stopwords.
Vectorization: Converts text data into numerical features using CountVectorizer with a maximum of 2000 features and n-grams (1,2).
Model Training: Uses logistic regression for binary classification (spam vs. ham).
Interactive Interface: Built with Streamlit to provide a user-friendly interface for entering SMS messages and displaying predictions

#Installation

1. Clone the repository:

git clone https://github.com/yourusername/sms-spam-detector.git
cd sms-spam-detector

2. Install the required packages:

pip install -r requirements.txt

3. Download NLTK stopwords:

import nltk
nltk.download('stopwords')
nltk.download('punkt')

4.Ensure SSL certificates are available:
Set the SSL_CERT_FILE environment variable if necessary:

import os
os.environ["SSL_CERT_FILE"]= "/path/to/your/certificate.pem"


#Usage


1. Run the Streamlit app:

streamlit run app.py

2.Enter an SMS message in the text input box and receive a prediction indicating whether the message is spam or not.

#Code Overview

data: Contains the spam_data.csv file used for training the model.
app.py: Main script to run the Streamlit app.
model.pkl: Pickle file containing the trained logistic regression model and CountVectorizer.
utils.py: Contains helper functions for text preprocessing and model prediction.
Model Training

The logistic regression model was trained using a dataset of SMS messages labeled as spam or ham. The text was preprocessed to remove stopwords and vectorized using CountVectorizer. The model was then trained and saved as a pickle file (model.pkl) for deployment.

#Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

#License

This project is licensed under the MIT License.

#Acknowledgments

This project uses Streamlit, NLTK, and scikit-learn.



