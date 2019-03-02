from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sms')
def sms():
    return render_template('sms.html')


@app.route('/town/<name>')
def town(name):
    return '<h1>I am in {}</h1>'.format(name)


@app.route('/latin/<latin_name>')
def latin(latin_name):

    latiname = ''

    if latin_name[-1] == 'y':
        latiname = latin_name[:-1] + 'iful'

    else:
        latiname = latin_name + 'y'

    return f'<h1>My latin name is {latiname}</h1>'


if __name__ == '__main__':
    app.run(debug=True)
