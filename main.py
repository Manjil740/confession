from flask import Flask, send_from_directory, abort, request, jsonify
import os
from datetime import datetime

app = Flask(__name__, static_folder='.', static_url_path='')

# Where her answer gets saved
ANSWERS_FILE = 'answers.txt'


# Serve the main page
@app.route('/')
def index():
    return send_from_directory('.', 'main.html')


# Serve any other static file in this folder (css, images, js, other html)
@app.route('/<path:filename>')
def static_files(filename):
    # simple safety: only serve files that exist in this directory
    if os.path.isfile(filename):
        return send_from_directory('.', filename)
    abort(404)


# Save her answer (yes/no) to a text file, along with a timestamp
@app.route('/save-answer', methods=['POST'])
def save_answer():
    data = request.get_json(silent=True) or {}
    answer = data.get('answer', 'unknown')

    # keep only expected values, but don't hard-fail on anything unexpected
    if answer not in ('yes', 'no'):
        answer = str(answer)

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open(ANSWERS_FILE, 'a', encoding='utf-8') as f:
        f.write(f'[{timestamp}] Answer: {answer}\n')

    return jsonify({'status': 'ok'})


if __name__ == '__main__':
    # debug mode for local development; change host/port as needed
    app.run(debug=True, host='127.0.0.1', port=5000)