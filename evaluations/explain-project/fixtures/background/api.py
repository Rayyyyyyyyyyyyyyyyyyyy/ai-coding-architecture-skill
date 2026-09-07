import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import urlparse, parse_qs

from store import initialize, create_order, get_order


def submit_order(data):
    if not isinstance(data, dict) or not data.get('item') or not data.get('email'):
        return 400, {'error': 'item and email are required'}
    return 202, create_order(data['item'], data['email'])


ROUTES = {('POST', '/orders'): submit_order}


class Handler(BaseHTTPRequestHandler):
    def send_json(self, status, data):
        payload = json.dumps(data).encode()
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(payload)

    def do_POST(self):
        handler = ROUTES.get(('POST', urlparse(self.path).path))
        if handler is None:
            return self.send_json(404, {'error': 'not found'})
        try:
            body = json.loads(self.rfile.read(int(self.headers.get('Content-Length', 0))))
        except (ValueError, TypeError):
            return self.send_json(400, {'error': 'invalid JSON'})
        self.send_json(*handler(body))

    def do_GET(self):
        url = urlparse(self.path)
        if url.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(Path(__file__).with_name('index.html').read_bytes())
        elif url.path == '/orders':
            order = get_order(parse_qs(url.query).get('id', [''])[0])
            self.send_json(200 if order else 404, order or {'error': 'not found'})
        else:
            self.send_json(404, {'error': 'not found'})


if __name__ == '__main__':
    initialize()
    HTTPServer(('127.0.0.1', 8080), Handler).serve_forever()
