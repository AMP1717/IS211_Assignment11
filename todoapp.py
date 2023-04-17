from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialize a list to store tasks
tasks = []

# Define a route to add new tasks
@app.route('/submit', methods=['POST'])
def add_task():
    if request.method == 'POST':

        # get TO DO details
        description = request.form['description']
        email = request.form['email']
        priority = request.form['priority']

        #input validation is also done in the form itself
        if "@" in email and priority in ["High", "Medium", "Low"]:
            task = {'description': description, 'email': email, 'priority': priority}
            tasks.append(task)        

    return redirect(url_for('show_tasks'))

# Define a route to display all tasks
@app.route('/')
def show_tasks():
    return render_template('index.html', tasks=tasks)

@app.route('/clear', methods=['POST'])
def clear():
    tasks.clear()
    return redirect(url_for('show_tasks'))


if __name__ == '__main__':
    app.run(debug=True)