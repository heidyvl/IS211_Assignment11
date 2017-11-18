from flask import Flask, render_template, request, redirect

app = Flask(__name__)
@app.route('/', methods = ['POST'])

def addItem():
    email = request.form['email']
    print("The email address is '" + email + "'")
    return redirect('/')

if __name__ == '__main__':
    app.run()
