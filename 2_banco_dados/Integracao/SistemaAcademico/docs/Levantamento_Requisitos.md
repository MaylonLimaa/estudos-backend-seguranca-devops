# 1 – Levantamento de Requisitos

## O que é o sistema?

Este sistema consiste em um protótipo de um sistema acadêmico desenvolvido com finalidade didática.

O projeto teve início durante a etapa de **Fundamentos**, utilizando dicionários como mecanismo de armazenamento de dados. Nesta nova versão, será reestruturado utilizando **Programação Orientada a Objetos (POO)** e **SQLite** para persistência dos dados.

Ao longo do roadmap de estudos, novas funcionalidades serão incorporadas ao sistema, incluindo APIs, autenticação, autorização e outras tecnologias, permitindo sua evolução contínua.

Inicialmente, o sistema será composto pelas seguintes entidades:

- Aluno
- Professor
- Sala
- Matéria

---

## Escopo

O principal objetivo deste projeto é servir como ambiente de aprendizagem prática.

Conforme novos conceitos forem estudados, eles serão aplicados ao sistema, permitindo sua evolução gradual e aproximando-o cada vez mais de um sistema acadêmico real.

Por esse motivo, novas funcionalidades, melhorias e refatorações serão implementadas ao longo do desenvolvimento.

---

## Funcionalidades do sistema

### Cadastro

- Cadastrar alunos;
- Cadastrar professores;
- Cadastrar salas;
- Cadastrar matérias.

### Relacionamentos

- Associar alunos às salas;
- Associar professores às salas.

### Gestão acadêmica

- Registrar notas dos alunos;
- Calcular automaticamente a média;
- Informar se o aluno foi aprovado ou reprovado.

### Consultas

- Consultar as informações dos alunos.

### Manutenção

- Alterar informações cadastradas;
- Remover registros do sistema.

---

## Entidades

O sistema será composto pelas seguintes entidades:

- Aluno;
- Professor;
- Sala;
- Matéria.

---

## Regras de negócio

### Sistema

- Cada CPF deverá ser único;
- Cada matrícula deverá ser única;
- Não será permitido o cadastro de registros duplicados;
- O e-mail deverá possuir um formato válido.

### Sala

- Uma sala poderá possuir diversos alunos;
- Cada sala possuirá apenas um professor responsável;
- Cada sala possuirá apenas uma matéria.
- Uma Sala só poderá ser considerada válida quando possuir pelo menos um aluno, um professor responsável e uma matéria atribuída.

### Professor

- Cada professor será responsável por apenas uma matéria.

### Notas

- As notas deverão estar entre 0 e 10;
- A média será calculada automaticamente pelo sistema;
- O aluno será considerado aprovado caso obtenha média igual ou superior a 6.

---

## Requisitos não funcionais

- Todo o sistema deverá ser desenvolvido em Python;
- A persistência dos dados será realizada utilizando SQLite;
- O sistema deverá seguir os princípios da Programação Orientada a Objetos;
- O projeto deverá possuir uma arquitetura modular, facilitando futuras manutenções e expansões.