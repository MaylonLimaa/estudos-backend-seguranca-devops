"""
Validar CPF (com cálculo dos dígitos verificadores)
Receber um CPF (somente números).
Calcular os dois dígitos finais usando a regra oficial.
Dizer se o CPF é válido.
"""

def validarCPF(cpfusuario): # Função para Validar o CPF
    cpfvalidado = [] # Cria uma lista
    contdig = 0 # Contador
    for i in range(0, len(cpfusuario), 1): # Cria um loop com a quantia de caracteres.
        try:
            cpfvalidado.append(int(cpfusuario[i])) # Transforma os números do tipo string em inteiros
        except ValueError: # Caso não seja possível, ignora o número
            continue
    if len(cpfvalidado) != 11: # Verifica se o CPF tem mais de 11 digitos.
        return False 
    for i in range(0, 10, 1): # Inicia dois loops para identificar se o cpf possui todos os digitos iguais
        if contdig == 11:
            return False
        else:
            contdig = 0
        for a in range(0, len(cpfvalidado), 1):
            if cpfvalidado[a] == i:
                contdig += 1
    # Valida o primeiro dígito do CPF
    somad1 = (cpfvalidado[0]*10 + cpfvalidado[1]*9 + cpfvalidado[2]*8 + cpfvalidado[3]*7 + cpfvalidado[4]*6 + cpfvalidado[5]*5 + cpfvalidado[6]*4 + cpfvalidado[7]*3 + cpfvalidado[8]*2) * 10
    if somad1 % 11 == 10:
        d1 = 0
    else:
        d1 = somad1 % 11
    #Valida o segundo digito do CPF
    somad2 = (cpfvalidado[0]*11 + cpfvalidado[1]*10 + cpfvalidado[2]*9 + cpfvalidado[3]*8 + cpfvalidado[4]*7 + cpfvalidado[5]*6 + cpfvalidado[6]*5 + cpfvalidado[7]*4 + cpfvalidado[8]*3 + d1*2) * 10
    if somad2 % 11 == 10:
        d2 = 0
    else:
        d2 = somad2 % 11

    if d1 == cpfvalidado[9] and d2 == cpfvalidado[10]:
        return True
    else:
        return False


cpfcorreto = validarCPF(input('Por gentileza, qual seu CPF: '))
if cpfcorreto == True:
    print('O CPF digitado está correto')
else:
    print('CPF incorreto')