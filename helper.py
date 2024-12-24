import numpy as np
import pandas as pd
import re
import string
import pickle
from nltk.stem import PorterStemmer

# Function to remove punctuation
def remove_punctuations(text):
    for punctuation in string.punctuation:
        text = text.replace(punctuation, '')
    return text

# Load stopwords
with open("modle/corpora/stopwords/english", 'r') as file:
    sw = file.read().splitlines()

# Load the model
with open("modle/modle.pickle", "rb") as f:
    modle = pickle.load(f)

# Load vocabulary
vocab = pd.read_csv("modle/vocabulary.txt", header=None)
tokens = vocab[0].tolist()



# Initialize stemmer
ps = PorterStemmer()

# Preprocessing function
def preprocessing(text):
    data = pd.DataFrame([text], columns=["tweet"])
    data["tweet"] = data["tweet"].apply(lambda x: " ".join(x.lower() for x in x.split()))
    data["tweet"] = data["tweet"].apply(lambda x: " ".join(re.sub(r'^https?:\/\/.*[\r\n]*', '', x, flags=re.MULTILINE) for x in x.split()))
    data["tweet"] = data["tweet"].apply(remove_punctuations)
    data["tweet"] = data["tweet"].replace(r'\d+', ' ', regex=True)
    data["tweet"] = data["tweet"].apply(lambda x: " ".join(x for x in x.split() if x not in sw))
    data["tweet"] = data["tweet"].apply(lambda x: " ".join(ps.stem(x) for x in x.split()))
    return data["tweet"]

# Vectorizer function
def vectorizer(ds, tokens):
    vocab_dict = {word: idx for idx, word in enumerate(tokens)}
    
    vectorized_lst = []
    for sentence in ds:
        sentence_vector = np.zeros(len(tokens), dtype=np.float16)
        for word in sentence.split():
            if word in vocab_dict:
                sentence_vector[vocab_dict[word]] = 1
        vectorized_lst.append(sentence_vector)
    
    return np.array(vectorized_lst, dtype=np.float32)

# Prediction function
def get_prediction(vectorized_txt):
    prediction = modle.predict(vectorized_txt)[0]  # Get the first prediction
    if prediction == 1:
        return "negative feedback"
    else:
        return "positive feedback"


print(vocab)