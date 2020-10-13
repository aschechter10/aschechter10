# Team aaaaaaaaahhhhhhhh 1
# Soft Dev
# K10: Putting little pieces together: creating flask app to display previously created occupation chooser
# 2020-10-13

# Import the neccesary modules
from flask import Flask
import csv
import random

dic = {}  # Initializes the dictionary for jobs and percentages

with open('occupy_flask_st/occupations.csv', 'r') as csv_file:  # opens the file
    # Uses the DictReader class to read the csv file into a dictionary like data structure
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:  # Loops through each line in the csv file
        # DictReader assigns each column a title based on the first row of the csv file.
        job_name = row['Job Class']
        # 'Job Class' for the title of each job and 'Percentage' for the percentage.
        if job_name == 'Total':  # Don't want to take the last line
            break
        # 'Percentage' is the second column
        percentage = float(row['Percentage'])
        # adding the names and percentages to our dictionary
        dic[job_name] = percentage

app = Flask(__name__)  # create instance of class Flask


@app.route("/")  # assign fxn to route
def random_occupation():
    # contains what will be printed on the web page
    return_string = "Team ahhhhhhh 1<br><br>"
    # gets a random value from 0 to 100, includes decimals.
    num = random.uniform(0, 100)
    chance = 0  # initial min chance
    for occupation in dic:
        chance += dic[occupation]  # Percentage of occupation
        # We add the chance for every occupation to get to the chance we want for the occupations
        # This way each occupation has its own area and all have the correct chance for being chosen.
        # If the num we got lies in the current chance, we got our value.
        if(num <= chance):
            return_string += "<b>Newly selected occupation:</b> " + \
                occupation + "<br><br> <b>List of occupations:</b>"
            # adds randomly selected occupation to return_string
            break

    for key in dic.keys():
        return_string += "<br>" + key  # adds all occupations to return_string

    return return_string


app.debug = True
app.run()
