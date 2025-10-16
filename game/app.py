from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    computer = ""
    player = ""

    if request.method == "POST":
        options = ["rock", "paper", "scissors"]
        player = request.form["choice"]
        computer = random.choice(options)

        if player == computer:
            result = "It's a tie!"
        elif (player == "rock" and computer == "scissors") or \
             (player == "paper" and computer == "rock") or \
             (player == "scissors" and computer == "paper"):
            result = "You win!"
        else:
            result = "You lose!"

    return render_template("app-index.html", result=result, player=player, computer=computer)

if __name__ == "__main__":
    app.run(debug=True)
