from flask import Flask, render_template
from sqlalchemy import false, true
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
#app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqllite:///test.db'
#db = SQLAlchemy(app)

#class Todo(db.Model):
    #id = db.column(db.Integer, primary_key=true)
    #content = db.Column(db.String(200), nullable=false)
    #date_created = db.Column(db.DateTime, default=datetime.utcnow)

    #def __repr__(self): 
        #return '<Task %r>' % self.id

@app.route('/')
def index():
    return render_template('index.html')
    
if __name__== "__main__":
    app.run(host='0.0.0.0', port=5000, debug=true)

