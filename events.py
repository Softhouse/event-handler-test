import os
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
import requests, json

app = Flask(__name__)

db_url = 'http://xyz.softhouse.se/api/event'
#db_url = 'http://localhost:3232/event'

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))

@app.route('/')
def start():
    events = requests.get(db_url)
    return render_template('event_admin.html', events=events.json())

@app.route('/show_event ')
def show_event():
    event_name = request.args.get('event')
    event = requests.get(db_url + '/' + event_name)
    return render_template('event_register.html', event=event.json())

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        data = {
            'family_name': request.form['family_name'],
            'first_name': request.form['first_name'],
            'event_id': request.form['event_id']
        }
        requests.post(db_url, data=json.dumps(data), headers={'content-type': 'application/json'})
    else:
	   get_resp = requests.get(db_url)
	   return json.dumps(get_resp.json())
    return redirect(url_for('start'))

@app.route('/event', methods=['POST', 'GET'])
def event():
    if request.method == 'POST':
        data = {
            'event_name': request.form['event_name'],
            'event_date': request.form['event_date_text'],
        }
        result = requests.post(db_url, data=json.dumps(data), headers={'content-type': 'application/json'})
        if result.status_code is requests.codes.ok:
            msg = "Event added"
        else:
            msg = "Something went wrong"
    else:
        pass
    return redirect(url_for(start))


if __name__ == '__main__':
    app.run('0.0.0.0', 8888)
