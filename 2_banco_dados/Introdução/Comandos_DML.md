# Aula 06 e 07 - Comandos DML (INSERT, UPDATE, DELETE e WHERE)

## Conteúdo Estudado

### Comandos de Manipulação de Dados (DML - Data Manipulation Language)

Responsáveis pela inserção, alteração e exclusão dos registros armazenados nas tabelas.

* `INSERT`
* `UPDATE`
* `DELETE`

### Cláusula de Filtragem

Responsável por selecionar quais registros serão afetados por uma operação.

* `WHERE`

---

# Atualizando todos os telefones da tabela

```sql
UPDATE clientes
SET tel = "1234";
```

### Explicação

* `UPDATE clientes` → informa qual tabela será alterada;
* `SET` → define o novo valor da coluna;
* Como não existe a cláusula `WHERE`, **todos os registros da tabela serão modificados**.

---

# Consultando os dados

```sql
SELECT * FROM clientes;
```

### Resultado

| id | nome    | tel  | cidade |
| -: | ------- | ---- | ------ |
|  3 | Maylon  | 1234 | Poá    |
|  4 | Claudio | 1234 | Poá    |

> A ausência do `WHERE` fez com que todos os telefones fossem alterados.

---

# Atualizando apenas um registro

```sql
UPDATE clientes
SET tel = "40028922"
WHERE id = 3;
```

### Explicação

* `WHERE id = 3` limita a alteração ao cliente cujo ID é igual a 3.

---

# Consultando os dados novamente

```sql
SELECT * FROM clientes;
```

### Resultado

| id | nome    | tel      | cidade |
| -: | ------- | -------- | ------ |
|  3 | Maylon  | 40028922 | Poá    |
|  4 | Claudio | 1234     | Poá    |

Agora apenas Maylon teve seu telefone alterado.

---

# Atualizando vários registros ao mesmo tempo

```sql
UPDATE clientes
SET cidade = "Suzano"
WHERE cidade = "Poá";
```

### Explicação

Todos os clientes cuja cidade era "Poá" terão o valor alterado para "Suzano".

---

# Consultando os dados

```sql
SELECT * FROM clientes;
```

### Resultado

| id | nome    | tel      | cidade |
| -: | ------- | -------- | ------ |
|  3 | Maylon  | 40028922 | Suzano |
|  4 | Claudio | 1234     | Suzano |

---

# Inserindo novos clientes

```sql
INSERT INTO clientes (nome, tel, cidade)
VALUES ("Lon", "1140024922", "SP");

INSERT INTO clientes (nome, tel, cidade)
VALUES ("Clo", "5689565687", "SP");
```

### Explicação

* `INSERT INTO` adiciona novos registros;
* `VALUES` define os valores das colunas.

---

# Consultando os dados

```sql
SELECT * FROM clientes;
```

### Resultado

| id | nome    | tel        | cidade |
| -: | ------- | ---------- | ------ |
|  3 | Maylon  | 40028922   | Suzano |
|  4 | Claudio | 1234       | Suzano |
|  5 | Lon     | 1140024922 | SP     |
|  6 | Clo     | 5689565687 | SP     |

---

# Excluindo registros utilizando WHERE

```sql
DELETE FROM clientes
WHERE cidade = "SP";
```

### Explicação

* `DELETE FROM` remove registros da tabela;
* `WHERE cidade = "SP"` limita a exclusão apenas aos clientes da cidade de SP.

> Assim como no `UPDATE`, omitir o `WHERE` pode afetar todos os registros.

---

# Consultando os dados novamente

```sql
SELECT * FROM clientes;
```

### Resultado

| id | nome    | tel      | cidade |
| -: | ------- | -------- | ------ |
|  3 | Maylon  | 40028922 | Suzano |
|  4 | Claudio | 1234     | Suzano |

Os clientes "Lon" e "Clo" foram removidos.

---

# Excluindo a tabela inteira

```sql
DROP TABLE clientes;
```

### Explicação

* `DROP TABLE` remove completamente a tabela;
* A estrutura da tabela e todos os seus registros são apagados.

> Diferente do `DELETE`, o `DROP TABLE` remove a própria tabela do banco de dados.

---

# Conclusão

Este exercício demonstrou:

* atualização de registros com `UPDATE`;
* importância da cláusula `WHERE`;
* atualização de um ou vários registros;
* inserção de novos dados com `INSERT`;
* exclusão de registros com `DELETE`;
* diferença entre `DELETE` e `DROP TABLE`;
* riscos de executar comandos sem utilizar filtros.
