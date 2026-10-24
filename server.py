#!/usr/bin/env python3
"""
AccessMap India — Production Web Server for Render & Cloud PaaS
==============================================================
Lightweight, zero-dependency HTTP server tailored for containerized
and serverless cloud hosting environments (Render, Railway, Fly.io, Heroku).
Compliant with standard PORT binding and graceful lifecycle signals.
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

# Resolve directory to serve (prioritize accessmap-site directory)
CANDIDATE_DIR = os.path.join(BASE_DIR, "accessmap-site")
if os.path.exists(os.path.join(CANDIDATE_DIR, "index.html")):
    WEB_DIR = CANDIDATE_DIR
else:
    WEB_DIR = BASE_DIR

# Ensure modern web MIME types are properly registered
mimetypes.add_type("application/javascript", ".js")
mimetypes.add_type("text/css", ".css")
mimetypes.add_type("application/json", ".json")
mimetypes.add_type("application/manifest+json", ".webmanifest")
mimetypes.add_type("image/svg+xml", ".svg")
mimetypes.add_type("image/png", ".png")
mimetypes.add_type("image/webp", ".webp")

class AccessMapHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Production HTTP request handler with health checks, CORS, and caching."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=WEB_DIR, **kwargs)

    def do_GET(self):
        # Health check endpoints for Render zero-downtime deployments
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
        # Security & CORS headers
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, HEAD, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Frame-Options", "SAMEORIGIN")

        # Static assets caching
        if self.path.endswith((".js", ".css", ".svg", ".png", ".webp", ".ico")):
            self.send_header("Cache-Control", "public, max-age=86400")
        elif self.path.endswith(".html") or self.path == "/":
            self.send_header("Cache-Control", "no-cache, must-revalidate")

        super().end_headers()

    def log_message(self, format, *args):
        # Clean production logging
        sys.stdout.write(f"[{self.log_date_time_string()}] {format % args}\n")
        sys.stdout.flush()

class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True
    daemon_threads = True

def run():
    print("==================================================================")
    print("  AccessMap India · Accessible Urban Navigation Web Service")
    print(f"  Target Environment : Render / Production Cloud PaaS")
    print(f"  Listening Port     : {PORT}")
    print(f"  Serving Directory  : {WEB_DIR}")
    print(f"  Health Check       : http://0.0.0.0:{PORT}/healthz")
    print("==================================================================")

    server = ThreadingTCPServer(("", PORT), AccessMapHTTPRequestHandler)

    def shutdown_handler(signum, frame):
        print(f"\n[INFO] Received signal {signum}. Shutting down gracefully...")
        server.shutdown()
        server.server_close()
        sys.exit(0)

    signal.signal(signal.SIGINT, shutdown_handler)
    if hasattr(signal, "SIGTERM"):
        signal.signal(signal.SIGTERM, shutdown_handler)

    try:
        server.serve_forever()
    except (KeyboardInterrupt, SystemExit):
        pass
    finally:
        server.server_close()
        print("[INFO] Server stopped.")

if __name__ == "__main__":
    run()
