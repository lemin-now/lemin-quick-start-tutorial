from flask import Flask, request, render_template
import requests

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/validate', methods=['POST'])
def validate():
    data = {'challenge_id': request.form['lemin_challenge_id'],
            'answer': request.form['lemin_answer'],
            'private_key': 'your_private_key'}
    headers = {'Content-Type': 'application/json'}
    r = requests.post('https://api.leminnow.com/captcha/v1/cropped/validate',
                      json=data, headers=headers)

    if r.json()['success']:
        return 'OK'
    else:
        return 'FAIL'
