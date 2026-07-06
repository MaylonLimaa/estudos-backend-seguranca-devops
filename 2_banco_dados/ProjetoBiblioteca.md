# 📚 Projeto Final - Sistema de Biblioteca com SQLite3

## Introdução

Este projeto consiste na criação de um banco de dados para um sistema simples de biblioteca utilizando SQLite3.

O principal objetivo é praticar a modelagem de dados, criação de tabelas, relacionamentos e manipulação de informações através dos comandos SQL estudados durante o minicurso.

Este documento apresenta o planejamento do banco de dados, as decisões tomadas durante a modelagem e a implementação prática do projeto.

Este é o primeiro e último projeto desenvolvido utilizando apenas SQL. Os próximos projetos passarão a integrar Python e banco de dados, permitindo a implementação de regras de negócio, automações e aplicações completas.

---

# 🎯 Objetivo do Projeto

O sistema tem como finalidade armazenar informações sobre:

* Livros;
* Clientes;
* Empréstimos.

O projeto foi desenvolvido com foco educacional, servindo como ambiente de prática para os principais conceitos de bancos de dados relacionais.

---

# 📖 Regras do Sistema

* Um cliente pode possuir vários empréstimos.
* Todo empréstimo deve estar associado a um cliente.
* Todo empréstimo deve estar associado a um livro.
* Um livro pode participar de vários empréstimos ao longo do tempo.
* Um livro só pode estar emprestado para um cliente por vez.
* O campo `emprestado` informa se o livro está disponível ou não.
* O campo `status` informa se o cliente possui empréstimos ativos.

---

# 🗄️ Estrutura do Banco de Dados

## Tabela: Livros

| Coluna     | Tipo    | Descrição                       |
| ---------- | ------- | ------------------------------- |
| id_livro   | INTEGER | Chave primária                  |
| titulo     | TEXT    | Título da obra                  |
| genero     | TEXT    | Gênero literário                |
| emprestado | INTEGER | 0 = Disponível / 1 = Emprestado |

---

## Tabela: Clientes

| Coluna     | Tipo    | Descrição                                                  |
| ---------- | ------- | ---------------------------------------------------------- |
| id_cliente | INTEGER | Chave primária                                             |
| nome       | TEXT    | Nome do cliente                                            |
| cpf        | TEXT    | CPF único                                                  |
| tel        | TEXT    | Telefone                                                   |
| status     | INTEGER | 0 = Sem empréstimos ativos / 1 = Possui empréstimos ativos |

---

## Tabela: Empréstimo

| Coluna          | Tipo    | Descrição                    |
| --------------- | ------- | ---------------------------- |
| id_emprestimo   | INTEGER | Chave primária               |
| id_cliente      | INTEGER | FK para clientes             |
| id_livro        | INTEGER | FK para livros               |
| data_emprestimo | TEXT    | Data do empréstimo           |
| data_devolucao  | TEXT    | Data prevista para devolução |

---

# 🔗 Relacionamentos

```text
Cliente (1)
    │
    └───────< Empréstimo >───────┐
                                 │
                                 │
                              Livro (1)
```

### Cardinalidade

* Cliente → Empréstimo = 1:N
* Livro → Empréstimo = 1:N

---

# 🛠️ Implementação

## Criação das Tabelas

```sql
CREATE TABLE livros(
    id_livro INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    genero TEXT,
    emprestado INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE clientes(
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT UNIQUE NOT NULL,
    tel TEXT NOT NULL,
    status INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE emprestimo(
    id_emprestimo INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER,
    id_livro INTEGER,
    data_emprestimo TEXT,
    data_devolucao TEXT,

    FOREIGN KEY(id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY(id_livro) REFERENCES livros(id_livro)
);
```

---

## Inserção de Dados

Foram cadastrados:

* 20 livros;
* 20 clientes;
* 5 empréstimos.

Além disso, foram realizadas atualizações para indicar:

* Livros atualmente emprestados;
* Clientes com empréstimos ativos.

```sql
UPDATE livros
SET emprestado = 1
WHERE id_livro IN (1, 3, 5, 7, 9);

UPDATE clientes
SET status = 1
WHERE id_cliente IN (1, 2, 3, 4, 5);
```

---

# 📚 Conceitos Aplicados

Durante o desenvolvimento deste projeto foram utilizados os seguintes conceitos:

* CREATE TABLE;
* PRIMARY KEY;
* AUTOINCREMENT;
* FOREIGN KEY;
* UNIQUE;
* NOT NULL;
* DEFAULT;
* INSERT;
* UPDATE;
* SELECT;
* Modelagem de banco de dados;
* Relacionamentos entre tabelas;
* Cardinalidade 1:N.

---

# ✅ Conclusão

Este projeto representa a conclusão da etapa inicial de estudos em SQL utilizando SQLite3.

Durante o desenvolvimento foi possível aplicar os principais conceitos de bancos de dados relacionais, incluindo modelagem, criação de tabelas, relacionamentos, inserção e atualização de dados.

A partir deste ponto, os próximos projetos passarão a integrar Python com SQLite, permitindo a implementação de regras de negócio, automações e aplicações mais próximas de cenários reais de desenvolvimento.

Este projeto serviu como base para consolidar os fundamentos necessários para os próximos estudos envolvendo backend, APIs e persistência de dados.
