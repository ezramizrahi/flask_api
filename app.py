import flask
from flask import request, jsonify

app = flask.Flask(__name__)

# data
data = [
    {'name': 'Ezra Mizrahi',
     'title': 'software engineer',
     'skills': [
     'javascript',
     'react.js',
     'node.js',
     'python',
     'ruby',
     'golang',
     'e2e testing',
     'cypress.io',
     'selenium',
     'test driven development',
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

# returns all info about Ezra Mizrahi
@app.route('/', methods=['GET'])
def api_all():
    return jsonify(data)

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000, debug=True, use_reloader=True)
