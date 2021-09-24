from app import hello_world, show_user

def test_hello_world():
  value = hello_world()
  assert 'hello world' == value
  

def test_show_user(user='rabong'):
  value = show_user(user)
  assert f'welcome to flask {user}' == value