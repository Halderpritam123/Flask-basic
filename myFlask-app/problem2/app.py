from flask import Flask, render_template, request

app = Flask(__name__)

# Create an empty dictionary to store data
data_dict = {}

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        key = request.form['key']
        value = request.form['value']
        data_dict[key] = value
        return 'Entry created successfully!'
    return render_template('create.html')

@app.route('/read')
def read():
    return render_template('read.html', data=data_dict)

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        key = request.form['key']
        if key in data_dict:
            value = request.form['value']
            data_dict[key] = value
            return 'Entry updated successfully!'
        else:
            return 'Key does not exist!'
    return render_template('update.html')

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        key = request.form['key']
        if key in data_dict:
            del data_dict[key]
            return 'Entry deleted successfully!'
        else:
            return 'Key does not exist!'
    return render_template('delete.html')

if __name__ == '__main__':
    app.run(debug=True)
