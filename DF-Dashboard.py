import webview
import sys

def start_app():
    # SETTINGS
    URL = 'https://dein-projekt.railway.app' 
    TITLE = 'DARKFOX CO. | MEMBER DASHBOARD'
   
    window = webview.create_window(
        title=TITLE,
        url=URL,
        width=1100,
        height=850,
        resizable=True,
        min_size=(800, 600),
        background_color='#000000',
        text_select=False 
    )
  
    webview.start(gui='mshtml', debug=False)

if __name__ == '__main__':
    try:
        start_app()
    except Exception as e:
        print(f"Terminal Error: {e}")
        sys.exit(1)
