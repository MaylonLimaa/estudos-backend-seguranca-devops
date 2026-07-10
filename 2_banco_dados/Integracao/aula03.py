"""
Banco de dados SQLite com Python #3

Aula onde aprenderemos sobre a exclusão de dados no banco de dados.
"""

import sqlite3
banco = sqlite3.connect('primeiro_banco.db')
cursor = banco.cursor()

cursor.execute("DELETE FROM pessoas WHERE id > 9")
banco.commit()

cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall())