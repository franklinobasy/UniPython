''' process_request.py
This module helps to extract useful parts from JsonObject
'''

from .json_to_object import JsonObject

import os



def get_chat_info(message: JsonObject) -> dict:
        message_info = {}
        message_info['text'] = message.text
        message_info['chat_id'] = message.chat.id
        message_info['user_id'] = message.from_.id
        if 'username' in message.from_.get_attr():
                message_info['username'] = message.from_.username
        else:
                message_info['username'] = ""

        message_info['first_name'] = message.from_.first_name

        return message_info


def log_user_info(chat_info: dict) -> None:
        user_id = str(chat_info["user_id"])
        user_name = chat_info["username"]
        first_name = chat_info["first_name"] + "\n"

        user_log = load_user_log()
        write_user_log([user_id, user_name, first_name], user_log)


def load_user_log(path="logs/users.csv") -> list:
        try:
                with open(path, "r") as f:
                        user_log = f.readlines()
        except FileNotFoundError:
                with open(path, "w") as f:
                        header = ["id", "username", "firstname\n"]
                        f.write(",".join(header))

                with open(path, "r") as f:
                        user_log = f.readlines()
        return user_log

def write_user_log(user_info: list, user_log: list, path="logs/users.csv"):
        user_info = ",".join(user_info)
        if user_info in user_log:
                pass
        else:
                with open(path, "a") as f:
                        f.write(user_info)
                print("new user logged!")

def delete_user_log(path="logs/users.csv"):
        if os.path.isfile(path):
                with open(path, "w") as f:
                        f.write("id,username,firstname\n")
                return True
        return False

