# First in terminal: 'pip3 install Flask'

import os
from flask import Flask # we're importing our Flask class.


app = Flask(__name__)
"""
We're then creating an instance of this and storing it in a variable called 'app'.
The first argument of the Flask class, is the name of the application's module - our package.
Since we're just using a single module, we can use __name__ which is a built-in Python variable.
Flask needs this so that it knows where to look for templates and static files.
"""


@app.route("/")
def index():
    return "Hello, world!"
"""
We're then using the app.route decorator.
In Python, a decorator starts with the @ symbol, which is also called pie-notation.
Effectively, a decorator is a way of wrapping functions.

When we try to browse to the root directory, as indicated by the "/", 
then Flask triggers the index function underneath and returns the "Hello, World" text.
"""


if __name__ == "__main__": # The word 'main' wrapped in double-underscores (__main__) is the name of the default module in Python.
    """
    If name is equal to "main" (both wrapped in double underscores), then we're going to run our app with the following arguments.

    The 'host' will be set to os.environ.get("IP"), and I will set a default of "0.0.0.0".

    We're using the os module from the standard library to get the 'IP' environment variable if it exists, 
    but set a default value if it's not found.

    It will be the same with 'PORT', but this time, we're casting it as an integer, and I will set that default to "5000", 
    which is a common port used by Flask.

    We also need to specify "debug=True", because that will allow us to debug our code much easier during the development stage.
    """
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("POST", "5000")),
        debug=True # You should only have debug=True while testing your application in development mode, but change it to debug=False before you submit your project.
    )
