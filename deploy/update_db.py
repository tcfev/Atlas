from supabase import create_client, Client
import os
import json


url: str = os.getenv("SUPABASE_URL", "")
key: str = os.getenv("SUPABASE_KEY", "")
users_email: str = os.getenv("SUPABASE_USERS_EMAIL", "")
users_password: str = os.getenv("SUPABASE_USERS_PASSWORD", "")


supabase: Client = create_client(url, key)

def reshape_data(entity):
    reshaped_entity = {
        "id": entity.get("id", ""),
        "logo": f"logos/{entity.get("id", "")}.png",
        "pageLink": entity.get("pageLink", ""),
        "mark for edit": "" if not entity.get("mark_for_edit") else entity.get("mark_for_edit"),
        "org_type": entity.get("org_type", ""),
        "name_fa": entity.get("name_fa", ""),
        "name_en": entity.get("name_en", ""),
        "name_short": entity.get("name_short", ""),
        "locations": entity.get("locations", ""),
        "post_location": entity.get("post_location", ""),
        "internet_address": entity.get("internet_address", ""),
        "email": entity.get("email", ""),
        "phone": entity.get("phone", ""),
        "about": entity.get("about", ""),
        "expertise": entity.get("expertise", ""),
        "کنش‌ها": entity.get("کنش\u200cها", ""),
        "history": entity.get("history", ""),
        "manifesto": entity.get("manifesto", ""),
        "coc": entity.get("coc", ""),
        "estimation_of_members": "" if entity.get("estimation_of_members") == -1 else entity.get("estimation_of_members"),
        "برنامه‌ها": entity.get("برنامه\u200cها", ""),
        "موارد دیگر ۱": entity.get("موارد دیگر ۱", ""),
        "موارد دیگر ۲": entity.get("موارد دیگر ۲", ""),
        "political_orientation": entity.get("political_orientation", ""),
        "social_instagram": entity.get("social_instagram", []),
        "social_x": entity.get("social_x", []),
        "social_facebook": entity.get("social_facebook", []),
        "name": entity.get("name", "")
    }
    return reshaped_entity

def main():
    user = supabase.auth.sign_in_with_password({
        "email": users_email, 
        "password": users_password 
    })

    data = supabase.table("Entities").select("*").execute()

    # all data len

    reshaped_data = [reshape_data(entity) for entity in data.data]


    this_file_path = os.path.abspath(__file__)
    this_dir_path = os.path.dirname(this_file_path)
    data_file_path = os.path.join(this_dir_path,'..' , 'static' , 'data', "data.json")

    # Write reshaped data to a json file
    with open(data_file_path, "w", encoding='utf-8') as json_file:
        json.dump(reshaped_data, json_file, ensure_ascii=False, indent=4)
    


    # cancel all threads
    threads = os.sched_getaffinity(0)
    # close 
    os._exit(0)


if __name__ == "__main__":
    main()
