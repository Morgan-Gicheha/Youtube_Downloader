from flask import Flask,redirect,render_template,request,url_for
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
            print('getting video...')
            yt = YouTube(url)
            print('getting streams')

            stream = yt.streams.first()
            print('getting video title...')
            title = stream.title
            print(title)
            print('downloading video...')
            stream.download()
            print('#####Download complete#####')
            # calling function to download
        download_video = download_yt(recieved_url)
           
        return render_template('home.html')

    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)