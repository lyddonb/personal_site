from pyPodcastParser.Podcast import Podcast
import requests


TTM_FEED = "https://www.tiedtomachines.com/feed/podcast"


def get_podcast(feed):
    response = requests.get(feed)
    return Podcast(response.content)


def get_last_n_items(feed, n=10):
    p = get_podcast(feed)

    return filter_to_last_n_items(p.items)


def filter_to_last_n_items(items, n=10):
    items = sorted(items, key=lambda x: x.date_time, reverse=True)

    if len(items) > n:
        items = items[:n]

    return items
