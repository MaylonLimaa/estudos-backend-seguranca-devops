repetir = True # Booleano

while repetir:
    resp = int(input('Digite a opção: '))

    match resp:
        case 1:
            print('Continuar')
        case 0:
            repetir = False

print('Fim')