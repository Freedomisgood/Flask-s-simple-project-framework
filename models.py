from exts import db



class Detail(db.Model):
    __tablename__ = 'Detail'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    Latitude = db.Column(db.String(100),nullable=False)
    longitude = db.Column(db.String(100),nullable=False)