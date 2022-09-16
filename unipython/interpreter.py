'''
Interpreter module that contains execution functionalities
'''

from io import StringIO
from contextlib import redirect_stdout

def exec_(text):
    '''Exec function that calls python exec(...)
    '''
    f = StringIO()
    with redirect_stdout(f):
        try:
            code = compile(text, "output", "exec")
            exec(code)
            output = '''[SUCCESS]>>>\n\n'''
        except SyntaxError as e:
            output = '''[SYNTAX ERROR]>>>\n\n'''
            print(e)
        except Exception as e:
            output = f'''[ERROR:]>>>\n\n'''
            print(e)
   
    output += f.getvalue()
    output += f"\n{'=' * 26}"

    return output
