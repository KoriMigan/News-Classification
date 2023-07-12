import numpy as np
import pandas as pd
import pickle
import requests
import json
import re
import string
from nltk.tokenize import word_tokenize
from flask import Flask, request, jsonify, render_template

#Loading the vectorizer
vectorizer = pickle.load(open('vectorizer.pkl','rb'))

def remove_emojis(text):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002500-\U00002BEF"  # Chinese/Japanese/Korean characters
                           u"\U00002702-\U000027B0"
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           u"\U0001f926-\U0001f937"
                           u"\U00010000-\U0010FFFF"
                           u"\u2640-\u2642"
                           u"\u2600-\u2B55"
                           u"\u200d"
                           u"\u23cf"
                           u"\u23e9"
                           u"\u231a"
                           u"\ufe0f"  # dingbats
                           u"\u3030"
                           "]+", flags=re.UNICODE)
    cleaned_text = emoji_pattern.sub(r'', text)
    return cleaned_text

# defining stopwords list
stopwords_swahili = ['akasema', 'alikuwa', 'alisema', 'baada', 'basi','bila', 'cha', 'chini', 'hadi', 'hapo', 'hata','hivyo', 'hiyo', 'huku', 'huo', 'ili',
'ilikuwa', 'juu', 'kama', 'karibu', 'katika', 'kila ', 'kima', 'kisha', 'kubwa', 'kutoka', 'kuwa', 'kwa', 'kwamba', 'kwenda', 'kwenye', 'la', 'lakini', 'mara',
'mdogo', 'mimi', 'mkubwa', 'mmoja', 'moja', 'muda', 'mwenye', 'na', 'naye', 'ndani', 'ng', 'ni', 'nini', 'pamoja', 'pia', 'sana', 'sasa', 'sauti', 'tafadhali', 'tena',
'tu', 'ule', 'vile', 'wa', 'wakati', 'wake', 'walikuwa', 'wao', 'watu', 'wengine', 'wote', 'ya', 'yake', 'yangu', 'yao', 'yeye', 'yule', 'za', 'zaidi', 'zake', 'vya']

# function to remove stopwords
def swahili_stops(text):
    no_stops = " ".join([word for word in text.split() if word not in stopwords_swahili])
    return no_stops

# punctuation
exclude = string.punctuation

# remove punctuations
def remove_punctuations(text):
    
    for char in exclude:
        text = text.replace(char,'')
    return text


def preprocess_text(text):
    # Transform text to lowercase
    text = text.lower()
    #removing emojis
    text = remove_emojis(text)
    # Remove stopwords
    text = swahili_stops(text)
    # Remove punctuations
    text = remove_punctuations(text)
    #Tokenizing 
    text = word_tokenize(text)
    #joining
    text = " ".join(text)

    text = [text]
    #vectorizing
    vector = vectorizer.transform(text)

    return vector

# Loading model to compare the results
app = Flask(__name__)
model = pickle.load(open('random_model.pkl','rb'))

category = {0: 'afya', 1: 'burudani', 2: 'kimataifa', 3: 'kitaifa', 4: 'michezo', 5: 'uchumi'}



@app.route('/')
def home():
    return 'welcome'

@app.route('/predict',methods=['POST'])
def predict():
    data = request.get_json(force=True)
    text = data['text']
    preprocessed_text = preprocess_text(text)
    prediction = model.predict(preprocessed_text)
    output = prediction[0]
    return jsonify({'prediction': category[output]})

if __name__ == "__main__":
    app.run(debug=True)
   


    
    






