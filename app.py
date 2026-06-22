# app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

data = [
    ["Ячейка 1.1", "Ячейка 1.2", "Ячейка 1.3"],
    ["Ячейка 2.1", "Ячейка 2.2", "Ячейка 2.3"]
]

@app.route('/')
def index():
    return render_template('index.html', data=data)

@app.route('/add', methods=['POST'])
def add_row():
    new_row = [
        request.form.get('col1', ''),
        request.form.get('col2', ''),
        request.form.get('col3', '')
    ]
    data.append(new_row)
    return redirect(url_for('index'))

@app.route('/delete/<int:row_id>', methods=['POST'])
def delete_row(row_id):
    if 0 <= row_id < len(data):
        data.pop(row_id)
    return redirect(url_for('index'))

# host='0.0.0.0' делает сервер доступным извне контейнера Codespaces
# port=8080 — стандартный порт для веб-приложений в Codespaces
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
