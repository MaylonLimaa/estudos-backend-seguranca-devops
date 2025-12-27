"""
Arquivo principal do sistema estoque
"""

import services

def main():
    """
    Função principal de menu
    """
    estoque = {}
    cont = 0
    while True:
        print("\n" + "="*40)
        print("   SISTEMA DE ESTOQUE - MENU PRINCIPAL")
        print("="*40)
        print("1 - Cadastrar produto")
        print("2 - Adicionar quantidade a um produto")
        print("3 - Remover quantidade de um produto")
        print("4 - Ver IDs dos produtos")
        print("5 - Exibir relatório do estoque")
        print("0 - Sair")
        print("="*40)

        try:
            escolha = int(input("Escolha uma opção: "))
            if escolha == 0:
                # Digitar duas vezes o valor para evitar sair por engano
                escolha = int(input('Digite 0 novamente para confirmar que deseja sair: '))
                if escolha != 0:
                    continue
        except ValueError:
            print("Digite um número válido!")
            continue

        match escolha:
            # Optei por usar match ao invés de elif devido a simplicidade
            case 1:
                cont = services.cadastro(estoque, cont)
            case 2:
                services.adicionar(estoque, cont)
            case 3:
                services.remover(estoque)
            case 4:
                services.ver_id(estoque)
            case 5:
                services.exibir_relat(estoque)
            case 0:
                break

if __name__ == "__main__":
    main()
