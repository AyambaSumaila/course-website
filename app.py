from flask import Flask #type:ignore

app=Flask(__name__)

@app.route("/")

def home():
    return "<h1>Sumaila, Hello World</h1>"

if __name__=="__main__":
  app.run(host='0.0.0.0', debug=True)

