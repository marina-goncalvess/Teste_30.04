import sqlite3

def create_database():
    #conexão o banco de dados/cria o arquivo

    conn = sqlite3.connect('database.db')
    #cria a tabela 
    conn.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf TEXT NOT NULL,
            telefone TEXT,
            email TEXT
        )
    ''')
    conn.commit()
    conn.close()
    print("Banco de dados criado com sucesso!")
if __name__ == "__main__":
    create_database()