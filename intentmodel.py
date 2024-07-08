import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import pickle

def train_model():
    data = pd.read_csv("dataset.csv")
    X = data["command"]
    y = data["intent"]

    #logistic regression model
    model = Pipeline([
        ('vectorizer', TfidfVectorizer()),
        ('classifier', LogisticRegression())
    ])

    model.fit(X, y)

    with open("intentmodel.pkl", "wb") as f:
        pickle.dump(model, f)

if __name__ == "__main__":
    train_model()
