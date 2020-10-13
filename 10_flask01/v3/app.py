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


app.debug = True
app.run()

# Difference: added line 14 app.debug = True
# Prediction: print how the file is running step by step to the terminal
# What happened: debug mode allows code changes to appear everytime you refresh the page
