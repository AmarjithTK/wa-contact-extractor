from flask import Flask, render_template, request
import re



app = Flask(__name__)


# make templates folder and 

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        html_text = request.form['html_text']
        output_file = request.form['output_file']

        # Save the HTML text as a file
        with open('templates/file.html', 'w') as file:
            file.write(html_text)

        # Extract phone numbers from the HTML text
        phone_numbers = extract_phone_numbers(html_text)

        # Generate the output HTML file
        output_html = generate_output_html(phone_numbers)

        # Save the output HTML file
        with open(f'templates/{output_file}.html', 'w') as file:
            file.write(output_html)

        return f"Phone numbers extracted and saved in work_dir/{output_file}.html"

    return render_template('index.html')

def extract_phone_numbers(html_text):
    # Use regular expressions to extract phone numbers from the HTML text
    phone_numbers = re.findall(r'\d{3}-\d{3}-\d{4}', html_text)
    return phone_numbers

def generate_output_html(phone_numbers):
    # Generate the output HTML with the phone numbers in a list format
    output_html = "<ul>"
    for number in phone_numbers:
        output_html += f"<li>{number}</li>"
    output_html += "</ul>"
    return output_html

if __name__ == '__main__':
    app.run()
