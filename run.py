# First in terminal: 'pip3 install Flask'


import os
from flask import Flask, render_template 
                  # we're importing our Flask class.
                         # we're importing the render_template() function from Flask


app = Flask(__name__)
"""
We're then creating an instance of this and storing it in a variable called 'app'.
The first argument of the Flask class, is the name of the application's module - our package.
Since we're just using a single module, we can use __name__ which is a built-in Python variable.
Flask needs this so that it knows where to look for templates and static files.
"""


@app.route("/")
def index():
    return render_template("index.html")
"""
We're then using the app.route decorator.
In Python, a decorator starts with the @ symbol, which is also called pie-notation.
Effectively, a decorator is a way of wrapping functions.

When we try to browse to the root directory, as indicated by the "/", 
then Flask triggers the index function underneath and returns the "Hello, World" text.

Instead of returning text, we return render_template("index.html"). 
Flask expects it to be a directory called templates with an 's',
which should be at the same level as our run.py file.

The root decorator binds the index() function to itself, 
so that whenever that root is called, the function is called.
This function is also called a 'view'.
"""


@app.route("/about")
def about():
    return render_template("about.html", page_title="About")
"""
We added in an additional argument.
I will just call that argument 'page_title'.
You can call this anything you want, it's not specific to the framework.
It's just a variable name that I've made up, but could've been called almost anything else,
except for one of the pre-defined Python variables.

To use this new variable, let's go to the about.html file, and remove the text between
the <h2> tags at the top.
I will replace that text with: {{ page_title }}
Remember, double curly brackets is an expression that's going to display something on the page.
"""


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


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
