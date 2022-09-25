# app

from flask import Flask, request, send_from_directory, send_file, jsonify

import os

import requests

from unipython.config import get_configuration
from unipython.interpreter import exec_
from unipython.json_to_object import JsonObject
from unipython.process_request import get_chat_info, log_user_info, delete_user_log

configuration = get_configuration()

app = Flask(__name__)
app.config["SECRET_KEY"] = configuration.secret_key
app.config["LOGS"] = "./logs/"


token = configuration.token
host_url = configuration.host_url


@app.route("/get-me")
def get_me():

    headers = {
        "accept": "application/json",
        "User-Agent": "Telegram Bot SDK - (https://github.com/irazasyed/telegram-bot-sdk)"
    }

    response = requests.post(f"https://api.telegram.org/bot{token}/getMe", headers=headers)

    return response.json()



@app.route(f"/{token}", methods=["GET", "POST"])
def get_update():
    if request.method == "POST":
        response = JsonObject(dict(request.get_json()))
        attr = response.get_attr()
        if "message" in attr.keys():
            chat_info = get_chat_info(response.message)
        elif "edited_message" in attr.keys():
            chat_info = get_chat_info(response.edited_message)
        else:
            return "unknown"

        log_user_info(chat_info)

        text = chat_info.get("text")    
        chat_id = chat_info.get("chat_id")

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

@app.route("/setwebhook/", methods=["GET", "POST"])
def webhook():
    payload = {
        "url": f"{host_url}/{token}"
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

@app.route("/download/<users>", methods=["GET", "POST"])
def download_user(users):
    try:
        return send_file(f"logs/{users}.csv", as_attachment=True)
    except:
        return "404"

@app.route("/delete/<filename>", methods=["GET", "POST"])
def delete_file(filename):
    file = f"{filename}.csv"
    if delete_user_log(path=f"logs/{file}"):
        return jsonify({"result":True})

    return jsonify({"result":False})

if __name__ == "__main__":
    app.run(debug=True)