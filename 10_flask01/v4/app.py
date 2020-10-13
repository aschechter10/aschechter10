# Clyde 'Thluffy' Sinclair
# SoftDev -- Rona Ed.
# Oct 2020

from flask import Flask
app = Flask(__name__)  # create instance of class Flask


@app.route("/")  # assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"


if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()

# Difference: lines 15 and 16 were placed in a if clause used similar to the main method in java
# Prediction: Nothing will change
# What happened: Only prints output of lines 11 and 12 to the terminal when a change is made to the file and it is saved
