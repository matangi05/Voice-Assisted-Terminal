import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import pickle

def train_model():
    # Load dataset
    data = pd.read_csv("dataset.csv")
    X = data["command"]
    y = data["intent"]

    #logistic regression model
    model = Pipeline([
        ('vectorizer', TfidfVectorizer()),
        ('classifier', LogisticRegression())
    ])

    # Train the model
    model.fit(X, y)

    # Save the model
    with open("intentmodel.pkl", "wb") as f:
        pickle.dump(model, f)

if __name__ == "__main__":
    train_model()
