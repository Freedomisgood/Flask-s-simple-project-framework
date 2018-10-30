from flask import Flask,request,render_template,redirect
import config
from exts import db
from models import Detail
app = Flask(__name__)

app.config.from_object(config)
db.init_app(app)

# with app.app_context():
#     db.create_all()

# @app.route('/',methods=['GET','POST'])
# def login():
#     if request.method == 'GET':
#         return render_template('login.html')
#     else:
#         return redirect('/data/')

@app.route('/')
def query():
    return 'Hello world'

@app.route('/data/')
def data():
    device = Detail(Latitude='qwe',longitude='asd')
    db.session.add(device)
    db.session.commit()
    return 'add done'

@app.route('/query/')
def query():
    device = Detail.query.filter(Detail.longitude=='asd').first()
    if device:
        print(device.Latitude)
    return 'query done'

if __name__ == '__main__':
    app.run(debug=True)
