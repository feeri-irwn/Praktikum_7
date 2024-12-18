from flask_sqlalchemy import SQLAlchemy
from flask import Flask

#init db connect
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://KelasPraktikum_pickpetboy:154b93a0f928519fb598bce52943d83eb1e0e8a7@de12p.h.filess.io:3306/KelasPraktikum_pickpetboy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def home():
    return "hello world!!!"
app.app_context().push()