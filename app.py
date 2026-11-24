from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World'

@app.route('/class_page')
def class_page():
    return 'Fundamentals of DataScience and Engineering'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
