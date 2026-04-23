import os
import json
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


def train_model_if_needed():
    model_dir = "Modele"
    model_path = os.path.join(model_dir, "model.pkl")
    vectorizer_path = os.path.join(model_dir, "vectorizer.pkl")

    if os.path.exists(model_path) and os.path.exists(vectorizer_path):
        print("✅ Modèle déjà existant")
        return None

    print("⚠️ Aucun modèle trouvé → entraînement en cours...")

    # Charger dataset
    with open("data/INTENT.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    texts = []
    labels = []

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            texts.append(pattern)
            labels.append(intent["tag"])

    # Split train/test
    X_train, X_test, y_train, y_test = train_test_split(
        texts, labels, test_size=0.2, random_state=42, stratify=labels
    )

    # Vectorisation (fit uniquement sur train !)
    vectorizer = TfidfVectorizer(ngram_range=(1, 2))
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    # Modèle
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train_vec, y_train)

    # Évaluation
    y_pred = model.predict(X_test_vec)
    print("\n📊 Rapport de classification :\n")
    print(classification_report(y_test, y_pred))

    # Création dossier
    os.makedirs(model_dir, exist_ok=True)

    # Sauvegarde
    joblib.dump(model, model_path)
    joblib.dump(vectorizer, vectorizer_path)

    print("✅ Modèle entraîné et sauvegardé")