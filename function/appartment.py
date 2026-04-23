import os
import json
from supabase import create_client
from dotenv import load_dotenv



def update_data_appartment(id_appartment):

    with open("token/token_supabase.txt", "r") as f:
        key = f.read()

    load_dotenv()

    url = "https://llrscaqomkhqropusqqb.supabase.co"

    supabase = create_client(url, key)

    response = supabase.table("apartments").select("*").execute()

    data = [data for data in response.data if data["id"] == id_appartment]
    data_to_save = ["name", "address", "capacity", "description", "price_per_night_weekday","price_per_night_weekend",
                    "wifi_name","wifi_password","housing_type","floor_number","room_count","distribution","access_type",
                    "default_check_in_time","default_check_out_time", "amenities","cleaning_fee"]
    data = data[0]


    # appart_data = {k: data[k] for k in set(wanted_keys) & set(old_dict.keys())}
    appart_data = {key: data[key] for key in data_to_save}
    with open("data/real_appart_data.json", "w") as f:
        json.dump(appart_data, f, indent=3)
    print("Data updated !")
    return None