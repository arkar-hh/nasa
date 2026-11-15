import ui
import os

folder = os.path.dirname(os.path.abspath(__file__))

html_path = os.path.join(folder, "index.html")

webview = ui.WebView()
webview.present("fullscreen")

webview.load_url("file://" + html_path)
