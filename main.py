from function.utils import request, Flask, Client, joblib, os
from function.reply import whatsapp_logic2, envoyer_message_direct
from function.train import train_model_if_needed
from function.appartment import update_data_appartment

app = Flask(__name__)

with open("token/account_sid.txt", "r") as f:
    account_sid = f.read().strip()
with open("token/auth_token.txt", "r") as f:
    auth_token = f.read().strip()

# Tes identifiants Twilio (à copier depuis ta console Twilio)
client = Client(account_sid, auth_token)


user_states = {
    "statut" : "INIT",
    "prenom" : "Gabrielle", 
    "reservation_info" : "Pas de réservation", 
    "statut_paiement": "En attente",
    "date_arrivee": "Non défini"
} # Mémoire temporaire : { '+336...': 'sujet' }

# AUTO TRAIN / LOAD MODEL
train_model_if_needed()

# Mise à jour info appartement
id_appartment = 'da00ace5-7e20-4e7a-b69b-8755e69401e4'
update_data_appartment(id_appartment)

@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    user_number = request.values.get('From', '')
    user_msg = request.values.get('Body', '').lower()
    return whatsapp_logic2(user_number, user_msg, user_states)

if __name__ == "__main__":
    # EXEMPLE : Envoyer un message dès que le script démarre
    # Remplace par ton numéro au format +336...
    texte = (
        "Bonjour ! En quoi puis-je me rendre utile ?"
    )
    #33612531045
    #33699842167
    envoyer_message_direct('+33612531045',texte ,client)
    
    app.run(port=5000)