from flask import Flask,redirect,render_template,request,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from pytube import YouTube

import os

app = Flask(__name__)
# creatimg configs
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:morgan8514@127.0.0.1:5432/YD'
# dialect+driver://username:password@host:port/database
app.config['SECRET_KEY'] = 'secret_key'

db=SQLAlchemy(app)

from models.download_info import YD
@app.before_first_request
def create():
    db.create_all

@app.route('/', methods=['POST','GET'])
def home():
    if request.method=='POST':
        recieved_url= request.form['users_input_url']
        print('url recieved')
        # python function to download video
        def download_yt(url):
            # flash("Communiccating with server...","success")
            yt = YouTube(url)
            # flash("Getting streams...")

            stream = yt.streams.first()
            # flash("Getting video title...")
            title = stream.title
            flash(title ,"info")
            try:
                # flash('downloading video...')
                stream.download ()
                flash('#####Download complete#####')
                # calling function to download
            except Exception:
                flash('error! unable to download site under contruction ', "warning")
        download_video = download_yt(recieved_url)
           
        return render_template('home.html')

    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)