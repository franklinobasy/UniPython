''' process_request.py
This module helps to extract useful parts from JsonObject
'''

from .json_to_object import JsonObject

def get_chat_info(message: JsonObject) -> dict:
        message_info = {}
        message_info['text'] = message.text
        message_info['chat_id'] = message.chat.id
        message_info['user_id'] = message.from_.id
        message_info['username'] = message.from_.username
        message_info['first_name'] = message.from_.first_name

        return message_info


def log_user_info(chat_info: dict) -> None:
        user_id = str(chat_info["user_id"])
        user_name = chat_info["username"]
        first_name = chat_info["first_name"] + "\n"

        user_log = load_user_log()
        write_user_log([user_id, user_name, first_name], user_log)


def load_user_log() -> list:
        try:
                with open("users.csv", "r") as f:
                        user_log = f.readlines()
        except FileNotFoundError:
                with open("users.csv", "w") as f:
                        user_log = ["id", "username", "firstname\n"]
                        f.write(",".join(user_log))
        return user_log

def write_user_log(user_info: list, user_log: list):
        if user_info in user_log:
                pass
        else:
                user_log.append(user_info)
                with open("users.csv", "w") as f:
                        for line in user_log:
                                line = ",".join(line)
                                f.write(line)
                print("new user logged!")


