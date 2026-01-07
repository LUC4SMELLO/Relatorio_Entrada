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
        transporte INTEGER,
        origem VARCHAR(50),
        ordens VARCHAR(250),
        usuario_id VARCHAR(10),
        nome_usuario VARCHAR(250),
        data_relatorio VARCHAR(10),
        data_carga VARCHAR(10),
        codigo_produto VARCHAR(10),
        quantidade INTEGER,
        data_estoque VARCHAR(10),
        data_fabricacao VARCHAR(10),
        data_vencimento VARCHAR(10),
        alterar_fefo VARCHAR(5),
        pallet_danificado VARCHAR(5),
        vazamento VARCHAR(5),
        observacao VARCHAR(250),
        

        -- 1. SHELF LIFE (Vencimento - Fabricação)
        shelf_life INTEGER GENERATED ALWAYS AS (
            julianday(substr(data_vencimento, 7, 4) || '-' || substr(data_vencimento, 4, 2) || '-' || substr(data_vencimento, 1, 2)) -
            julianday(substr(data_fabricacao, 7, 4) || '-' || substr(data_fabricacao, 4, 2) || '-' || substr(data_fabricacao, 1, 2))
        ) VIRTUAL,

        -- 2. DIAS PARA VENCIMENTO (Vencimento - Chegada/Estoque)
        dias_para_vencimento INTEGER GENERATED ALWAYS AS (
            julianday(substr(data_vencimento, 7, 4) || '-' || substr(data_vencimento, 4, 2) || '-' || substr(data_vencimento, 1, 2)) -
            julianday(substr(data_relatorio, 7, 4) || '-' || substr(data_relatorio, 4, 2) || '-' || substr(data_relatorio, 1, 2))
        ) VIRTUAL,

        -- 3. % DIAS VENCIMENTO (Dias p/ Vencer - Shelf Life * 100)
        percentual_dias_vencimento REAL GENERATED ALWAYS AS (
        ROUND(
            ABS(
                ((julianday(substr(data_vencimento, 7, 4) || '-' || substr(data_vencimento, 4, 2) || '-' || substr(data_vencimento, 1, 2)) -
                  julianday(substr(data_relatorio, 7, 4) || '-' || substr(data_relatorio, 4, 2) || '-' || substr(data_relatorio, 1, 2))) * 100.0) /
                NULLIF(
                    julianday(substr(data_vencimento, 7, 4) || '-' || substr(data_vencimento, 4, 2) || '-' || substr(data_vencimento, 1, 2)) -
                    julianday(substr(data_fabricacao, 7, 4) || '-' || substr(data_fabricacao, 4, 2) || '-' || substr(data_fabricacao, 1, 2)), 
                0)
            ), 
        2) -- O número 2 define as casas decimais
    ) VIRTUAL
    )
    """
    )

    conexao.commit()
    conexao.close()
