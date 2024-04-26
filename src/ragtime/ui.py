"""
Source code: https://github.com/zargit/tkinter-json-editor
"""

import tkinter as tk
from json_editor import JsonEditor

if __name__ == '__main__':
    root = tk.Tk()
    editor = JsonEditor(root)
    editor.set_title('JSON Editor')
    root.mainloop()
    

class UI:

    def __init__(self):
        self.root = tk.Tk()
    
    def json_editor():
        """Launches the JSON editor
        """
        editor = JsonEditor(root)
        editor.set_title('JSON Editor')
        root.mainloop()

# TODO: Code all unit tests for the UI