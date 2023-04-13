import instaloader
from flask import Flask, request, render_template, redirect

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('ig.html')


@app.route('/download', methods=['POST'])
def download_instagram_video():
    # Get the URL from the HTML form
    url = request.form['url']

    # Create an instance of Instaloader class
    loader = instaloader.Instaloader()

    # Retrieve the post object
    post = instaloader.Post.from_shortcode(loader.context, url.split("/")[-2])

    # Download the video
    loader.download_post(post, target="loaderMedia")

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
