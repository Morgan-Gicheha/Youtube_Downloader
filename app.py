from flask import Flask,redirect,render_template,request,url_for
from flask_sqlalchemy import SQLAlchemy
from pytube import YouTube
import urllib.request
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
        recieved_url= request.form['users_input_url']
        print('imeingia')
        # python function to download video
        def download_yt(url):
            print('getting video...')
            yt = YouTube(url)
            print('getting streams')

            streams=yt.streams.first()
            print('getting video title...')
            # print(yt.title)
            print('downloadint video...')
            yt.streams.download()
            print('#####Download complete#####')
            
        download_yt(recieved_url)
        print("pgrogress")
    
        
      
        

        return render_template('home.html')
# route to view videoes available for download
# @app.route('/home/download' , methods=['GET','POST'])
# def download_route():

#     return render_template('view_streams_availabe.html')


        
    return render_template('home.html')





if __name__ == "__main__":
    app.run(debug=True)