from time import sleep
import mysql.connector

conexao = mysql.connector.connect(host='localhost', user='root', password='m741a123', database='estoque')
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


def alterar(indice, colunas, dado):
    comando = f'UPDATE produto SET {coluna} = "{dado}" WHERE id = {indice}'
    cursor.execute(comando)
    conexao.commit()


def produtos():
    comando = 'SELECT * FROM produto'
    cursor.execute(comando)
    produtos = cursor.fetchall()
    return produtos


val = True

# Apresentação do sistema
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
            nome = str(input('\n\nNome do item: '))
            modelo = str(input('Modelo do item: '))
            fabricante = str(input('Fabricante do item: '))
            while ValueError:
                try:
                    valor = float(input('Valor do item: '))
                except ValueError:
                    print('ERRO com o valor digitado, insira um número positivo')
                else:
                    break
            while ValueError:
                try:
                    quantidade = int(input('Qtd do item: '))
                except ValueError:
                    print('ERRO com o valor digitado, insira um número positivo')
                else:
                    break
            continuar = str(input('\nContinuar cadastrando? S/N'))
            comando = (f'''INSERT INTO produto(nome, fabricante, modelo, VALOR, quantidade) 
                        VALUES ("{nome}", "{modelo}", "{fabricante}", {valor}, {quantidade})''')
            cursor.execute(comando)
            conexao.commit()
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
                print(
                    f'{item[0]:<3} {item[1]:<15} {item[2]:<15} {item[3]:<15} R$ {item[4]:<12} '
                    f'{item[5]:<}')
            while True:
                escolha = str(input('\n00 - Sair 0 - Retornar ao Menu '))
                if escolha == '00':
                    val = False
                    break
                if escolha == '0':
                    break

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
                    print(
                        f'{item[0]:<3} {item[1]:<15} {item[2]:<15} {item[3]:<15} R$ {item[4]:<12} '
                        f'{item[5]:<}')
                cod = int(input('\nInforme o código do item: [00 - Menu Principal] '))
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
            pos = int(input('Informe o Código do item? '))
            print(f'\n{"Cod":<14} {"Nome":<14} {"Modelo":<14} {"Fabricante":<14} {"Valor":<14} {"Quantidade"::<}')
            comando = f'SELECT * FROM produto WHERE id="{pos}"'
            cursor.execute(comando)
            linha = cursor.fetchone()
            for coluna in linha:
                print(f'{coluna:<15}', end='')
            confirmar = ' '
            while confirmar not in 'SsNn':
                confirmar = str(input('\nConfirmar exlusão? S/N '))
                if confirmar in 'Ss':
                    comando = f'DELETE FROM produto WHERE id = {pos}'
                    cursor.execute(comando)
                    conexao.commit()
                    print('\nItem Excluido !')
                    sleep(1)

    if opcao == 0:
        val = False

conexao.close()
print('\nOBRIGADO !!')
