"""
Arquivo de estudo para Programação Orientada a Objetos (POO) em Python.

Objetivos:
1. Reforçar o entendimento sobre classes, métodos e atributos.
2. Aplicar encapsulamento (atributos públicos, protegidos e privados).
3. Demonstrar relacionamentos entre classes:
   - Associação
   - Agregação
   - Composição

OBS: Este arquivo tem foco DIDÁTICO.
Não é um código de produção, e sim um bloco de notas conceitual.
"""

# =========================
# CLASSE CLIENTE
# =========================

class Cliente:
    """
    Representa um cliente do sistema.

    Relacionamentos:
    - Composição com Pedido:
      Um pedido NÃO EXISTE sem um cliente.
      Todo pedido pertence obrigatoriamente a um cliente.

    - Associação com Produto:
      O cliente interage com produtos (visualiza, compra),
      mas não depende diretamente deles para existir.
    """

    def __init__(self, nome, cpf, telefone):
        self.nome = nome              # atributo público (pode ser acessado livremente)
        self.__cpf = cpf              # atributo privado (não deve ser acessado fora da classe)
        self._telefone = telefone     # atributo protegido (uso interno / subclasses)

        # Lista de pedidos do cliente
        # Aqui o cliente "possui" pedidos → composição
        self.vendas = []

    def comprar(self, produto, qtd):
        """
        Método que representa a ação de compra do cliente.

        Aqui ocorre:
        - Associação: o cliente recebe um Produto existente
        - Composição: o cliente CRIA um Pedido
        """

        # Cria um pedido usando um objeto Produto já existente
        # Pedido depende do cliente → composição
        pedido = Pedido(cliente=self, produto=produto, quantidade=qtd)

        # Guarda o pedido dentro do cliente
        self.vendas.append(pedido)


# =========================
# CLASSE PRODUTO
# =========================

class Produto:
    """
    Representa um produto do sistema.

    Relacionamentos:
    - Agregação com Pedido:
      O produto pode estar em um pedido,
      mas continua existindo mesmo sem pedidos.

    - Associação com Cliente:
      Clientes podem interagir com produtos,
      mas o produto não depende de clientes para existir.
    """

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


# =========================
# CLASSE PEDIDO
# =========================

class Pedido:
    """
    Representa um pedido feito por um cliente.

    Relacionamentos:
    - Composição com Cliente:
      Um pedido NÃO EXISTE sem cliente.
      Se o cliente deixar de existir, o pedido perde sentido.

    - Agregação com Produto:
      O pedido referencia um produto existente,
      mas não é dono do produto.
    """

    def __init__(self, cliente, produto, quantidade):
        self.cliente = cliente        # referência a um objeto Cliente (composição)
        self.produto = produto        # referência a um objeto Produto (agregação)
        self.quantidade = quantidade


# =========================
# USO DO CÓDIGO (EXEMPLO)
# =========================

# Cria um cliente (objeto independente)
p1 = Cliente("Maylon", "123.123.123-12", "11 99999-9999")

# Cria produtos (objetos independentes)
pdt001 = Produto("Água", 2.5)
pdt002 = Produto("Refrigerante", 5.0)

# Cliente compra um produto já existente
# - Produto entra por AGREGRAÇÃO
# - Pedido é criado por COMPOSIÇÃO
p1.comprar(pdt001, 2)

# Neste ponto:
# - Cliente existe sem pedido ✔
# - Produto existe sem pedido ✔
# - Pedido NÃO existe sem cliente ✖
