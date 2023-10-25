from time import sleep
import sqlite3

conexao = sqlite3.connect("estoque.db")
cursor = conexao.cursor()


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


def consultaId(referencia):
    comando = f'SELECT id FROM produto WHERE id = "{referencia}"'
    cursor.execute(comando)
    ids = cursor.fetchone()
    return ids


def alterar(indice, colunas, dado):
    comando = f'UPDATE produto SET {colunas} = "{dado}" WHERE id = {indice}'
    cursor.execute(comando)
    conexao.commit()


def produtos():
    comando = 'SELECT * FROM produto'
    cursor.execute(comando)
    produtos = cursor.fetchall()
    return produtos


try:
    comando = f'CREATE TABLE produto(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(50), modelo VARCHAR(15), fabricante VARCHAR(15), VALOR DECIMAL(10, 2), quantidade INT)'
    cursor.execute(comando)
    conexao.commit()
except sqlite3.OperationalError:

    val = True

    # Apresentação do sistema
    layout()
    print('\n\nCarregando', end='')
    for i in range(0, 5):
        print('.', end='', flush=True)
        sleep(0.5)
    # Loop principal de retono ao menu inicial
    while val == True:
        menu()
        # Validação de opção escolhida apresentando erro interpretado ao inserir str ou espaços
        while True:
            try:
                opcao = int(input('Qual opção deseja? '))
            except ValueError:
                print('Número invalido, digite apenas inteiros positivos')
            else:
                if -1 < opcao < 5:
                    break
                else:
                    print('\nNúmero não se encontra no menu')
                    continue

        # Escopo de cadastro do intem no BD
        if opcao == 1:
            # Loop para continuação de multiplos cadastros
            while True:
                nome = str(input('\n\nNome do item: '))
                modelo = str(input('Modelo do item: '))
                fabricante = str(input('Fabricante do item: '))
                # Validação de dado compativel com float/ int em valor e quantidade do item
                while True:
                    try:
                        valor = float(input('Valor do item: '))
                    except ValueError:
                        print('ERRO com o valor digitado, insira um número positivo')
                    else:
                        break
                while True:
                    try:
                        quantidade = int(input('Qtd do item: '))
                    except ValueError:
                        print('ERRO com o valor digitado, insira um número positivo')
                    else:
                        break
                # Comando SQL para iserção do dado no BD
                comando = (f'''INSERT INTO produto(nome, fabricante, modelo, VALOR, quantidade) 
                            VALUES ("{nome}", "{modelo}", "{fabricante}", {valor}, {quantidade})''')
                cursor.execute(comando)
                conexao.commit()
                # Confirmação de continuação do cadastro
                continuar = str(input('\nContinuar cadastrando? S/N'))
                if continuar in 'Nn':
                    break

        # Escopo para retorno de estoque armazenado na lista > dicicionário
        if opcao == 2:
            if len(produtos()) == 0:
                print('\nEstoque vazio !!')
                sleep(1)
            else:
                print(f'\n{"Cod"} {"Nome":<15} {"Modelo":<15} {"Fabricante":<15} {"Valor":<15} {"Quantidade":<}')
                for item in produtos():
                    print(f'{item[0]:<3} {item[1]:<15} {item[2]:<15} {item[3]:<15} R$ {item[4]:<12} {item[5]:<}')
                while True:
                    escolha = int(input('\n0 - Sair 1 - Retornar ao Menu '))
                    if escolha == 0:
                        val = False
                        break
                    if escolha == 1:
                        break
                    print('\nValor digitado não corresponde, digite apenas 0 ou 1.')

        # Escopo para impressão do estoque e escolha do item e atributo a ser alterado diretamente no dict
        if opcao == 3:
            if len(produtos()) == 0:
                print('\nEstoque vazio !!')
                sleep(1)
            else:
                while True:
                    print('Itens cadastrados:')
                    print(f'\n{"Cod"} {"Nome":<15} {"Modelo":<15} {"Fabricante":<15} {"Valor":<15} {"Quantidade":<}')
                    for item in produtos():
                        print(f'''
                            {item[0]:<3} {item[1]:<15} {item[2]:<15} {item[3]:<15} R$ {item[4]:<12}
                            {item[5]:<}''')
                    while True:
                        try:
                            cod = int(input('\nInforme o código do item: [0 - Menu Principal] '))
                        except ValueError:
                            print('Valor digitado é inválido, insira um número inteiro positivo')
                            continue
                        if cod == 0:
                            break
                        if consultaId(cod) is None:
                            print('\nCódigo não encontrado !')
                            continue
                        else:
                            break
                    if cod == 0:
                        break
                    atributo = int(
                        input('Qual atributo quer modificar? 1 -Nome 2-Modelo 3-Fabricante 4-Valor 5-Quantidade '))
                    if atributo == 1:
                        novonome = str(input('Novo nome: '))
                        alterar(cod, "nome", novonome)

                    if atributo == 2:
                        modelo = str(input('Novo modelo: '))
                        alterar(cod, "modelo", modelo)

                    if atributo == 3:
                        fabricante = str(input('Novo Fabricante: '))
                        alterar(cod, "fabricante", fabricante)

                    if atributo == 4:
                        valor = float(input('Novo Valor: '))
                        alterar(cod, "VALOR", valor)

                    if atributo == 5:
                        quantidade = int(input('Nova Quantidade: '))
                        alterar(cod, "quantidade", quantidade)

        # Escopo para deletar o conjunto de atributos do produto na lista > dict
        if opcao == 4:
            if len(produtos()) == 0:
                print('\nEstoque vazio !!')
                sleep(1)
            else:
                ref = int(input('Informe o Código do item? '))
                print(f'\n{"Cod":<14} {"Nome":<14} {"Modelo":<14} {"Fabricante":<14} {"Valor":<14} {"Quantidade"::<}')
                comando = f'SELECT * FROM produto WHERE id="{ref}"'
                cursor.execute(comando)
                linha = cursor.fetchone()
                for coluna in linha:
                    print(f'{coluna:<15}', end='')
                confirmar = ' '
                while confirmar not in 'SsNn':
                    confirmar = str(input('\nConfirmar exlusão? S/N '))
                    if confirmar in 'Ss':
                        comando = f'DELETE FROM produto WHERE id = {ref}'
                        cursor.execute(comando)
                        conexao.commit()
                        print('\nItem Excluido !')
                        sleep(1)
        if opcao == 0:
            val = False
    conexao.close()
    print('\nVolte Sempre !!')
