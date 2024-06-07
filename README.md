# SMS-spam-detector-Streamlit
This repository contains the code for an SMS Spam Detector built using Python, NLTK, and scikit-learn. The application preprocesses SMS messages to remove stopwords, vectorizes the text using CountVectorizer, and uses a trained logistic regression model to predict whether a message is spam or not.

Features

Text Preprocessing: Tokenizes SMS messages, removes punctuation, and filters out stopwords.
Vectorization: Converts text data into numerical features using CountVectorizer with a maximum of 2000 features and n-grams (1,2).
Model Training: Uses logistic regression for binary classification (spam vs. ham).
Interactive Interface: Built with Streamlit to provide a user-friendly interface for entering SMS messages and displaying predictions

Installation

1. Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/sms-spam-detector.git
cd sms-spam-detector

