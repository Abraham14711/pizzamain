from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///db.sqlite'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy()
db.init_app(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    tel = db.Column(db.String(11), nullable=False)
    food = db.Column(db.String, nullable=False)
    adress = db.Column(db.String(600), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<users {self.id}>"

@app.route('/')
def main_page():
    return render_template('main page.html')

@app.route('/отправить', methods=['POST'])
def send():
    name=request.form['name']
    tel=request.form['tel']
    food=request.form['food']
    adress=request.form['adress']
    db.session.add(Users(name,tel,food,adress))
    db.session.commit()
    return redirect(url_for('main page.html'))


@app.route('/contacts')
def contacts():
    return render_template('Contacts.html')

@app.route('/new')
def new_things():
    return render_template('New things.html')

@app.route('/new1')
def new1():
    return render_template('new 1.html')

@app.route('/new2')
def new2():
    return render_template('new 2.html')


if __name__ == '__main__':
    app.run()


