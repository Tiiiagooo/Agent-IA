# 🏠 Agent IA — Assistant Conversationnel pour Locations Courte Durée

> Un agent IA capable de répondre automatiquement aux questions des locataires sur leur appartement, sans solliciter le propriétaire.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![LLM](https://img.shields.io/badge/LLM-Agent_IA-green)
![Status](https://img.shields.io/badge/Status-En%20cours-orange)

---

## 🎯 Objectif

Les propriétaires Airbnb et gestionnaires de locations courte durée reçoivent constamment les mêmes questions de leurs locataires : comment fonctionne le chauffage ? Où sont les clés ? Quel est le code wifi ? À quelle heure est le check-out ?

Ce projet propose un agent IA conversationnel capable de répondre à ces questions de façon autonome, en s'appuyant sur les informations fournies par le propriétaire. Résultat : moins de sollicitations pour le propriétaire, une meilleure expérience pour le locataire.

---

## ✨ Fonctionnalités

**Pour le locataire :**
- Poser des questions en langage naturel sur l'appartement
- Obtenir des réponses instantanées 24h/24 sans attendre le propriétaire
- Accéder aux consignes, équipements et informations pratiques

**Pour le propriétaire :**
- Renseigner une base de connaissances sur son appartement une seule fois
- Ne plus être sollicité pour les questions récurrentes
- Exposer l'agent via une URL publique (ngrok) accessible depuis n'importe quel appareil

---

## 🏗️ Architecture

```
├── Modele/                  # Modèles et configuration LLM
├── function/                # Fonctions utilitaires de l'agent
├── main.py                  # Point d'entrée principal de l'agent
├── test_connexion.ipynb     # Tests de connexion et intégration
├── test_model.ipynb         # Tests du modèle et des réponses
└── ngrok.exe                # Exposition locale via URL publique
```

---

## 🧠 Choix techniques

| Composant | Choix | Justification |
|---|---|---|
| Agent conversationnel | LLM (Mistral / GPT) | Compréhension du langage naturel |
| Base de connaissances | RAG sur FAQ propriétaire | Réponses ancrées dans les vraies infos de l'appartement |
| Exposition | ngrok | URL publique accessible sans serveur cloud |
| Interface | En cours (Streamlit / WhatsApp) | Accessible depuis mobile |

---

## 🚀 Installation

```bash
git clone https://github.com/Tiiiagooo/Agent-IA.git
cd Agent-IA

pip install -r requirements.txt

python main.py
```

---

## 🗺️ Roadmap

- [x] Architecture de base de l'agent
- [x] Connexion au modèle LLM
- [x] Exposition via ngrok
- [ ] Base de connaissances RAG sur les infos de l'appartement
- [ ] Interface conversationnelle mobile (WhatsApp / Streamlit)
- [ ] Intégration domotique (volets, chauffage, consommation)
- [ ] Dashboard propriétaire pour gérer les informations
- [ ] Version SaaS pour Airbnb et conciergeries

---

## 💡 Cas d'usage visés

- Locations Airbnb et courte durée
- Conciergeries et gestionnaires de biens
- Hôtels et résidences de tourisme
- À terme : escape games et expériences immersives

---

## 🛠️ Stack

`Python` `LLM` `RAG` `LangChain` `ngrok` `Streamlit`

---

## 📄 Licence

GPL-3.0
