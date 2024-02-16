from flask import Flask, render_template, request

app = Flask(__name__)

checklist = []
completed = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        item = request.form.get('item')
        action = request.form.get('action')
        if action == 'add':
            checklist.append(item)
        elif action == 'complete':
            checklist.remove(item)
            completed.append(item)
    return render_template('index.html', checklist=checklist, completed=completed)

if __name__ == "__main__":
    app.run()