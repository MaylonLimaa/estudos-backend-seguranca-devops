# 1 – Levantamento de Requisitos

Nesta etapa, foi analisado o que o sistema irá fazer, realizando o levantamento dos requisitos.
Por se tratar de um projeto pequeno e desenvolvido por apenas uma pessoa (eu), este levantamento tem caráter mais didático e simulado, não envolvendo custos de produção, prazos ou restrições externas.

## Funcionalidades do sistema
### Adicionar produto:
- O sistema deve permitir adicionar um produto ao estoque. Caso o produto já exista, a quantidade em estoque deverá ser incrementada.

### Remover produto:
- O sistema deve permitir remover produtos do estoque, decrementando a quantidade. Caso a quantidade chegue a zero, o produto deve ser removido do estoque.

### Relatório:
**O sistema deve gerar um relatório contendo as informações dos produtos cadastrados**. O relatório deve apresentar:

- Dados de todos os produtos
- Produto com maior valor total (quantidade × preço)
- Produto com menor valor total (quantidade × preço)

# 2 – Planejamento

**Nesta etapa foi definido o planejamento de como o sistema irá funcionar, estabelecendo quais elementos serão classes, métodos, atributos, objetos, variáveis e funções.**

Mesmo sendo um projeto pequeno, com poucas classes, optei por seguir um padrão de nomeação e organização semelhante ao de projetos médios ou grandes, com o objetivo de desenvolver boas práticas desde o início.

## Classe Produto
A classe Produto será responsável por representar um produto do sistema.

### Atributos:
- Quantidade em estoque
- Preço

### Métodos
- adicionarProduto()
- removerProduto()

**O produto será instanciado como um objeto.** Após a criação, esse objeto será armazenado em um dicionário que funcionará como base de dados (database).
A variável utilizada para a instanciação poderá ser descartada, mantendo o objeto acessível apenas através do dicionário.

## Comportamento da database
**A database será um dicionário** que armazenará os produtos cadastrados no sistema.
**Cada produto terá um ID único**, gerado automaticamente por meio de um contador.
**O ID será utilizado como chave do dicionário**, e o valor associado será o objeto Produto.

## Classe Relatório
A classe Relatório será responsável por gerar e exibir as informações do sistema.

### Atributos:
- Produto com maior valor total
- Produto com menor valor total
- Lista de produtos

### Método:
- exibirRelatorio()

Essa classe terá um relacionamento de composição com os produtos, pois depende dos dados existentes na database.
Ela receberá o dicionário de produtos para análise, sem controlar o ciclo de vida desses objetos.
