import json
import joblib
from datetime import datetime
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client # On ajoute le Client pour l'envoi
from function.savelog import enregistrer_log


# --- VOTRE BASE DE DONNÉES DES INTENTIONS ---
with open(f"data/INTENT.json", "r", encoding="utf-8") as f:
    INTENTS = json.load(f)
