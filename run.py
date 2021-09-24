# First in terminal: 'pip3 install Flask'


import os
import json  # now we want Python to import the data. To do that, we first need to import the JSON library, because we're going to be passing the data that's coming in as JSON.
from flask import Flask, render_template, request, flash
                  # we're importing our Flask class.
                         # we're importing the render_template() function from Flask
                                          # Request is going to handle things like finding out what method we used, and it will also contain our form object when we've posted it.
                                                   # 'flashed messages' in Flask
if os.path.exists("env.py"):
    import env # Once we save that, a new directory called 'pycache' is created.


app = Flask(__name__)
"""
We're then creating an instance of this and storing it in a variable called 'app'.
The first argument of the Flask class, is the name of the application's module - our package.
Since we're just using a single module, we can use __name__ which is a built-in Python variable.
Flask needs this so that it knows where to look for templates and static files.
"""
app.secret_key = os.environ.get("SECRET_KEY")


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
    data = [] #  We will initialize an empty array or list called 'data'.
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)
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

We need to have Python open the JSON file in order to read it.
This is called a 'with' block.
with open("data/company.json", "r") as json_data: Python is opening the JSON file as "read-only",
and assigning the contents of the file to a new variable we've created called json_data.
We need to set our empty 'data' list to equal the parsed JSON data that we've sent through.
data = json.load(json_data)

Finally, I will pass that list into my return statement, and call it 'company'.
company=data This is assigning a new variable called 'company'
that will be sent through to the HTML template, which is equal to the list of data it's loading
from the JSON file.
"""


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)
"""
The first argument is going to be our new "member.html" template that we just created.
The second argument will be "member=member".
This first 'member' is the variable name being passed through into our html file.
The second 'member' is the member object we created above on line 24.
"""


@app.route("/contact", methods=["GET", "PORT"])
def contact():
    if request.method == "PORT":
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
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
        port=int(os.environ.get("PORT", "5000")),
        debug=True # You should only have debug=True while testing your application in development mode, but change it to debug=False before you submit your project.
    )
