import webview
import sys
import tkinter as tk
from tkinter import messagebox

def show_error(title, message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror(title, message)
    root.destroy()

def on_loaded():
    webview.active_window().evaluate_js(
        """
        window.alert = function(msg) {
            window.pywebview.api.handle_error(msg);
        };
        """
    )

class API:
    def handle_error(self, msg):
        show_error("Access Denied", msg)

def run_terminal():
    URL = 'https://darkfox-dashboard-production.up.railway.app/'
    TITLE = 'DARKFOX CO. | INTERNAL SYSTEM'
    api = API()
    
    try:
        window = webview.create_window(
            title=TITLE,
            url=URL,
            width=1200,
            height=900,
            resizable=True,
            background_color='#000000',
            js_api=api
        )
        webview.start(on_loaded, gui='mshtml', debug=False)
    except Exception as e:
        show_error("System Error", f"Critical failure: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    run_terminal()
