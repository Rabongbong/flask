from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'hello world'

@app.route('/user/<int:username>')
def show_name(username):
  return f'{username}'

@app.route('/user/<path>')
def show_path(path):
  return path

if __name__ == '__main__':
  app.run()