# Modelo Conceitual - Sistema Acadêmico
## Objetivo
O sistema possui um objetivo de gerenciar as notas dos alunos nas respectivas matérias.

## Entidades
### Aluno
Representa um Aluno cadastrado no sistema.
- Nome
- CPF
- E-mail
- Status
- Matricula

### Professor
Representa um Professor cadastrado no sistema.
- Nome
- CPF
- E-mail
- Status
- Matricula

### Matéria
Representa uma matéria lecionada no sistema.
- Nome
- idmateria

### Notas
- Matricula do Aluno
- Id da Matéria
- Notas do Aluno

## Relacionamentos
- Aluno pode aprender diversas matérias.
- Professor pode ser responsável por mais de uma matéria.

## Regras de Negócio
- Para o aluno ser considerado estudando a matéria ele deve ter uma nota atribuída aquela matéria.
- Cada CPF deverá ser único;
- Cada matrícula deverá ser única;
- Não será permitido o cadastro de registros duplicados;
- O e-mail deverá possuir um formato válido.
- Cada Aluno e Professor deve ter pelo menos Nome, CPF, Matricula e E-mail.
- Notas não podem existir sem matéria.
- Notas não podem existir sem aluno.