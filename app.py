from flask import Flask 
from flask import render_template #type:ignore

app=Flask(__name__)

@app.route("/")

def home():

    JOBS = [
        {
            'id':1,
            'title':'Data Analyst',
            'location':'Bengaluru, India',
            'salary':'Rs. 10,00,000'
        },
        {
            'id':2,
            'title':'Data Scientist',
            'location':'Delhi, India',
            'salary':'Rs. 15,00,000'

        },
        {
            'id':3,
            'title':'Frontend Engineer',
            'location':'Remote',
            'salary':'Rs. 12,00,000'
        }
    ]
    return render_template("home.html", jobs=JOBS)

if __name__=="__main__":
  app.run(host='0.0.0.0', debug=True)

