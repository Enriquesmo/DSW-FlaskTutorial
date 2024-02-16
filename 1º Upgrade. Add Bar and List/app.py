from flask import Flask, render_template, request

app = Flask(__name__)

checklist = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        item = request.form.get('item')
        action = request.form.get('action')
        if action == 'add':
            checklist.append(item)
    return render_template('index.html', checklist=checklist)

if __name__ == "__main__":
    app.run()