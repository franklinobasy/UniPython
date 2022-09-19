from flask import Flask, request
import requests

from unipython.config import token, url
from unipython.interpreter import exec_
from unipython.json_to_object import JsonObject

app = Flask(__name__)



@app.route(f"/{token}", methods=["GET", "POST"])
def get_update():
    if request.method == "POST":
        response = JsonObject(request.get_json())
        text = response.message.text
        chat_id = response.message.chat.id
        user_id  = response.message.from_.id

        if text == "/start":
            reply = {
                    "chat_id" : chat_id,
                    "text" : "Welcome 👋\n\nThis bot will help you run python codes.\nEnjoy 🎉🎈"
                }

            requests.post(f"https://api.telegram.org/bot{token}/sendMessage", params=reply)
            return "Ok"
        elif text == "/help":
            reply = {
                    "chat_id" : chat_id,
                    "text" : "Type python codes/commands and press enter when done.🤪"
                }
            requests.post(f"https://api.telegram.org/bot{token}/sendMessage", params=reply)
            return "Ok"
        else:
            reply = {
                    "chat_id" : chat_id,
                    "text" : exec_(text)
                }
            requests.post(f"https://api.telegram.org/bot{token}/sendMessage", params=reply)
            return "Ok"

@app.route("/setwebhook/")
def webhook():
    payload = {
        "url": f"{url}/{token}"
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    response = requests.post(f"https://api.telegram.org/bot{token}/setWebhook", json=payload, headers=headers)
    response = response.json()
    if response["ok"]:
        return "ok"
    return response['error_code']



if __name__ == "__main__":
    app.run(debug=True)