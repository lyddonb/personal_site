from flask import Flask
from flask import request
from flask import render_template

from core import podcasts as pc
from core.feed import recent_items
from core.videos import get_videos
from core.writing import get_medium_posts
from core.writing import get_rk_posts


app = Flask(__name__)

# TODO: Pull from config
app.secret_key = b'mysecret'


MENU = (
    ("/", "home-link", "home"),
    ("/about", "process-link", "about"),
    ("/writing", "writing-link", "writing"),
    ("/videos", "videos-link", "videos"),
    ("/podcasts", "podcasts-link", "podcasts"),
    ("/contact", "contact-link", "contact"),
)


@app.route('/', methods=['GET'])
def index():
    return _simple('index.html', recent_items=recent_items())


@app.route('/about', methods=['GET'])
def about():
    return _simple('about.html')


@app.route('/podcasts', methods=['GET'])
def podcasts():
    ttm = pc.get_podcast(pc.TTM_FEED)
    ttm.items = pc.filter_to_last_n_items(ttm.items)

    return _simple('podcasts.html', ttm=ttm)


@app.route('/videos', methods=['GET'])
def videos():
    return _simple('videos.html', videos=get_videos())


@app.route('/contact', methods=['GET'])
def contact():
    return _simple('contact.html')


@app.route('/writing', methods=['GET'])
def writing():
    return _simple('writing.html', posts=get_medium_posts(),
                   rkposts=get_rk_posts())


def _simple(page, **kwargs):
    if not kwargs:
        kwargs = {}

    kwargs["menu"] = _menu_items(active=request.path)

    return render_template(page, **kwargs)


def _menu_items(active="home"):
    items = []
    for item in MENU:
        url = item[0]
        items.append((url, item[1], item[2], active == url))

    return items


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
