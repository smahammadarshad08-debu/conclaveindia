#!/usr/bin/env python3
"""
AccessMap India — Production Web Server for Render & Cloud PaaS
==============================================================
"""

import os
import sys
import signal
import json
import mimetypes
import http.server
import socketserver

PORT = int(os.environ.get("PORT", 10000))
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# If inside accessmap-site or at root
if os.path.exists(os.path.join(BASE_DIR, "index.html")):
    WEB_DIR = BASE_DIR
elif os.path.exists(os.path.join(BASE_DIR, "accessmap-site", "index.html")):
    WEB_DIR = os.path.join(BASE_DIR, "accessmap-site")
else:
    WEB_DIR = BASE_DIR

mimetypes.add_type("application/javascript", ".js")
mimetypes.add_type("text/css", ".css")
mimetypes.add_type("application/json", ".json")
mimetypes.add_type("application/manifest+json", ".webmanifest")
mimetypes.add_type("image/svg+xml", ".svg")
mimetypes.add_type("image/png", ".png")
mimetypes.add_type("image/webp", ".webp")

class AccessMapHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=WEB_DIR, **kwargs)

    def do_GET(self):
        if self.path in ("/healthz", "/health", "/ping"):
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            payload = {
                "status": "healthy",
                "service": "AccessMap India",
                "version": "2.4.0",
                "standards": "MoHUA HG-2021 Compliant",
                "port": PORT
            }
            self.wfile.write(json.dumps(payload).encode("utf-8"))
            return
        super().do_GET()

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, HEAD, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Frame-Options", "SAMEORIGIN")

        if self.path.endswith((".js", ".css", ".svg", ".png", ".webp", ".ico")):
            self.send_header("Cache-Control", "public, max-age=86400")
        elif self.path.endswith(".html") or self.path == "/":
            self.send_header("Cache-Control", "no-cache, must-revalidate")

        super().end_headers()

class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True
    daemon_threads = True

def run():
    print(f"AccessMap server listening on port {PORT} serving {WEB_DIR}")
    server = ThreadingTCPServer(("", PORT), AccessMapHTTPRequestHandler)
    try:
        server.serve_forever()
    except (KeyboardInterrupt, SystemExit):
        pass
    finally:
        server.server_close()

if __name__ == "__main__":
    run()
