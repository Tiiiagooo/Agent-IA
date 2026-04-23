from function.utils import json, MessagingResponse, Client
from function.savelog import enregistrer_log
from function.predict import load_all ,detect_intent
from function.llm import generer_reponse_llm

# --- VOTRE BASE DE DONNÉES DE RÉPONSES ---
with open(f"data/FAQ.json", "r", encoding="utf-8") as f:
    FAQ = json.load(f)

# --- VOTRE BASE DE DONNÉES DES INTENTIONS ---
with open(f"data/real_appart_data.json", "r", encoding="utf-8") as f:
    APPART_DATA = json.load(f)

def envoyer_message_direct(numero_destinataire, texte, client):
    """Fonction pour envoyer un message sans attendre de réponse"""
    message = client.messages.create(
        from_='whatsapp:+14155238886', # Le numéro de la Sandbox
        body=texte,
        to=f'whatsapp:{numero_destinataire}'
    )
    print(f"Message envoyé ! SID: {message.sid}")

def whatsapp_logic(user_number, user_msg, user_states):

    # --- LOG ENTRANT ---
    print(f"\n--- NOUVEAU MESSAGE ---")
    print(f"De: {user_number}")
    print(f"Message: {user_msg}")
    print(f"-----------------------\n")

    resp = MessagingResponse()

    # 1. Vérifier si on connaît déjà l'utilisateur
    current_state = user_states.get(user_number)

    # --- LOGIQUE DE DÉTECTION ---
    model, vectorizer, X, labels = load_all()
    intent, score, methode = detect_intent(user_msg, model, vectorizer, X, labels)

    if methode == "cosine":
        reply = FAQ[intent]

    elif methode == "ml":
        reply = f"Je pense que vous parlez sur le thème '{intent}' voici ma réponse : \n {FAQ[intent]}"

    else:
        reply = (
                "Veuillez m'excuser je n'ai pas totalement compris.\nEn tant que 'Assistant Automatique', je peux aussi répondre aux sujets suivants 🤖 :\n\n"
                "- Les *Prix*\n"
                "- Les *Horaires* (arrivée/départ)\n"
                "- Le *Parking*\n"
                "- L'*Adresse*"
            )
        
    # --- ENREGISTREMENT DU LOG ---
    enregistrer_log(user_number, user_msg, reply, current_state)

    # --- LOG SORTANT ---
    print(f"📤 RÉPONSE du Bot: {reply}")
    print(f"--------------------------------")
    resp.message(reply)
    return str(resp)

def whatsapp_logic2(user_number, user_msg, user_states):

    # --- LOG ENTRANT ---
    print(f"\n--- NOUVEAU MESSAGE ---")
    print(f"De: {user_number}")
    print(f"Message: {user_msg}")
    print(f"-----------------------")
    resp = MessagingResponse()

    current_state = user_states.get("statut")

    # Appel au LLM avec les datas
    reply = generer_reponse_llm(user_msg, APPART_DATA, user_states)

    # --- ENREGISTREMENT DU LOG ---
    enregistrer_log(user_number, user_msg, reply, current_state)

    # --- LOG SORTANT ---
    print(f"📤 RÉPONSE du Bot: {reply}")
    print(f"--------------------------------")
    resp.message(reply)
    return str(resp)
