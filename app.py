from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'hello world'

@app.route('/user/<user>')
def show_path(user):
  return f"welcome to flask {user}"

if __name__ == '__main__':
  app.run()