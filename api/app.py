from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"
@app.route("/about")
def hello():
  return "Hello this is about page!, I'm running using Vercel"

if __name__ == "__main__":
  app.run()
