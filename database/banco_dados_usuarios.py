import sqlite3

from backend.constants.banco_dados import BANCO_DADOS_USUARIOS, TABELA_USUARIOS

def conectar_banco_dados_usuarios():

    return sqlite3.connect(BANCO_DADOS_USUARIOS)

def criar_tabela_usuarios():

    conexao = conectar_banco_dados_usuarios()
    cursor = conexao.cursor()

    cursor.execute(
    f"""
    CREATE TABLE IF NOT EXISTS {TABELA_USUARIOS} (
    usuario_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_completo VARCHAR(50),
    senha VARCHAR(50)
    )
    """
    )

    conexao.commit()
    conexao.close()