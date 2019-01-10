import datetime

VIDEOS = [
    {
        'url': "https://www.youtube.com/watch?v=CD5zTkipGqU",
        'title': "Don't Worry About Monads",
        'location': "LambdaConf",
        'date': datetime.date(2018, 6, 2),
        'snippet': "Many of us have struggled to pick up functional languages. We've been scared off by the terminology: monads, monoids, functors. My goal is to show those afraid to jump in that there is room in the functional world for all of us, no matter your background or skills. I will show how you can not only learn functional languages without understanding those scary terms but that you can even ship production code.",
        'photo': "beau_monads.png",
        'photo_alt': "LambdaConf",
        'modified': datetime.datetime(2019, 1, 6, 1, 46)
    },
    {
        'url': "https://www.youtube.com/watch?v=xy3w2hGijhE",
        'title': "What is Happening?: Attempting to Understand Our Systems",
        'location': "DevOpsDays Des Moines",
        'date': datetime.date(2018, 4, 20),
        'snippet': "Our systems are growing, not only in size but also in complexity. There are more and more relationships between systems, often via fragile network connections. We’re increasingly integrating with systems outside of our control. Not only that, but these systems are more dynamic. While we increase expectations of uptime, we’ve also continued to increase the communication entropy in the system. Many systems now change by the hour. And this only captures a portion of the complexity. A question keeps getting asked that we struggle to answer: what is happening?",
        'photo': "beau_what_is_happening.png",
        'photo_alt': "DevOpsDays",
        'modified': datetime.datetime(2019, 1, 6, 1, 42)
    },
    {
        'url': "https://www.youtube.com/watch?v=AQB9eECueSI",
        'title': "Asset Management in Python (with Robert Kluin)",
        'location': "PyCon - Santa Clara",
        'date': datetime.date(2013, 3, 19),
        'snippet': "With the growth of Coffeescript, Less, SASS, etc..., compiling the assets for your project is becoming more useful. This talk covers using a Python library called Webassets to automate your build process.",
        'photo': "beau_robert_pycon.png",
        'photo_alt': "pycon",
        'modified': datetime.datetime(2019, 1, 6, 1, 40)
    }
]


def get_videos():
    return sorted(VIDEOS, key=lambda k: k['date'], reverse=True)
