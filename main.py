from flask import Flask, send_from_directory, abort
import os

app = Flask(__name__, static_folder='.', static_url_path='')

# Serve the main page
@app.route('/')
def index():
    return send_from_directory('.', 'for-you.html')

# Serve any other static file in this folder (css, images, js, other html)
@app.route('/<path:filename>')
def static_files(filename):
    # simple safety: only serve files that exist in this directory
    if os.path.isfile(filename):
        return send_from_directory('.', filename)
    abort(404)

if __name__ == '__main__':
    # debug mode for local development; change host/port as needed
    app.run(debug=True, host='127.0.0.1', port=5000)
