from time import mktime
from datetime import datetime

from core import podcasts as pc
from core.videos import get_videos
from core.writing import get_medium_posts
from core.writing import get_old_medium_posts


class KIND:
    PODCAST = "podcast"
    WRITING = "writing"
    VIDEO = "video"

    @staticmethod
    def all():
        return (
            KIND.PODCAST,
            KIND.WRITING,
            KIND.VIDEO
        )


class Item():

    def __init__(self, kind, title, url, snippet, publish_date, img=None):
        self.kind = kind
        self.title = title
        self.url = url
        self.snippet = snippet
        self.publish_date = publish_date
        self.img = img

    @property
    def kind_icon(self):
        if self.kind == KIND.PODCAST:
            return "mic"
        elif self.kind == KIND.WRITING:
            return "edit"
        elif self.kind == KIND.VIDEO:
            return "video"


def recent_items(n=10):
    # We can look into making this async with grequests if this is too slow
    items = from_podcast(pc.get_last_n_items(pc.TTM_FEED, 10))
    items.extend(from_rss(get_medium_posts()))
    items.extend(from_rss(get_old_medium_posts()))
    items.extend(from_video(get_videos()))

    items = sorted(items, key=lambda x: x.publish_date, reverse=True)

    if len(items) > n:
        items = items[:n]

    return items


def from_podcast(items):
    return [Item(KIND.PODCAST, pi.title, pi.enclosure_url, pi.description,
                 pi.date_time)
            for pi in items]


def from_rss(items):
    return [Item(KIND.WRITING, i.title, i.link, i.description,
                 datetime.fromtimestamp(mktime(i.published_parsed)))
            for i in items]


def from_video(items):
    return [Item(KIND.VIDEO, i["title"], i["url"], i["snippet"],
                 datetime.combine(i["date"], datetime.min.time()),
                 img="/static/img/video/thumbs/{}".format(i["photo"]))
            for i in items]
