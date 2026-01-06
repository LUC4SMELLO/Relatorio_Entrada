import sqlite3

from backend.constants.banco_dados import BANCO_DADOS_RELATORIOS_TEMPORARIOS, TABELA_RELATORIOS_TEMPORARIOS


def conectar_banco_dados_relatorios_temporarios():

    return sqlite3.connect(BANCO_DADOS_RELATORIOS_TEMPORARIOS)

def criar_tabela_relatorios_temporarios():

    conexao = conectar_banco_dados_relatorios_temporarios()
    cursor = conexao.cursor()

    cursor.execute(
    f"""
    CREATE TABLE IF NOT EXISTS {TABELA_RELATORIOS_TEMPORARIOS} (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id TEXT UNIQUE,
    dados_json TEXT,
    data_atualizacao TEXT
    )
    """
    )

    conexao.commit()
    conexao.close()
