import json

def run_json():
    data = {"name": "Python", "version": 3}
    json_str = json.dumps(data)
    print("[JSON] Серіалізований рядок:", json_str)
