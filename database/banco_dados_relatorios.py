import sqlite3

from backend.constants.banco_dados import BANCO_DADOS_RELATORIOS, TABELA_RELATORIOS


def conectar_banco_dados_relatorios():

    return sqlite3.connect(BANCO_DADOS_RELATORIOS)

def criar_tabela_relatorios():

    conexao = conectar_banco_dados_relatorios()
    cursor = conexao.cursor()

    cursor.execute(
    f"""
    CREATE TABLE IF NOT EXISTS {TABELA_RELATORIOS} (
    transporte INTERGER PRIMARY KEY,
    usuario_id VARCHAR(10),
    nome_usuario VARCHAR(250),
    data_relatorio VARCHAR(10),
    data_carga VARCHAR(10),
    codigo_produto VARCHAR(10),
    quantidade INTERGER,
    data_estoque VARCHAR(10),
    data_fabricacao VARCHAR(10),
    data_vencimento VARCHAR(10),
    alterar_fefo VARCHAR(5),
    pallet_danificado VARCHAR(5),
    vazamento VARCHAR(5),
    observacao VARCHAR(250)
    )
    """
    )

    conexao.commit()
    conexao.close()
