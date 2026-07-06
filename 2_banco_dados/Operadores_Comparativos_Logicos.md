# Aula 08, 09 e 10 - Operadores Comparativos e Lógicos

## Conteúdo Estudado

Nesta etapa do curso foram apresentados os principais operadores utilizados em conjunto com a cláusula `WHERE`, permitindo realizar filtros e consultas mais específicas.

---

# Operadores Comparativos

Os operadores comparativos são utilizados para comparar valores.

| Operador | Significado    |
| -------- | -------------- |
| =        | Igual          |
| != ou <> | Diferente      |
| >        | Maior que      |
| >=       | Maior ou igual |
| <        | Menor que      |
| <=       | Menor ou igual |

---

## Operador Igual (=)

```sql
SELECT * FROM produtos
WHERE produto = "Calça";
```

### Explicação

Retorna apenas os registros cujo produto seja exatamente "Calça".

### Resultado

| id | produto | cor   | valor |
| -: | ------- | ----- | ----: |
|  1 | Calça   | Azul  | 49.90 |
|  5 | Calça   | Preta | 59.90 |

---

## Operador Diferente (!= ou <>)

```sql
SELECT * FROM produtos
WHERE cor != "Azul";
```

### Explicação

Retorna todos os produtos cuja cor seja diferente de azul.

---

## Operador Maior que (>)

```sql
SELECT * FROM produtos
WHERE valor > 50;
```

### Explicação

Retorna todos os produtos com valor superior a R$ 50,00.

---

## Operador Menor que (<)

```sql
SELECT * FROM produtos
WHERE valor < 30;
```

### Explicação

Retorna todos os produtos com valor inferior a R$ 30,00.

---

## Operador Maior ou Igual (>=)

```sql
SELECT * FROM produtos
WHERE valor >= 50;
```

### Explicação

Retorna os produtos com valor igual ou superior a R$ 50,00.

---

## Operador Menor ou Igual (<=)

```sql
SELECT * FROM produtos
WHERE valor <= 50;
```

### Explicação

Retorna os produtos com valor igual ou inferior a R$ 50,00.

---

# Operadores Lógicos

Os operadores lógicos permitem combinar múltiplas condições.

## Operador AND

```sql
SELECT * FROM produtos
WHERE cor = "Preto"
AND valor > 50;
```

### Explicação

Ambas as condições precisam ser verdadeiras.

---

## Operador OR

```sql
SELECT * FROM produtos
WHERE cor = "Azul"
OR cor = "Preto";
```

### Explicação

Pelo menos uma das condições precisa ser verdadeira.

---

## Operador IN

```sql
SELECT * FROM produtos
WHERE cor IN ("Azul", "Preto", "Vermelho");
```

### Explicação

Equivale a fazer várias comparações utilizando `OR`.

Exemplo equivalente:

```sql
SELECT * FROM produtos
WHERE cor = "Azul"
OR cor = "Preto"
OR cor = "Vermelho";
```

---

## Operador NOT

```sql
SELECT * FROM produtos
WHERE NOT cor = "Azul";
```

### Explicação

Inverte a condição, retornando tudo que não seja azul.

---

# Operador BETWEEN

Utilizado para trabalhar com intervalos.

```sql
SELECT * FROM produtos
WHERE valor BETWEEN 30 AND 50;
```

### Explicação

Retorna todos os produtos com valor entre R$ 30,00 e R$ 50,00.

O mesmo resultado poderia ser obtido com:

```sql
SELECT * FROM produtos
WHERE valor >= 30
AND valor <= 50;
```

---

# Operador LIKE

Utilizado para procurar padrões em textos.

---

## Começa com

```sql
SELECT * FROM produtos
WHERE produto LIKE "Ca%";
```

### Explicação

Retorna todos os produtos cujo nome começa com "Ca".

Exemplos:

* Calça
* Camiseta
* Casaco

---

## Termina com

```sql
SELECT * FROM produtos
WHERE produto LIKE "%ta";
```

### Explicação

Retorna os produtos que terminam com "ta".

Exemplo:

* Camiseta

---

## Contém

```sql
SELECT * FROM produtos
WHERE produto LIKE "%sa%";
```

### Explicação

Retorna todos os produtos que possuam "sa" em qualquer parte do nome.

Exemplos:

* Casaco
* Camiseta

---

# Estrutura utilizada nas aulas

Para os exemplos práticos, foi criada a tabela `produtos`, contendo:

* `id`
* `produto`
* `cor`
* `tamanho`
* `sexo`
* `valor`
* `mes`
* `ano`

Os registros foram importados através de um arquivo CSV, demonstrando uma forma mais rápida de popular uma tabela com diversos dados.

---

# Conclusão

Neste conjunto de aulas foram apresentados:

* operadores comparativos;
* operadores lógicos;
* cláusula `WHERE`;
* filtragem de dados;
* operador `BETWEEN`;
* operador `LIKE`;
* consultas mais específicas utilizando múltiplas condições.

Esses conceitos representam a base das consultas SQL e serão amplamente utilizados em bancos de dados maiores e em projetos futuros com Python e SQLite.
 