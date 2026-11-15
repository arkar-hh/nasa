import os
import webview

folder = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(folder, "index.html")

webview.create_window("App", html_path, fullscreen=True)
webview.start()