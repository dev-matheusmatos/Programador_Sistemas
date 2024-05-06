# conectar com o banco
# pip install mysql-connector-python

# importar biblioteca
# criar conexão
# efetuar transação sql

import mysql.connector

conexao = mysql.connector.connect(
    host='LocalHost',
    username='root',
    password='',
    database='Loja'
)

cursor = conexao.cursor()
sql = '''
INSERT INTO produtos(codigo_barras, descricao, descricao_completa, codigo, peso, um)
VALUES
("TESTE", "TESTE", "TESTE", TESTE, 0.00, "kg");
'''

cursor.execute(sql)
conexao.commit()
cursor.close()
conexao.close()


