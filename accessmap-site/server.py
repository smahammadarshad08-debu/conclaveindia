import os
import sys
import http.server
import socketserver

PORT = int(os.environ.get("PORT", 10000))
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Determine directory to serve
if os.path.exists(os.path.join(BASE_DIR, "index.html")):
    WEB_DIR = BASE_DIR
elif os.path.exists(os.path.join(BASE_DIR, "accessmap-site", "index.html")):
    WEB_DIR = os.path.join(BASE_DIR, "accessmap-site")
else:
    WEB_DIR = BASE_DIR

class AccessMapHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=WEB_DIR, **kwargs)

    def end_headers(self):
        # Enable CORS and disable aggressive caching for development
        self.send_header("Access-Control-Allow-Origin", "*")
        super().end_headers()

if __name__ == "__main__":
    print(f"==================================================")
    print(f" AccessMap Production Server running on port {PORT}")
    print(f" Serving files from: {WEB_DIR}")
    print(f"==================================================")
    with socketserver.TCPServer(("", PORT), AccessMapHandler) as httpd:
        httpd.serve_forever()
