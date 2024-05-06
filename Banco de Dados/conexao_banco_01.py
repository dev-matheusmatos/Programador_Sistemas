# conectar com o banco
# pip install mysql-connector-python

# importar biblioteca
# criar conexão
# efetuar transação sql

import mysql.connector

conexao = mysql.connector.connect(
    host='',
    username='',
    password='',
    database=''
)

cursor = conexao.cursor()
sql = '''
INSERT INTO produtos(codigo_barras, descricao, descricao_completa, codigo, peso, um)
VALUES
("7896443138652", "Ventilador de Coluna Mallory", "Ventilador de Coluna Mallory Max Control Com Controle Remoto 140W, Silencioso, Com Hélice de15 pás, Grade Especial em Sistema TS, Máxima Vazão e Mínimo Ruído - PR-GR - 220V", 2222, 5.9, "kg"),
("7908085006814", "Mouse Pad Gamer 700x350x3mm", "Mouse Pad Gamer Extra Grande 700x350x3mm Bordas Costuradas e Base Antiderrapante Exbom MP7035C Mapa MundiCom tamanho diferenciado, este mouse pad tem 70 cm de comprimento, 35 cm de largura e espessura de 3mm, com conforto e praticidade, cabem teclado e mouse juntos.", 11111, 500, "g");
'''

cursor.execute(sql)
conexao.commit()
cursor.close()
conexao.close()
