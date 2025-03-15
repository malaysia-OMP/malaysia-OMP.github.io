import os
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
REPO_OWNER = "malaysia-OMP"
REPO_NAME = "malaysia-OMP.github.io"

if not BOT_TOKEN:
    print("❌ ERROR: BOT_TOKEN is not set!")
    exit(1)

def create_pull_request():
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/pulls"
    headers = {
        "Authorization": f"token {BOT_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    payload = {
        "title": "Test PR",
        "body": "This is a test PR from the bot.",
        "head": "submissions",
        "base": "main"
    }

    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 401:
        print("❌ ERROR: Unauthorized (Check BOT_TOKEN permissions!)")
    else:
        print(response.json())

create_pull_request()
