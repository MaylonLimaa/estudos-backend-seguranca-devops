# Aula 03, 04 e 05 - Comandos DDL

## Conteúdo Estudado

### Comandos de Definição de Dados (DDL - Data Definition Language)

Responsáveis pela criação e alteração da estrutura do banco de dados.

* `CREATE DATABASE`
* `CREATE TABLE`
* `ALTER TABLE`
* `DROP TABLE`

### Comandos de Manipulação de Dados (DML - Data Manipulation Language)

Responsáveis pela inserção, atualização e remoção dos registros.

* `INSERT`
* `UPDATE`
* `DELETE`

### Comandos de Consulta (DQL - Data Query Language)

Responsáveis pela leitura dos dados armazenados.

* `SELECT`

Esses são alguns dos principais comandos da linguagem SQL, embora existam diversos outros.

---

# Criando a tabela de clientes

```sql
CREATE TABLE clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    tel TEXT
);
```

### Explicação

* `id`: chave primária da tabela (`PRIMARY KEY`) e incremento automático (`AUTOINCREMENT`);
* `nome`: armazena o nome do cliente;
* `tel`: armazena o telefone do cliente.

> Apesar de o telefone conter apenas números, normalmente ele é armazenado como `TEXT`, pois pode conter parênteses, hífens e zeros à esquerda.

---

# Consultando os dados da tabela

```sql
SELECT * FROM clientes;
```

### Explicação

* `SELECT` → seleciona dados;
* `*` → significa "todas as colunas";
* `FROM clientes` → informa de qual tabela os dados serão obtidos.

Neste momento, a tabela ainda está vazia, portanto nenhuma linha será retornada.

### Resultado

|                  id | nome | tel |
| ------------------: | ---- | --- |
| *(nenhum registro)* |      |     |

---

# Inserindo dados

```sql
INSERT INTO clientes (nome, tel)
VALUES ("Maylon", "1140028922");
```

### Explicação

* `INSERT INTO` significa "inserir na tabela";
* `VALUES` define os valores que serão adicionados.

Após inserir os dados:

```sql
SELECT * FROM clientes;
```

### Resultado

| id | nome   | tel        |
| -: | ------ | ---------- |
|  1 | Maylon | 1140028922 |

---

# Adicionando uma nova coluna

```sql
ALTER TABLE clientes
ADD COLUMN cidade TEXT;
```

### Explicação

* `ALTER TABLE` altera a estrutura da tabela;
* `ADD COLUMN` adiciona uma nova coluna.

---

# Inserindo um novo cliente

```sql
INSERT INTO clientes (nome, tel, cidade)
VALUES ("Claudio", "5689565687", "Poá");
```

Agora temos:

* Maylon → sem cidade cadastrada;
* Claudio → cidade igual a "Poá".

Ao executar:

```sql
SELECT * FROM clientes;
```

percebemos que a coluna `cidade` do primeiro cliente ficou com valor `NULL`, pois ela foi criada depois do registro já existir.

### Resultado

| id | nome    | tel        | cidade |
| -: | ------- | ---------- | ------ |
|  1 | Maylon  | 1140028922 | NULL   |
|  2 | Claudio | 5689565687 | Poá    |

---

# Importância do planejamento

Até este momento, todas as colunas permitem valores nulos.

Suponha que desejamos tornar a coluna `cidade` obrigatória utilizando `NOT NULL`.

Primeiro, removemos a coluna:

```sql
ALTER TABLE clientes
DROP COLUMN cidade;
```

Verificando novamente:

```sql
SELECT * FROM clientes;
```

podemos observar que a coluna foi removida.

### Resultado

| id | nome    | tel        |
| -: | ------- | ---------- |
|  1 | Maylon  | 1140028922 |
|  2 | Claudio | 5689565687 |

---

# Tentando criar uma coluna obrigatória

```sql
ALTER TABLE clientes
ADD COLUMN cidade TEXT NOT NULL;
```

O SQLite retorna o erro:

```text
Cannot add a NOT NULL column with default value NULL
```

Isso acontece porque os registros já existentes não possuem valor para a nova coluna.

---

# Removendo os registros

```sql
DELETE FROM clientes;
```

### Atenção

Esse comando remove todos os registros da tabela, mas **não remove a tabela em si**.

Após executar:

```sql
SELECT * FROM clientes;
```

nenhum dado será retornado.

### Resultado

|                  id | nome | tel |
| ------------------: | ---- | --- |
| *(nenhum registro)* |      |     |

---

# Criando novamente a coluna obrigatória

```sql
ALTER TABLE clientes
ADD COLUMN cidade TEXT NOT NULL;
```

Agora a operação é executada com sucesso, pois não existem registros na tabela.

---

# Inserindo os dados novamente

```sql
INSERT INTO clientes (nome, tel, cidade)
VALUES ("Maylon", "1140024922", "Poá");

INSERT INTO clientes (nome, tel, cidade)
VALUES ("Claudio", "5689565687", "Poá");
```

Consultando:

```sql
SELECT * FROM clientes;
```

os dados aparecem normalmente.

Observe que o campo `id` continua sendo incrementado automaticamente.

### Resultado

| id | nome    | tel        | cidade |
| -: | ------- | ---------- | ------ |
|  3 | Maylon  | 1140024922 | Poá    |
|  4 | Claudio | 5689565687 | Poá    |

> Mesmo após apagar os registros, o contador do `AUTOINCREMENT` não foi reiniciado.

---

# Tentando inserir um cliente sem cidade

```sql
INSERT INTO clientes (nome, tel)
VALUES ("Marcos", "4554548");
```

Resultado:

```text
NOT NULL constraint failed: clientes.cidade
```

### Explicação

Como a coluna `cidade` foi criada com a restrição `NOT NULL`, todos os novos registros são obrigados a informar esse valor.

---

# Conclusão

Este exercício demonstrou:

* criação de tabelas;
* consulta de dados;
* inserção de registros;
* alteração da estrutura da tabela;
* exclusão de registros;
* utilização da restrição `NOT NULL`;
* importância do planejamento da estrutura do banco de dados.

Além disso, foi possível observar que o `AUTOINCREMENT` continua a sequência dos IDs mesmo após a exclusão dos registros da tabela.
