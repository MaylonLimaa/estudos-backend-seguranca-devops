# Projeto 2 – Sistema de Alunos

Este projeto cria um **Sistema de Controle de Alunos**, permitindo cadastrar, atualizar e consultar informações de estudantes.  
É um projeto **base**, que será escalado futuramente com integração a **API**, **banco de dados** e implementação em **POO**.

## Funcionalidades principais

O programa deve permitir ao usuário realizar operações como:

### 1. Cadastrar aluno
- Informar **nome, idade e notas** do aluno.  
- Se o aluno já existir, o sistema alerta: `"Aluno já cadastrado!"`  

Exemplo de uso:  
Operação: cadastrar  
Nome: Bruno  
Idade: 15  
Notas: 7.5, 8.0, 9.0  

Aluno cadastrado: Bruno

### 2. Atualizar aluno
- Permite atualizar **notas, idade ou nome** de um aluno existente.  
- Se o aluno não existir, o sistema alerta: `"Aluno não encontrado"`

Exemplo de uso:  
Operação: atualizar  
Nome: Bruno  
Nova idade: 16  

Aluno atualizado: Bruno, idade 16

### 3. Consultar aluno
- Mostra as informações de um aluno: nome, idade e notas.  
- Calcula **média das notas** e informa **aprovado ou reprovado** (média ≥ 7 = aprovado).

Exemplo de saída:  
Consulta: Bruno  
Nome: Bruno  
Idade: 16  
Notas: 7.5, 8.0, 9.0  
Média: 8.17  
Status: Aprovado

### 4. Listar todos os alunos
- Mostra todos os alunos cadastrados, suas idades e médias.

Exemplo de saída:  
Alunos cadastrados:  
1. Bruno – Idade: 16 – Média: 8.17  
2. Larissa – Idade: 15 – Média: 6.5  
3. Carlos – Idade: 17 – Média: 7.2

### **Bônus de lógica**
- Validação de dados ao cadastrar ou atualizar alunos (notas entre 0 e 10, idade válida).  
- Preparar para **futuras implementações**:
  - Persistência em **banco de dados**  
  - Criação de **API REST** para cadastro e consulta  
  - Estruturação em **POO**, com classes `Aluno` e `SistemaAlunos`  
  - Geração de **relatórios automáticos** e estatísticas

### **Objetivos de aprendizado**
- Trabalhar **listas e dicionários** para armazenar alunos e notas  
- Manipular **loops e condicionais**  
- Criar **funções** para cada operação (`cadastrar_aluno`, `atualizar_aluno`, `consultar_aluno`, `listar_alunos`)  
- Implementar **validação de dados e lógica de aprovação**  
- Preparar o sistema para **escalabilidade futura**
