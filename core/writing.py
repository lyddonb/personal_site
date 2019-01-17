from datetime import datetime
from time import mktime

import feedparser

from core import medium


IMG_BASE = "https://cdn-images-1.medium.com/max/800/"
PERSONAL = "lyddonb"
RK = "beau.lyddon"


try:
    import ssl
    if hasattr(ssl, '_create_unverified_context'):
        ssl._create_default_https_context = ssl._create_unverified_context
except:
    pass


class Post():
    """ This is an object to hold the basic data pulled from a medium feed.
    Ideally it will be filled by the JSON feed which has all the data we need.
    If we fallback to RSS we lose some data like the image and subtitle.
    """

    def __init__(self, id, title, first_published, last_published, word_count,
                 reading_time, subtitle, img_id, tags):
        self.id = id
        self.title = title
        self.first_published = first_published
        self.last_published = last_published
        self.word_count = word_count
        self.reading_time = reading_time
        self.subtitle = subtitle
        self.img_id = img_id
        self.tags = tags


RK_POSTS = [
    {"title": "Stop Wasting Your Beer Money",
     "link": "https://blog.realkinetic.com/stop-wasting-your-beer-money-12c3fe5e4d54",
     "img": "beermoney.jpeg",
     "alt": "beermoney",
     "snippet": "Why are engineers so bad at paying other engineers for their work? If we can afford spending $50 on pizza and beer for a late night of coding, then we can afford spending $50 a month for a logging service. Yet something is keeping us from just paying for that service. I believe it starts with us consistently undervaluing our own time, which leads to us undervaluing other engineers’ time."
     },
    {"title": "What Is the Customer Impact?",
     "link": "https://blog.realkinetic.com/what-is-the-customer-impact-ce7bceb20a6d",
     "img": "impact.jpg",
     "alt": "impact",
     "snippet": "Failure is inevitable, my goal is keep customer impact costs as close to zero as possible. This means building a fault tolerant environment. Fault tolerance is different from failure avoidance: total avoidance isn’t actually possible."
     },
    {"title": "Load Testing with Locust (Part 1)",
     "link": "https://blog.realkinetic.com/load-testing-with-locust-part-1-174040afdf23",
     "img": "loadtest1.png",
     "alt": "loadtest1",
     "snippet": "Load testing allows us to create artificial usage of our system that mimics real usage. To do this correctly, we want to use our existing APIs in the same manner that our clients do. This means using production logs to build realistic usage patterns. If we have not yet released our system we could analyze traffic to our test instances, demos or betas. Existing tools like Locust allow us to more easily create these test scenarios."
     },
    {"title": "Load Testing with Locust (Part 2)",
     "link": "https://blog.realkinetic.com/load-testing-with-locust-part-2-5f5abd8dbce4",
     "img": "kubernetes.png",
     "alt": "loadtest2",
     "snippet": "In Part 1 we walked through setting up Locust. We ran a single instance locally and then we deployed it as a single node to Google Container Engine (GKE). In this post, we’re going leverage GKE (and Kubernetes) to deploy and run Locust in distributed mode."
     },
    {"title": "My Journey",
     "link": "https://blog.realkinetic.com/my-journey-708884635be7",
     "img": "myjourney.jpeg",
     "alt": "myjourney",
     "snippet": "Understanding the full picture, from business to infrastructure, allowed my career to accelerate at an unbelievable rate. I took the same principles I was applying at the code level and applied them to entire areas of the business, to customers usage of our software, to the sales process, to team management, to code, to delivery. I wanted to understand the entire process end-to-end and the relationships between each subprocess. This gave me a better overall view. It allowed me to communicate empathetically with all stakeholders."
     }
]


def get_medium_latest():
    feed = medium.get_feed(PERSONAL)

    if not feed:
        return _make_posts_from_xml(get_medium_posts())

    parsed = medium.parse_feed(feed)

    if not parsed:
        return _make_posts_from_xml(get_medium_posts())

    return _make_posts_from_json(parsed)


def get_rk_posts():
    return RK_POSTS


def get_medium_posts():
    return _get_medium_posts(PERSONAL)


def get_old_medium_posts():
    return _get_medium_posts(RK)


def _get_medium_posts(user):
    url = "https://medium.com/feed/@{}".format(user)
    f = feedparser.parse(url)
    return f.entries


def _from_timestamp(pub):
    return datetime.fromtimestamp(pub / 1000) if pub else None


def _make_posts_from_xml(feed):
    result = []
    for item in feed:
        result.append(Post(
            item.id,
            item.title,
            datetime.fromtimestamp(mktime(item.published_parsed)),
            None,
            -1,
            -1,
            "",
            None,
            [t["term"] for t in item.tags]
        ))

    return result


def _make_posts_from_json(feed):
    posts = feed.get("payload", {}).get("references", {}).get("Post", {})

    result = []
    for pid, post in posts.items():
        virtuals = post.get("virtuals", {})
        tags = virtuals.get("tags", [])
        first_pub = post["firstPublishedAt"]
        latest_pub = post["latestPublishedAt"]

        result.append(Post(
            pid,
            post.get("title"),
            _from_timestamp(first_pub),
            _from_timestamp(latest_pub),
            virtuals.get("wordCount", -1),
            virtuals.get("readingTime", -1),
            virtuals.get("subtitle", ""),
            virtuals.get("previewImage", {}).get("imageId"),
            [t["name"] for t in tags if t]
        ))

    return result



