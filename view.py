import sqlite3 as lite
import pandas as pd
from tkinter import filedialog

con = lite.connect('dados.db')

#Criando banco de dados
def criar():
    with con: #abre e fecha bd automaticamente
        cur = con.cursor()
        cur.execute("CREATE TABLE produto(codigo INTEGER PRIMARY KEY , nome VARCHAR(50),modelo VARCHAR(15), fabricante VARCHAR(15), custo DECIMAL(10, 2), quantidade INT, data DATE)")

#Inserindo informações no banco
def inserir_dados(insert):
    with con:
        cur = con.cursor()
        query = "INSERT INTO produto(codigo, nome, modelo, fabricante, custo, quantidade, data) VALUES(?,?, ?, ?, ?, ?, ?)"
        cur.execute(query,insert)

#Acessando os dados existentes
def acessar_dados():
    with con:
        cur = con.cursor()
        query = "SELECT * FROM produto "
        cur.execute(query)
        dados = cur.fetchall() #pegar todos os itens do bd 
        
    return dados       

#Atualizando um produto
def atualizar_dados(insert):
    with con:
        cur = con.cursor()
        query = "UPDATE produto SET nome=?, modelo=? , fabricante=?, custo=?, quantidade=?, data=? WHERE codigo =?"
        cur.execute(query,insert)

#Apagando informações do BD
def deletar_dados(i): 
    with con:
        cur = con.cursor()
        query = "DELETE FROM produto WHERE codigo=?"
        cur.execute(query,i)

#Pesquisando informações do BD
def pesquisar_dados(i):
    lista = []
    with con:
        cur = con.cursor()
        query = f"SELECT * FROM produto WHERE nome LIKE '%{i}%'"
        cur.execute(query)
        dados = cur.fetchall() #pegar todos os itens do bd
        
        for item in dados:
            lista.append(item)    
    return lista

#Exportando para o Excel
def exportar_excel(i):
    
    #abrir a caixa de dialogo para que o usuário escolha onde salvar o arquivo, mantendo a extensão padrão de excel
    local_salvo = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])
    
    with con:
        cur = con.cursor()
        query = f"SELECT * FROM produto WHERE nome LIKE '%{i}%'"
        cur.execute(query)
        dados = cur.fetchall()
        produtos_exportados = pd.DataFrame(dados, columns=['Código','Nome', 'Modelo', 'Fabricante', 'Custo', 'Quantidade', 'Data de Cadastro'])
        produtos_exportados.to_excel(local_salvo)
    
