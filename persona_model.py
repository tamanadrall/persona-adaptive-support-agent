import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Training data
data = {
    "text": [
        "The API is returning 500 error",
        "Check server logs for debugging",
        "This app keeps crashing I am frustrated",
        "I am very unhappy with the service",
        "How does this impact revenue?",
        "What is the business impact?"
    ],
    "persona": [
        "technical",
        "technical",
        "frustrated",
        "frustrated",
        "executive",
        "executive"
    ]
}

df = pd.DataFrame(data)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["text"])

model = LogisticRegression()
model.fit(X, df["persona"])

def detect_persona(user_input):
    vec = vectorizer.transform([user_input])
    return model.predict(vec)[0]
    