import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
import joblib

data = pd.read_csv("dataset.csv")

X=data["url"]
y=data["label"]

vectorizer=CountVectorizer()

X_vector=vectorizer.fit_transform(X)

model=RandomForestClassifier()

model.fit(X_vector,y)

joblib.dump(model,"model.pkl")
joblib.dump(vectorizer,"vectorizer.pkl")

print("Model ready")