listaItens = []

def validaInt(pergunta):
    while True:
        try:
            valida = int(input(pergunta))
        except ValueError:
            print('Valor não inteiro, tente novamente: ')
            continue
        else:
            return valida

def cadastrarItem(codigo):

    try:
        print('Bem vindo ao cadastro de peças.')
        print('Número da nova peça a ser cadastrada é: {}'.format(registroItem))
        nome = input("Digite o nome da peça: ")
        fabricante = input("Digite o fabricante da peça: ")
        valor = float(input("Digite o valor da peça: "))
    except ValueError:
        print('Valores incorretos, tente novamente.')
        return
    else:
        dicionarioItem = {'codigo'      : codigo,
                          'nome'        : nome,
                          'fabricante'  : fabricante,
                          'valor'       : valor}
        listaItens.append(dicionarioItem.copy())




def consultarItem():
    while True:
        print('<< Bem vindo a consulta de peças >>')
        opConsulta = validaInt('Digite a opção desejada      \n'
                               '1- Consultar todas as peças. \n'
                               '2- Consultar por código.     \n'
                               '3- Consultar por Fabricante  \n'
                               '4- Retornar ao menu anterior \n'
                               '>>')

        if opConsulta == 1:
            print("Bem vindo ao consultar TODOS.")
            for item in listaItens:
                for key, value in item.items():
                    print("{} : {}".format(key, value))
                print()

        elif opConsulta == 2:
            verificador = 0
            print("Bem vindo a consulta por código.")
            entrada = validaInt("Digite o código desejado.")
            for item in listaItens:
                if item['codigo'] == entrada:
                    for key, value in item.items():
                        print("{} : {}".format(key, value))
                        verificador += 1
            if not verificador:
                print('Valor incorreto, tente novamente')
                continue

            print()

        elif opConsulta == 3:
            verificador = 0
            print("Bem vindo a consulta por fabricante.")
            entrada = input("Digite o fabricante desejado: ")
            for item in listaItens:
                if item['fabricante'] == entrada:
                    for key, value in item.items():
                        print("{} : {}".format(key, value))
                        verificador += 1
            if not verificador:
                print('Valor incorreto, tente novamente')
                continue

            print()

        elif opConsulta == 4:
            return

        else:
            print('Opção inválida, tente novamente.')
            continue

def removerItem():
    print('Bem vindo ao REMOVER peças')
    entrada = validaInt("Digite o código da peça a ser removida: ")
    for item in listaItens:
        if (item['codigo'] == entrada):
            listaItens.remove(item)
print('Bem vindo ao Controle de Estoque da Bicicletaria de Cristiano Godoy. ')
registroItem = 0

while True:
    opcao = validaInt("Digite a opção desejada:   \n"
                      "1- Cadastrar Peça.    \n"
                      "2- Consultar Peça.    \n"
                      "3- Remover Peça.      \n"
                      "4- SAIR. "
                       "\n>>")

    if opcao == 1:
        registroItem += 1
        cadastrarItem(registroItem)
    elif opcao == 2:
        consultarItem()
    elif opcao == 3:
        removerItem()
    elif opcao == 4:
        print('Programa se auto destruindo...')
        break
    else:
        print('Digite alguma opção do menu.')
        continue

