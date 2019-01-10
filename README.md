Personal Site
=============

My personal website.

This is a basic Google App Engine, Python 3 site. At the moment there are no dependencies on other services as this is a static site that pulls some content (podcast, old blog posts) from 3rd party services.


## Environment

### Installation

I recommend setting up a Python virtual environment. I use [Virtualenv](https://virtualenv.pypa.io/en/latest/). If you're only using Python 3 on your system then you can probably just move on to the standard library supported [venv](https://docs.python.org/3/library/venv.html).

Then get a virtual envrionment set up based on their instructions with a python 3 dependency. You should also ensure that you have [pip](https://pypi.org/project/pip/) installed.

Once you're good to go we can install our dependencies with:

``` sh
$ pip install -r requirements.txt
```

This will install the dependencies into the virtualenv site-packages. And that's all we need to do to give this a go.

### Running locally

Running locally is quite simple:

``` 
$ python main.py
```

### Deploying

To deploy the site make sure to install the Google [Cloud SDK](https://cloud.google.com/sdk/). Follow the directions there to install the SDK and make sure to set up a Google [Cloud Project](https://cloud.google.com/resource-manager/docs/creating-managing-projects) and authenticate the SDK against that project. You can use Google's [quick start documentation](https://cloud.google.com/appengine/docs/standard/python3/quickstart) to get everything set up in a way that will work here.

Once the SDK is installed and your project is setup then run:

``` sh
$ gcloud app deploy
```

That's it. My site up and running. I have no clue why you would want to run my site. Unless you're future Beau and you've forgot. Which is the reason I do this :).


## Reference Material

Material for the site and potential future features.

### Design
https://css-tricks.com
https://feathericons.com/
https://tailwindcss.com
https://citizennet.github.io

### Blog
https://github.com/gouthambs/Flask-Blogging
http://charlesleifer.com/blog/how-to-make-a-flask-blog-in-one-hour-or-less/
