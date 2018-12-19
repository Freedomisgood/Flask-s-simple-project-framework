from flask import Flask,request,render_template,redirect
import config
from exts import db
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
def hello():
    return 'Hello world'


if __name__ == '__main__':
    app.run(debug=True)
