import json

def process_json(filename):
   
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{filename}'.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def filter_users_by_language(data, language):
    
    return [user for user in data if user.get('language') == language]



def write_json(data, filename):
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4) 
    except Exception as e:
        print(f"An error occurred while writing to the JSON file: {e}")



json_data = process_json("lab.json")

if json_data:
    filtered_users = filter_users_by_language(json_data, "English")  
    write_json(filtered_users, "out.json")
    print("Filtered users written to out.json")