from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import pandas as pd
import pickle

data = pd.read_csv('winereviews.csv')

X = data['review_description']
y = data['variety']

model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(X, y)

# Save the model to disk
pickle.dump(model, open('model.pkl', 'wb'))
