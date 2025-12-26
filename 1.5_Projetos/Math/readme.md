# Biblioteca Math – Recriação Total

Este projeto tem como objetivo **recriar toda a biblioteca `math` do Python** utilizando apenas código próprio, sem depender do módulo `math`.  
O foco é **entender a lógica por trás das operações matemáticas**, trabalhar com funções reutilizáveis, loops, condicionais e manipulação de dados.

---

## Descrição do projeto

O projeto visa implementar:

- **Operações básicas:** soma, subtração, multiplicação, divisão.
- **Operações avançadas:** potência, raiz quadrada, fatorial, logaritmo.
- **Funções trigonométricas:** seno, cosseno, tangente.
- **Funções estatísticas:** média, mediana, desvio padrão de listas.

O objetivo é que **todas as funções tenham comportamento semelhante às originais do Python**, mas implementadas do zero.

---

## Operações e funcionalidades

### Operações básicas
- `soma(a, b)` → retorna `a + b`
- `subtracao(a, b)` → retorna `a - b`
- `multiplicacao(a, b)` → retorna `a * b`
- `divisao(a, b)` → retorna `a / b` (com verificação de divisão por zero)

### Operações avançadas
- `potencia(a, b)` → retorna `a ** b`
- `raiz_quadrada(a)` → calcula a raiz quadrada de `a`
- `fatorial(n)` → calcula o fatorial de `n`
- `logaritmo(a, base)` → calcula logaritmo de `a` em relação a `base`

### Funções trigonométricas
- `seno(angle)` → retorna o seno do ângulo (em graus)
- `cosseno(angle)` → retorna o cosseno do ângulo (em graus)
- `tangente(angle)` → retorna a tangente do ângulo (em graus)

### Funções estatísticas
- `media(lista)` → retorna a média dos elementos
- `mediana(lista)` → retorna a mediana dos elementos
- `desvio(lista)` → retorna o desvio padrão da lista

---

## Exemplos de saída

```python
soma(5, 3)           # 8
subtracao(10, 4)     # 6
multiplicacao(3, 7)  # 21
divisao(10, 2)       # 5

potencia(2, 5)       # 32
raiz_quadrada(16)    # 4
fatorial(5)          # 120
logaritmo(8, 2)      # 3.0

seno(90)             # ~1.0
cosseno(0)           # ~1.0
tangente(45)         # ~1.0

lista = [2, 4, 6, 8, 10]
media(lista)         # 6.0
mediana(lista)       # 6
desvio(lista)        # ~2.828
