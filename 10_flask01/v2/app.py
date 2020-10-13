# Clyde 'Thluffy' Sinclair
# SoftDev -- Rona Ed.
# Oct 2020

from flask import Flask
app = Flask(__name__)  # create instance of class Flask


@app.route("/")  # assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)  # where will this go?
    return "No hablo queso!"


app.run()

# Difference: added lines 10 and 11
# Prediction: will print "about to print __name__..." and then "__main__" to the terminal
# What happened: When link is opened, prints output of lines 10,11 to terminal
