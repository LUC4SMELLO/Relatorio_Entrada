import pandas as pd

from backend.constants.arquivos import DICIONARIO_FABRICAS


def carregar_cargas_excel(caminho_arquivo):

    df_produtos = pd.read_excel(
        caminho_arquivo,
        sheet_name="RELATÓRIO",
        header=4
    )

    df_produtos = df_produtos.rename(columns={0: "Transporte"})

    df_produtos["Cód Fabrica"] = (
        pd.to_numeric(df_produtos["Cód Fabrica"], errors="coerce")
        .dropna()
        .astype(int)
        .astype(str)
    )

    df_produtos["Transporte"] = (
        pd.to_numeric(df_produtos["Transporte"], errors="coerce")
        .dropna()
        .astype(int)
        .astype(str)
    )

    COL_TRANSPORTE = "Transporte"
    COL_DATA = "Data entrega"
    COL_CODIGO = "Código"
    COL_QTD = "Quant"
    COL_DESC = "Descrição"
    COL_COD_FABRICA = "Cód Fabrica"

    df_produtos = df_produtos.dropna(subset=[COL_TRANSPORTE, COL_DATA, COL_CODIGO])
    df_produtos[COL_QTD] = df_produtos[COL_QTD].fillna(0).astype(int)




    df_motorista = pd.read_excel(
        caminho_arquivo,
        sheet_name="RELATÓRIO1",
        header=4
    )

    df_motorista = df_motorista.rename(columns={0: "Transporte"})

    df_motorista["Transporte"] = (
        pd.to_numeric(df_motorista["Transporte"], errors="coerce")
        .dropna()
        .astype(int)
        .astype(str)
    )

    df_motorista["Motorista"] = df_motorista["Motorista"].astype(str).str.strip()

    mapa_motoristas = (
        df_motorista
        .dropna(subset=["Transporte", "Motorista"])
        .set_index("Transporte")["Motorista"]
        .to_dict()
    )



    

    cargas = {}

    for _, row in df_produtos.iterrows():
        transporte = row[COL_TRANSPORTE]
        data = str(pd.to_datetime(row[COL_DATA]).date())
        origem = DICIONARIO_FABRICAS.get(row[COL_COD_FABRICA], "Não Informado")

        if transporte not in cargas:
            cargas[transporte] = {
                "transporte": transporte,
                "motorista": mapa_motoristas.get(transporte, "Não informado"),
                "data": data,
                "origem": origem,
                "produtos": []
            }

        cargas[transporte]["produtos"].append({
            "codigo": row[COL_CODIGO],
            "descricao": row[COL_DESC],
            "quant": row[COL_QTD]
        })

    return cargas
