import os
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__)

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
    return render_template('event_admin.html')

@app.route('/event', methods=['POST', 'GET'])
def event():
    if request.method == 'POST':
        flash('New entry was successfully posted')
        flash(request.form['event_name'])
        flash(request.form['event_date_text'])
    else:
        pass
    return redirect(url_for('start'))


if __name__ == '__main__':
    app.run(debug=True)
    app.run('0.0.0.0', 8888)