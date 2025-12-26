## Operações do Sistema de Estoque

O programa deve permitir ao usuário executar três operações principais:

### 1. Adicionar produto
- Se o produto já existir, aumenta a quantidade;  
- Se não, adiciona o novo produto.  

Exemplo de uso:  
Operação: adicionar  
Produto: Caneta  
Quantidade: 10  
Preço: 1.5  

Operação: adicionar  
Produto: Caderno  
Quantidade: 2  
Preço: 5.0  

### 2. Remover produto
- Diminui a quantidade de um produto;  
- Se a quantidade chegar a zero, remove do estoque.  

Exemplo de uso:  
Operação: remover  
Produto: Caneta  
Quantidade: 3  

Estoque baixo em: Caderno  

### 3. Gerar relatório
- Imprime todos os produtos, quantidade total e valor total do estoque.  

Exemplo de saída:  
Relatório:  
Produto    Quantidade    Preço    Valor Total  
Caneta       7           1.5        10.5  
Caderno      2           5.0        10.0  

Produto de maior valor total: Caneta  
Produto de menor valor total: Caderno  

### **Bônus de lógica**
- Ao adicionar ou remover produtos, se o estoque de algum produto atingir **menos de 5 unidades**, o programa deve alertar:  
  `"Estoque baixo!"`  
- Ao gerar relatório, também exibir:
  - Produto com **maior valor total** (`quantidade * preco`)  
  - Produto com **menor valor total**
