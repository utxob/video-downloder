from flask import Flask, request, render_template, send_file
import yt_dlp
import os
import uuid

app = Flask(__name__)

DOWNLOAD_FOLDER = "downloads"
COOKIES_FILE = "cookies/cookies.txt"  # কুকি ফাইল লোকেশন

if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

def fix_shorts_url(url):
    if 'youtube.com/shorts/' in url:
        video_id = url.split('/')[-1].split('?')[0]
        return f'https://www.youtube.com/watch?v={video_id}'
    return url

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    resolution = request.form['resolution']
    url = fix_shorts_url(url)

    unique_id = str(uuid.uuid4())
    output_template = os.path.join(DOWNLOAD_FOLDER, f'{unique_id}.%(ext)s')

    if resolution != 'best' and resolution.endswith('p'):
        height = resolution.replace('p', '')
        fmt = f'bestvideo[height<={height}]+bestaudio/best'
    else:
        fmt = 'best'

    ydl_opts = {
        'outtmpl': output_template,
        'format': fmt,
        'merge_output_format': 'mp4',
        'quiet': True,
        'cookiefile': COOKIES_FILE  # ✅ সঠিক কী
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            ext = info.get('ext', 'mp4')
            final_file = filename.replace(f".{ext}", ".mp4")
            return send_file(final_file, as_attachment=True)
    except Exception as e:
        return f"<h3>❌ Download failed: {str(e)}</h3><a href='/'>Go Back</a>"

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
