import http.server
import socketserver
from pathlib import Path

PORT = 8080
DIRECTORY = Path(__file__).resolve().parent

class Handler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        full_path = DIRECTORY / path.lstrip('/')
        if full_path.is_dir():
            index_file = full_path / 'index.html'
            if index_file.exists():
                return str(index_file)
        return str(full_path)

if __name__ == '__main__':
    with socketserver.TCPServer(('', PORT), Handler) as httpd:
        print(f'Serving {DIRECTORY} at http://localhost:{PORT}/ (Ctrl+C to stop)')
        httpd.serve_forever()
