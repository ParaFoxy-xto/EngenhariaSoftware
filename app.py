from flask import Flask, render_template, request, redirect, Response
import csv
from datetime import datetime

app = Flask(__name__)

students = []

@app.route('/')
def index():
    return render_template('index.html', students=students)

@app.route('/submit', methods=['POST'])
def submit():
    id = request.form['id']
    name = request.form['name']
    present = request.form.get('present')
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    students.append([id, name, date])
    
    return redirect('/')

@app.route('/export', methods=['GET'])
def export():
    with open('students.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Name', 'Date'])
        writer.writerows(students)
    
    def generate():
        with open('students.csv', 'r') as file:
            data = file.read()
        response = Response(data, mimetype='text/csv')
        response.headers.set("Content-Disposition", "attachment", filename="students.csv")
        return response
    
    return generate()

if __name__ == '__main__':
    app.run(debug=True)
