from flask import Flask, render_template, request, redirect, url_for
from pytube import YouTube

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('yt.html')


@app.route('/download', methods=['POST'])
def download():
    # Get the video URL from the form
    url = request.form['url']

    # Create a YouTube object
    youtube = YouTube(url)

    # Get the highest resolution video stream
    stream = youtube.streams.get_highest_resolution()

    # Download the video
    stream.download()

    # Redirect back to the home page
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
