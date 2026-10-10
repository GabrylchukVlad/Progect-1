import requests

def run_requests():
    response = requests.get("https://api.github.com")
    print("[Requests] Status code:", response.status_code)
