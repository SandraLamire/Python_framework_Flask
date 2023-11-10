from flask import Flask, render_template, request

app = Flask(__name__)


# http://127.0.0.1:5000/welcome/Sandra
@app.route('/welcome/<name>')
def welcome(name):
    return f"<p><i>Bienvenue ici {name} !</i></p>"


# http://127.0.0.1:5000
@app.route('/')
def index():
    return render_template("index.html")


@app.route("/form")
def form():
    return render_template("form.html")


# http://127.0.0.1:5000/validate
@app.route("/validate", methods=['GET', 'POST'])
def validate():
    mail = request.form['mail']
    password = request.form['password']
    # return f"<p>E-mail : {mail}</p><p>Mot de passe : {password}</p>"
    return render_template("result.html", mail=mail, password=password)


# Lancer l'appli et aller sur http://127.0.0.1:5000
# server de dev tant que pas d'intall de waitress
app.run()
