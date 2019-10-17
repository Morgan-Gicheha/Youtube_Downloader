from app import db
from app import *
# creating a database
class YD (db.Model):
    __tablename__='YD'
    id = db.Column(db.Integer, primary_key=True)
    url= db.Column(db.String())
    time_of_download = db.Column(db.DateTime)
    # ip_address_of_download = db.Column(db.)

    # function to commit to   db
    def create(self):
        db.session.add(self)
        db.session.commit()

    # python function to download



    
