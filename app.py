from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'hello world'

@app.route('/user/<user>')
def show_user(user):
  return f"welcome to flask {user}"

if __name__ == '__main__':
  app.run()