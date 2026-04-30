from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

DATABASE = os.path.join(os.path.dirname(__file__), 'database.db')

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    items = conn.execute('SELECT * FROM items').fetchall()
    conn.close()
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add():
    nome = request.form['nome']
    cpf = request.form['cpf']
    telefone = request.form['telefone']
    email = request.form['email']
    if nome and cpf:
        conn = get_db_connection()
        conn.execute(
            'INSERT INTO items (nome, cpf, telefone, email) VALUES (?, ?, ?, ?)',
            (nome, cpf, telefone, email)
        )
        conn.commit()
        conn.close()
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    conn = get_db_connection()
    item = conn.execute('SELECT * FROM items WHERE id = ?', (id,)).fetchone()
    if not item:
        conn.close()
        return redirect(url_for('index'))

    if request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        telefone = request.form['telefone']
        email = request.form['email']
        if nome and cpf:
            conn.execute(
                'UPDATE items SET nome = ?, cpf = ?, telefone = ?, email = ? WHERE id = ?',
                (nome, cpf, telefone, email, id)
            )
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    conn.close()
    return render_template('edit.html', item=item)

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM items WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)


#cd
#db_setup.py
#python app.py

#http://localhost:5000/
#http://127.0.0.1:5000/