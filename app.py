from flask import Flask,redirect,render_template,request,url_for
from flask_sqlalchemy import SQLAlchemy
from pytube import YouTube
import os

app = Flask(__name__)


# importing db from download_info.py file


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
        url = request.form['users_input_url']

        # print(url)
        commit_url = YD(url=url)
        # commited_url = commit_url.create()
            #youtub function to download
        def download_func(url):
            yt = YouTube(url)
            videos = yt.streams.first()
            # s=1
            # for all in videos:
            #     print(all)
            #     s=s+1
            stream.download('/Downloads')
      
            


        download=download_func(url)
        print('imeingia')



        
    return render_template('home.html')





if __name__ == "__main__":
    app.run(debug=True)