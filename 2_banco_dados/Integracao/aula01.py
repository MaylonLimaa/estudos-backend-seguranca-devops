"""
Banco de dados SQLite com Python #1
Aula onde aprendemos os primeiros passos para criar uma conexão com um banco de dados, criar tabelas, inserir dados etc.
"""

# Importa o módulo sqlite3, responsável por fornecer os recursos necessários para trabalhar com bancos de dados SQLite.
import sqlite3

# Cria uma conexão com um banco de dados SQLite por meio do método connect().
# Caso o arquivo do banco não exista, ele será criado automaticamente.
banco = sqlite3.connect('primeiro_banco.db')

# Cria um cursor.
# O cursor é o objeto responsável por executar comandos SQL.
# Quando uma consulta retorna dados, ele também armazena e gerencia esses resultados,
# permitindo que o programa os consulte de forma organizada.
cursor = banco.cursor()

# Executa um comando SQL utilizando o cursor por meio do método execute().
# Neste caso, foi exemplificado como criar uma tabela
# cursor.execute("CREATE TABLE IF NOT EXISTS pessoas (id integer primary key autoincrement, nome text, idade integer)")
# # Exemplo de inserção de dados na tabela.
#for i in range(0, 10):
#    cursor.execute(f"INSERT INTO pessoas(nome, idade) VALUES ('Maylon', {i})")

# Confirma todas as alterações realizadas desde o último commit.
# Sem essa confirmação, as alterações poderão ser descartadas caso a execução seja encerrada.
#banco.commit()

# Agora, segue o exemplo de como consultar dados do banco de dados
#cursor.execute("SELECT * FROM pessoas")
# Recupera todos os registros retornados pela última consulta executada pelo cursor.
# Existem outros métodos iniciados por "fetch", cada um destinado a uma forma diferente de recuperar os resultados da consulta.
#print(cursor.fetchall())
