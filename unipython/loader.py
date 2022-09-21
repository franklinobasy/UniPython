'''
This module contains functionalities for preloading texts for the interpreter.
'''

import re

def check_forbidden(text):
    """
    This function searches for forbidden module import.
    Args:
        text: code to search

    ---
    Forbidden modules could affect the server hosting the application.
    Example os, sys, pathlib ...

    """

    forbidden = re.compile(r"(import|from) (os|sys|pathlib)")

    searches = forbidden.finditer(text)
    searches = list(searches)

    to_return = []

    if not searches:
        return to_return

    else:
        for search in searches:
            to_return.append(search.group(2))
        return to_return


def laod_text(user_id, text):
    '''
    This function loads or creates a special file for a user, using the
    user's chat_id as the name of the file.
    The file contains all the commands history of the user.
    Any time a user sends a command to the bot, the command is appended to this
    file and the whole file is the executed.

    '''
    try:
        with open(f"{user_id}", "r") as f:
            code = f.readlines()
    except FileNotFoundError:
        code = []

    for line in code:
        if line.startswith("print"):
            pass
    
