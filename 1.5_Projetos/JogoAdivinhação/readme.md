# Projeto 3 – Jogo de Adivinhação com Níveis

Este projeto cria um **jogo de adivinhação**, no qual o usuário deve descobrir um número ou palavra secreta, com níveis de dificuldade variados.

## Funcionalidades principais

O programa deve permitir ao usuário jogar em três níveis:

### 1. Nível fácil
- O jogador tenta adivinhar o número secreto.  
- O sistema informa se o palpite é maior ou menor que o número secreto.  
- O jogador tem tentativas ilimitadas.

Exemplo de uso:  
Número secreto: 42  

Palpite: 50  
Resposta: Menor  

Palpite: 30  
Resposta: Maior  

Palpite: 42  
Resposta: Acertou!  

### 2. Nível médio
- O jogador recebe dicas de **proximidade**: “quente” se estiver perto do número, “frio” se estiver distante.  
- Limite de tentativas: 10.

Exemplo de uso:  
Número secreto: 37  

Palpite: 10  
Resposta: Frio  

Palpite: 35  
Resposta: Quente  

Palpite: 37  
Resposta: Acertou!

### 3. Nível difícil
- Sem dicas, apenas o número secreto informado.  
- Limite de tentativas: 5.

Exemplo de uso:  
Número secreto: 21  

Palpite: 10  
Resposta: Errado  

Palpite: 21  
Resposta: Acertou!

### **Bônus de lógica**
- Permitir **múltiplos jogadores** e registrar pontuações.  
- Criar ranking de vencedores.  
- Preparar para implementação futura em **POO**, como classes `Jogador` e `Jogo`.

### **Objetivos de aprendizado**
- Trabalhar **loops e condicionais**  
- Criar **funções** para cada nível (`jogo_facil`, `jogo_medio`, `jogo_dificil`)  
- Manipular **entradas do usuário** e controlar **tentativas**  
- Implementar **lógica de proximidade e dicas**  