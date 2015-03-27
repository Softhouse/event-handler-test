from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('event_admin.html')

if __name__ == '__main__':
    app.run('0.0.0.0', 8888)