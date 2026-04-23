import joblib
import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Charger le modèle et le vectorizer
def load_all():
    model = joblib.load("Modele/model.pkl")
    vectorizer = joblib.load("Modele/vectorizer.pkl")

    # Charger dataset
    with open("data/INTENT.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    texts = []
    labels = []

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            texts.append(pattern)
            labels.append(intent["tag"])

    X = vectorizer.transform(texts)

    return model, vectorizer, X, labels


# 🔹 Cosine similarity
def detect_intent_cosine(message, vectorizer, X, labels):
    X_input = vectorizer.transform([message])

    similarities = cosine_similarity(X_input, X)[0]

    best_idx = np.argmax(similarities)
    return labels[best_idx], similarities[best_idx]


# 🔹 ML
def detect_intent_ml(message, model, vectorizer):
    X = vectorizer.transform([message])
    intent = model.predict(X)[0]
    score = model.predict_proba(X).max()
    return intent, score


# 🔥 HYBRIDE
def detect_intent(message, model, vectorizer, X, labels):

    # 1. Cosine
    intent_cos, score_cos = detect_intent_cosine(message, vectorizer, X, labels)

    if score_cos > 0.7:
        return intent_cos, score_cos, "cosine"

    # 2. ML fallback
    else:
        intent_ml, score_ml = detect_intent_ml(message, model, vectorizer)

    return intent_ml, score_ml, "ml"


# Test local
if __name__ == "__main__":
    model, vectorizer, X, labels = load_all()

    while True:
        msg = input("Message: ")

        intent, score, method = detect_intent(msg, model, vectorizer, X, labels)

        print(f"Intent : {intent} | score={score:.2f} | méthode={method}")