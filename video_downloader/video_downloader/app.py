from flask import Flask, request, send_file, render_template, jsonify
from yt_dlp import YoutubeDL
import os
import uuid
import glob

app = Flask(__name__)

DOWNLOAD_DIR = 'downloads'
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_video():
    url = request.json.get('url')
    if not url:
        return jsonify({'error': 'No URL provided'}), 400

    try:
        # Generate a unique filename prefix
        unique_id = str(uuid.uuid4())
        output_template = f'{DOWNLOAD_DIR}/{unique_id}.%(ext)s'

        ydl_opts = {
            'format': 'best',
            'outtmpl': output_template,
            'quiet': True,
            'noplaylist': True,
        }

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
        
        # Find the actual file (with whatever extension)
        matching_files = glob.glob(f'{DOWNLOAD_DIR}/{unique_id}.*')
        if not matching_files:
            return jsonify({'error': 'Downloaded file not found'}), 500

        downloaded_file = matching_files[0]
        return send_file(downloaded_file, as_attachment=True)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
