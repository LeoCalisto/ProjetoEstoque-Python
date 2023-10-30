import sqlite3 as lite

con = lite.connect('dados.db')
#inserir informações no Bd

def criar():
    with con: #abre e fecha bd automaticamente
        cur = con.cursor()
        cur.execute("CREATE TABLE produto(codigo INTEGER PRIMARY KEY , nome VARCHAR(50),modelo VARCHAR(15), fabricante VARCHAR(15), custo DECIMAL(10, 2), quantidade INT, data DATE)")

def inserir_dados(insert):
    with con:
        cur = con.cursor()
        query = "INSERT INTO produto(codigo, nome, modelo, fabricante, custo, quantidade, data) VALUES(?,?, ?, ?, ?, ?, ?)"
        cur.execute(query,insert)

def acessar_dados():
    with con:
        cur = con.cursor()
        query = "SELECT * FROM produto "
        cur.execute(query)
        dados = cur.fetchall() #pegar todos os itens do bd 
        
    return dados       

def atualizar_dados(insert):
    with con:
        cur = con.cursor()
        query = "UPDATE produto SET nome=?, modelo=? , fabricante=?, custo=?, quantidade=?, data=? WHERE codigo =?"
        cur.execute(query,insert)

def deletar_dados(i): 
    with con:
        cur = con.cursor()
        query = "DELETE FROM produto WHERE codigo=?"
        cur.execute(query,i)

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
