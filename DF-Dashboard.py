import webview
import sys
import os
import tkinter as tk
from tkinter import messagebox

def run_darkfox_terminal():
    URL = 'https://darkfox-dashboard-production.up.railway.app/'
    TITLE = 'DF-Dashboard'
    
    try:
        window = webview.create_window(
            title=TITLE,
            url=URL,
            width=1200,
            height=900,
            resizable=True,
            background_color='#000000',
            min_size=(800, 600)
        )
        webview.start(gui='mshtml', debug=False)
    except Exception as e:
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("System Error", f"Connection to DarkFox Terminal failed.\n\nDetails: {str(e)}")
        root.destroy()
        sys.exit(1)

if __name__ == '__main__':
    run_darkfox_terminal()
