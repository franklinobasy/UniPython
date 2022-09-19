'''
Interpreter module that contains execution functionalities
'''

from contextlib import redirect_stdout
from io import StringIO
import re

from unipython.loader import check_forbidden


def exec_(text):
    '''Exec function that calls python exec(...)
    '''
    forbidden = check_forbidden(text)
    if forbidden:
        output = f'''💀❌ERROR:]>>>\nThe following modules are not allowed 😔.\n'''
        for search in forbidden:
            output += f"{search}❌\n"
        output += f"{'=' * 26}"

    else:
        f = StringIO()
        with redirect_stdout(f):
            try:
                code = compile(text, "output", "exec")
                exec(code)
                output = '''[✅✅SUCCESS]>>>\n\n'''
            except SyntaxError as e:
                output = '''[⚠🛑🚫SYNTAX ERROR]>>>\n\n'''
                print(e)
            except Exception as e:
                output = f'''[🛑🛑ERROR:]>>>\n\n'''
                print(e)
    
        output += f.getvalue()
        output += f"\n{'=' * 26}"

    return output
