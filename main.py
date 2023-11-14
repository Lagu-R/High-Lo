# this is my first step to flask ;) higher/lower game .

#import important modules for that proj.
from flask import Flask
import random
# generate number
generated_num = random.randint(0, 9)

app = Flask(__name__)

# first route view
@app.route("/")
def hello_world():
    return  "<h1>Guess a number between 0 and 9</h1>"\
            "<img src='https://media.giphy.com/media/l378khQxt68syiWJy/giphy-downsized-large.gif'>"


# dinamical view for as many option u want :* ;)
@app.route("/<int:number>")
def guess(number):
    if number == generated_num:
        return "<h1 style='color: Yellow;'> You Found me!</h1>"\
            "<img src='https://media.giphy.com/media/mDJD1O0qrbd5659hlh/giphy.gif'>"
    elif number < generated_num:
        return "<h1 style='color: red;'> Too low, lets try again!!!</h1>"\
            "<img src='https://media.giphy.com/media/VlqzeaRnhCvPLfrSh6/giphy.gif'>"
    else:
        return "<h1 style='color: purple;'> Too high, lets try again!!!</h1>"\
            "<img src='https://media.giphy.com/media/YQAuKJ7wf68qBHPw6Y/giphy.gif'>"

# run server until u want ;) refreshe automaticaly...
if __name__ == "__main__":
    app.run(debug=True)
