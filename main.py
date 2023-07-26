from flask import Flask, render_template, request,redirect,url_for
import re,os
from flaskwebgui import FlaskUI


from lib.extractor import extract


def fireflask():

    app = Flask(__name__)
    ui = FlaskUI(app=app,server="flask",width=1280,height=720) 


    workdir =  os.getcwd()
# make templates folder and 

# os.makedirs('templates')


    try:
        os.makedirs('blobs', exist_ok=True)
    except Exception:
        pass


    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            html_text = request.form['html_text']
            output_file = request.form['output_file']

            # Save the HTML text as a file
            with open(f'{workdir}/blobs/file.html', 'w',encoding='utf-8') as file:
                file.write(html_text)

            # Extract phone numbers from the HTML text
            phone_numbers = extract(workdir)

            print(f"""{phone_numbers} are these \n""")

            return redirect(url_for('processed', phone_numbers=phone_numbers, output_file=output_file))

        return render_template('index.html')

    @app.route('/processed')
    def processed():
        phone_numbers = request.args.getlist('phone_numbers')
        output_file = request.args.get('output_file')



        print('\n')
        print(phone_numbers)


        # Process the phone numbers and output filename
        # ...

        # Pass the processed data to the template
        return render_template('processed.html', items=phone_numbers,heading=output_file)

        # app.run()
        ui.run()

