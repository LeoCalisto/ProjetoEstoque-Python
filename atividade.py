from time import sleep


def layout():
    print(' ****************************************** ')
    print(' ***         Bem Vindo ao Simat          ** ')
    print(' ****************************************** ')


def menu():
    print('\n\n\n ************************ ')
    print(' *                      * ')
    print(' *  1 - Cadastrar item  * ')
    print(' *  2 - pesquisar item  * ')
    print(' *  3 - Alterar item    * ')
    print(' *  4 - Excluir item    * ')
    print(' *  0 - SAIR            * ')
    print(' *                      * ')
    print(' ************************ ')


item = {}
estoque = []
val = True

# Apresentação do sistema com menu
layout()
print('\n\nCarregando', end='')
for i in range(0, 5):
    print('.', end='', flush=True)
    sleep(0.5)

# Loop de retono ao menu com validação de opção escolhida
while val == True:
    menu()
    opcao = int(input('Qual opção deseja? '))
    while opcao != 1 and opcao != 2 and opcao != 0 and opcao != 4 and opcao != 3:
        opcao = int(input('Qual opção deseja? '))

    # Escopo de cadastro de atributos do item em um dicionário
    if opcao == 1:
        while True:
            item['nome'] = str(input('\n\nNome do item: '))
            item['modelo'] = str(input('Modelo do item: '))
            item['fabricante'] = str(input('Fabricante do item: '))
            item['valor'] = float(input('Valor do item: '))
            item['quantidade'] = int(input('Qtd do item: '))
            continuar = str(input('\nContinuar cadastrando? S/N'))
            estoque.append(item.copy())
            if continuar in 'Nn':
                break

    # Escopo para retorno de estoque armazenado na lista > dicicionário
    if opcao == 2:
        if len(estoque) == 0:
            print('\nEstoque vazio !!')
            sleep(1)
        else:
            print(f'\n{"Cod"} {"Nome":<15} {"Modelo":<15} {"Fabricante":<15} {"Valor":<15} {"Quantidade":<}')
            for i, item in enumerate(estoque):
                print(
                    f'{i:<3} {item["nome"]:<15} {item["modelo"]:<15} {item["fabricante"]:<15} R$ {item["valor"]:<12} '
                    f'{item["quantidade"]:<}')
            while True:
                escolha = str(input('\n00 - Sair 0 - Retornar ao Menu '))
                if escolha == '00':
                    val = False
                    break
                if escolha == '0':
                    val = True
                    break

    #Escopo para impressão do estoque e escolha do item e atributo a ser alterado diretamente no dict
    if opcao == 3:
        while True:
            print('Itens cadastrados:')
            print(f'\n{"Cod"} {"Nome":<15} {"Modelo":<15} {"Fabricante":<15} {"Valor":<15} {"Quantidade":<}')
            for i, item in enumerate(estoque):
                print(
                    f'{i:<3} {item["nome"]:<15} {item["modelo"]:<15} {item["fabricante"]:<15} R$ {item["valor"]:<12} '
                    f'{item["quantidade"]:<}')
            pos = str(input('\nInforme o código do item: [00 - Menu Principal] '))
            if pos == '00':
                break
            atributo = int(input('Qual atributo quer modificar? 1 -Nome 2-Modelo 3-Fabricante 4-Valor 5-Quantidade '))
            if atributo == 1:
                estoque[int(pos)]['nome'] = str(input('Novo nome: '))
            if atributo == 2:
                estoque[int(pos)]['modelo'] = str(input('Novo Modelo: '))
            if atributo == 3:
                estoque[int(pos)]['fabricante'] = str(input('Novo Fabricante: '))
            if atributo == 4:
                estoque[int(pos)]['valor'] = int(input('Novo Valor: '))
            if atributo == 5:
                estoque[int(pos)]['quantidade'] = int(input('Nova Quantidade: '))

    #Escopo para deletar o conjunto de atributos do produto na lista > dict
    if opcao == 4:

        pos = int(input('Informe o Código do item? '))
        print(f'\n{"Cod"} {"Nome":<15} {"Modelo":<15} {"Fabricante":<15} {"Valor":<15} {"Quantidade"::<}')
        print(
            f'{pos:<3} {estoque[pos]["nome"]:<15} {estoque[pos]["modelo"]:<15} {estoque[pos]["fabricante"]:<15} R$ {estoque[pos]["valor"]:<15} {estoque[pos]["quantidade"]:<12}')
        confirmar = ' '
        while confirmar not in 'SsNn':
            confirmar = str(input('\nConfirmar exlusão? S/N '))
            if confirmar in 'Ss':
                del (estoque[pos])
                print('\nItem Excluido !')
                sleep(1)

    if opcao == 0:
        val = False

print('\nOBRIGADO !!')
