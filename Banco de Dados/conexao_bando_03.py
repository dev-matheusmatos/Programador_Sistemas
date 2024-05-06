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
("TESTE", "TESTE", "TESTE", "TESTE", 0.00, "kg");
'''
cursor.execute(sql)

sql = 'SELECT * FROM produtos'
cursor.execute(sql)

for linha in cursor.fetchall():
    print(linha)