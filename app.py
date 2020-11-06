import flask
from flask import request, jsonify

app = flask.Flask(__name__)

# data
data = [
    {'name': 'Ezra Mizrahi',
     'title': 'software engineer',
     'skills': [
     'javascript',
     'es6',
     'react.js',
     'node.js',
     'python',
     'flask',
     'ruby',
     'golang',
     'e2e testing',
     'cypress.io',
     'selenium',
     'test driven development',
     'unit testing',
     'jest',
     'enzyme',
     'rspec',
     'CI/CD',
     'AWS',
     'bash scripting'
     ],
     'email': 'ezra.mizrahi@hey.com',
     'blog_url': 'https://gitcommit.netlify.app/',
     'github_url': 'https://github.com/ezramizrahi'}
]

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Ezra Mizrahi</h1>
<p>An API with information about me, such as: name, software engineering skills, websites.</p>
<p>Made using Flask.</p>'''

# returns all info about Ezra Mizrahi
@app.route('/ezra', methods=['GET'])
def api_all():
    return jsonify(data)

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000, debug=True, use_reloader=True)
