#!/usr/bin/python3
"""
Task 03 - http.server:
A simple HTTP API server that serves text and JSON responses.
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Request handler for the simple API."""

    def _send_response(self, status_code, body, content_type="text/plain"):
        """Send an HTTP response with headers and a body."""
        self.send_response(status_code)
        self.send_header("Content-Type", content_type)
        self.end_headers()
        if isinstance(body, str):
            body = body.encode("utf-8")
        self.wfile.write(body)

    def do_GET(self):
        """Handle GET requests for different endpoints."""
        if self.path == "/":
            self._send_response(200, "Hello, this is a simple API!")
        elif self.path == "/status":
            self._send_response(200, "OK")
        elif self.path == "/data":
            payload = {"name": "John", "age": 30, "city": "New York"}
            self._send_response(200, json.dumps(payload), "application/json")
        else:
            self._send_response(404, "Endpoint not found")


def run_server(host="0.0.0.0", port=8000):
    """Start the HTTP server."""
    server = HTTPServer((host, port), SimpleAPIHandler)
    print(f"Serving on http://{host}:{port}")
    server.serve_forever()


if __name__ == "__main__":
    run_server()
