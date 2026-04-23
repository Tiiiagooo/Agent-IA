import os
import json
from datetime import datetime


def enregistrer_log(numero, message_in, message_out, current_state):
    """1 fichier log + 1 fichier JSON client"""

    now = datetime.now()
    date_du_jour = now.strftime("%Y-%m-%d")
    heure_actuelle = now.strftime("%H:%M:%S")

    # Nettoyage du numéro
    clean_num = numero.replace('whatsapp:', '').replace('+', '')

    # =========================
    # 📁 DOSSIERS
    # =========================
    log_dir = "log"
    data_dir = "clients"

    os.makedirs(log_dir, exist_ok=True)
    os.makedirs(data_dir, exist_ok=True)

    # =========================
    # 📄 FICHIER LOG TEXTE
    # =========================
    log_filename = f"log_{clean_num}_{date_du_jour}.txt"
    log_path = os.path.join(log_dir, log_filename)

    with open(log_path, "a", encoding="utf-8") as f:
        f.write(f"[{heure_actuelle}] CLIENT: {message_in}\n")
        f.write(f"[{heure_actuelle}] AGENT : {message_out}\n")
        f.write("-" * 30 + "\n")

    # =========================
    # 📊 FICHIER JSON CLIENT
    # =========================
    json_filename = f"client_{clean_num}.json"
    json_path = os.path.join(data_dir, json_filename)

    # Si le fichier existe → on le charge
    if os.path.exists(json_path):
        with open(json_path, "r", encoding="utf-8") as f:
            client_data = json.load(f)
    else:
        # Sinon on initialise
        client_data = {
            "numero": clean_num,
            "date_creation": date_du_jour,
            "historique": [],
            "current_state": None,
            "last_interaction": None
        }

    # =========================
    # 🧠 MISE À JOUR DES DONNÉES
    # =========================
    client_data["historique"].append({
        "timestamp": now.isoformat(),
        "message_client": message_in,
        "message_agent": message_out
    })

    client_data["current_state"] = current_state
    client_data["last_interaction"] = now.isoformat()

    # =========================
    # 💾 SAUVEGARDE JSON
    # =========================
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(client_data, f, indent=4, ensure_ascii=False)