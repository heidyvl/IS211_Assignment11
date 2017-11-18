from flask import Flask, render_template, request, redirect, session
import re

app = Flask(__name__)

task = ''
email = ''
priority = ''
task_list = []
email_list = []
priority_list = []

@app.route('/')

def todolist():

    return render_template('index.html', task=task, email=email, priority=priority)

@app.route('/submit', methods = ['POST'])
           
def addItem():
    
        task = request.form['Task']
        email = request.form['Email']
        priority = request.form['Priority']

        if priority != 'Select' and task != '' and re.search('@', email):
            task_list.append(task)
            email_list.append(email)
            priority_list.append(priority)
        return render_template('index.html', task_list=task_list, email_list = email_list, priority_list = priority_list)
    
    
@app.route('/clear', methods = ['POST'])

def clear_list():
    task_list[:] = []
    email_list[:] = []
    priority_list[:] = []
    return redirect('/')

if __name__ == '__main__':
    app.run()

