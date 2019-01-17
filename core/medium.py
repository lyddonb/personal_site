import json
import logging
import requests


# TOOD: Handle auto retries with backoff, etc


BASE_URL = "https://medium.com/@{}/latest?format=json"
KEY = "</x>"


def get_feed(user):
    try:
        response = requests.get(BASE_URL.format(user))
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        # NOTE: This is generally bad. I should handle this better.
        logging.exception(e)
        return

    return response.text


def parse_feed(feed):
    try:
        index = feed.index(KEY)
    except ValueError:
        # NOTE: This is generally bad. I should handle this better.
        logging.exception("Unable to find key: {} in feed.".format(KEY))
        return

    return json.loads(feed[index + 4:])
