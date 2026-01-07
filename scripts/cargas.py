import pandas as pd

from backend.constants.arquivos import DICIONARIO_FABRICAS


def carregar_cargas_excel(caminho_arquivo):

    df_relatorio = pd.read_excel(
        caminho_arquivo,
        sheet_name="RELATÓRIO",
        header=4
    )

    df_relatorio = df_relatorio.rename(columns={0: "Transporte"})

    df_relatorio["Cód Fabrica"] = (
        pd.to_numeric(df_relatorio["Cód Fabrica"], errors="coerce")
        .dropna()
        .astype(int)
        .astype(str)
    )

    df_relatorio["Transporte"] = (
        pd.to_numeric(df_relatorio["Transporte"], errors="coerce")
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

    df_relatorio = df_relatorio.dropna(subset=[COL_TRANSPORTE, COL_DATA, COL_CODIGO])
    df_relatorio[COL_QTD] = df_relatorio[COL_QTD].fillna(0).astype(int)




    df_relatorio_1 = pd.read_excel(
        caminho_arquivo,
        sheet_name="RELATÓRIO1",
        header=4
    )

    df_relatorio_1 = df_relatorio_1.rename(columns={0: "Transporte"})

    df_relatorio_1["Transporte"] = (
        pd.to_numeric(df_relatorio_1["Transporte"], errors="coerce")
        .dropna()
        .astype(int)
        .astype(str)
    )

    df_relatorio_1["Motorista"] = df_relatorio_1["Motorista"].astype(str).str.strip()

    mapa_motoristas = (
        df_relatorio_1
        .dropna(subset=["Transporte", "Motorista"])
        .set_index("Transporte")["Motorista"]
        .to_dict()
    )

    mapa_ordens = (
        df_relatorio_1
        .dropna(subset=["Transporte", "Cód Ordens de Carregamento"])
        .set_index("Transporte")["Cód Ordens de Carregamento"]
        .to_dict()
    )



    

    cargas = {}

    for _, row in df_relatorio.iterrows():
        transporte = row[COL_TRANSPORTE]
        data = str(pd.to_datetime(row[COL_DATA]).date())
        origem = DICIONARIO_FABRICAS.get(row[COL_COD_FABRICA], "Não Informado")

        if transporte not in cargas:
            cargas[transporte] = {
                "transporte": transporte,
                "motorista": mapa_motoristas.get(transporte, "Não informado"),
                "ordens": mapa_ordens.get(transporte, "Não Informado"),
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
