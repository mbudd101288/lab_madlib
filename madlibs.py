"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]


@app.route("/")
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route("/greet")
def greet_person():
    """Greet user, ask if they want to play"""

    player = request.args.get("person")
    # "person" is the name="person" input from the hello.html. person is the key and player is the value

    return render_template("madlib_game.html", person=player)
    # in template madlib_game.html we will use {{person}} key to call the value player(player's submitted name)


@app.route("/game")
# decorator/route requested in madlib_game.html
def show_madlib_form():
    """Get user's reponse of if they want to play game, if yes then play, if no goodbye"""

    play = request.args.get("play")
    # value = request.args.get(key) "play" comes 
    # from the name or id in the madlib_game html form that was submitted"

    if play == "yes":
        return render_template("game.html")
        # will go to game.html to play
    else:
        return render_template("goodbye.html")
        # will go to goodbye.html to quit (how do you say bye using the players name?)


@app.route("/madlib")
# decorator route requested in game.html
def show_madlib():
    # below you are using info from game.html to create key:value with "person" being the name="person" 
    # in the form input and the value being the information the person put in
    person = request.args.get("person")
    noun = request.args.get("noun")
    color = request.args.get("color")
    adj = request.args.get("adj")
    return render_template("madlib.html", person=person, noun=noun, color=color, adj=adj)
    # keys will be put into madlib.html and associated value will be displayed


if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
