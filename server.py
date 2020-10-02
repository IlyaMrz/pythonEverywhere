from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('./index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def savoToTxt(data):
    with open('./database.txt', 'a') as f:
        email = data['email']
        topic = data['subject']
        message = data['message']
        f.write(f'\n{email}, {topic}, {message}')


def savetoCSV(data):
    with open('./database.csv', 'a', newline='') as f2:
        email = data['email']
        topic = data['subject']
        message = data['message']
        csv_writer = csv.writer(
            f2, delimiter=',',
            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, topic, message])
        return print('ok')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            print(data)
            savetoCSV(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database'
    else:
        return 'something else happend'
