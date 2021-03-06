import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1' #needed if you're doing this locally, not necessary on website
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1' #needed if you're doing this locally, not necessary on website
#####################
from flask import Flask,redirect,url_for,render_template
from flask_dance.contrib.google import make_google_blueprint,google

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

<<<<<<< HEAD
blueprint = make_google_blueprint(client_id='',client_secret='',offline=True,
=======
blueprint = make_google_blueprint(client_id='1051655849101-atpovvoplsnupqign2gtcsmd1a26prhj.apps.googleusercontent.com',client_secret='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',offline=True,
>>>>>>> fbbc2ffaf69f20e22bba830f07b398f8fff07265
                                    scope=['profile','email'])

app.register_blueprint(blueprint,url_prefix='/login')


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/welcome')
def welcome():
    #return error internal server rorr if not logged in
    resp = google.get('/oauth2/v2/userinfo')
    assert resp.ok, resp.text
    email = resp.json()['email']

    return render_template('welcome.html',email=email)


@app.route('/login/google')
def login():
    if not google.authorized:
        return render_template(url_for('google.login')) #automated call from flask_dance to take you to the automated login screen for google
    resp = google.get('/oauth2/v2/userinfo')
    assert resp.ok, resp.text
    email = resp.json()['email']

    return render_template('welcome.html',email=email)

if __name__ == '__main__':
    app.run()
