import csv
import re
from flask import Flask, render_template_string,render_template


heading=input("Enter a heading for your html")

app = Flask(__name__)

# Read the CSV file and extract phone numbers
with open('numbers.csv', 'r') as file:
    reader = csv.reader(file)
    numbers = [row[0].replace(' ', '') for row in reader]
    # Remove duplicates
    # numbers = list(set(numbers))

# Convert phone numbers to an HTML to-do list
# html_list = """

# <head> 
# <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@1/css/pico.min.css">
# <style>

# *{
#     box-sizing: border-box;
#     margin:0;
#     padding:0;
# }

# html{
#     font-size:16px;
# }

# ol{
#     width:90%;
#     font-size: 4rem;
#     margin: 5% auto;
#     text-align:center;
#     padding:2rem;
#     list-style-type: decimal;
# }


# </style>


# </head>
# <h1>Seva List</h1>\n<ol>\n"""
# for number in numbers:
#     html_list += f'<li><input type="checkbox" name="numbers"><a href="tel:{number}">{number}</a></li>\n'


# html_list += '</ol>'

# Render the HTML list using a Flask template
# app.route('/')
# def index():
#     return render_template_string(html_list)@

# print(numbers)

@app.route('/')
def index():
    return render_template('index.html',items=numbers,heading=heading)

if __name__ == '__main__':
    app.run(debug=True)