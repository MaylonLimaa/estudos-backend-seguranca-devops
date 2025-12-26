class Produto:
    """
    A classe produto representa os produtos do sistema
    Cada produto obrigatoriamente deve ser um objeto instanciado de Produto.
    """

    def __init__(self, nome, preco, qtd):
        """
        Método construtor, define oque precisa para o objeto(produto) 
        nascer válido

        :param nome: nome do produto
        :param preco: preço do protuo
        """
        if not nome or nome.isnumeric():
            raise ValueError('Produto não pode ser vazio')
        if preco <= 0:
            raise ValueError('Produto não pode ter preço menor ou igual a zero')
        if qtd <= 0:
            raise ValueError('Produto não pode ter quantidade menor ou igual a zero')

        self.__nome = nome
        self.__preco = preco
        self.__quantidade = qtd
    
    def __str__(self):
        """
        Método especial
        Transforma o objeto em uma string para exibição
        """
        return f'{self.__nome} - Preço: {self.__preco} - Quantidade: {self.__quantidade}'

    def adicionar_produto(self, qtd):
        """
        Método que adiciona um produto em quantidade.

        :param qtd: quantidade do produto
        :param id: referencia o objeto

        não tem retorno
        """
        self.__quantidade += qtd
    def remover_produto(self, qtd):
        """
        Método que remove um produto, em quantidade ou existencia.
        
        :param qtd: quantidade do produto
        :param id: referencia o objeto

        retorna a quantidade que não foi possível subtrair do estoque
        """
        if self.__quantidade < qtd:
            qtd -= self.__quantidade
            self.__quantidade = 0
            return qtd

        self.__quantidade -= qtd
        return 0
