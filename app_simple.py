from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from datetime import datetime
import random
import os

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/v1/predict':
            data = {
                "timestamp": datetime.now().isoformat(),
                "fx_flows_usd": {
                    "USD": 5850000,
                    "MXN": 2340000,
                    "CAD": 1755000
                },
                "arbitrage": "Buy USD, sell MXN"
            }
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())
        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'OK')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    server = HTTPServer(('0.0.0.0', port), Handler)
    server.serve_forever()
