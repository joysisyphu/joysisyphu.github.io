#from flask import Flask

#app = Flask('hello')

#@app.route('/')
#def hello():
#  return 'Hello world!'

#@app.route('/page2')
#def page2():
#  return 'This is page 2'

#@app.route('/page3')
#def page3():
#  return '''
#<html>
#<head>
#  <title>page 3</title>
#</head>

#<body>
#  <h1>hi there</h1>
#  <h2>subheading</h2>
#  <hr>
#  here is some html with a <a href=page2>link to page 2</a>
#  <hr>
#</body>
#</html>
#'''

#some_data = {'key1': 'a bit of data',
#             'key2': 'some more data',
#             'key3': 'even more'}

#@app.route('/data/<key>')
#def data(key):
#  try:
#    return 'data for ' + key + ': ' + some_data[key]
#  except KeyError:
#    return 'sorry there is no data for ' + key
