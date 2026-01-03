import pandas as pd


def carregar_cargas_excel(caminho_arquivo):
    df = pd.read_excel(
        caminho_arquivo,
        sheet_name="RELATÓRIO",
        header=4
    )


    # df = df.loc[:, ~df.columns.isna()]
    # df.columns = df.columns.str.strip()


    df = df.rename(columns={0: "Transporte"})


    df["Transporte"] = (
        pd.to_numeric(df["Transporte"], errors="coerce")
        .dropna()
        .astype(int)
        .astype(str)
    )

    COL_TRANSPORTE = "Transporte"
    COL_DATA = "Data entrega"
    COL_CODIGO = "Código"
    COL_QTD = "Quant"
    COL_DESC = "Descrição"


    df = df.dropna(subset=[COL_TRANSPORTE, COL_DATA, COL_CODIGO])
    df[COL_QTD] = df[COL_QTD].fillna(0).astype(int)


    cargas = {}

    for _, row in df.iterrows():
        transporte = row[COL_TRANSPORTE]
        data = str(pd.to_datetime(row[COL_DATA]).date())

        if transporte not in cargas:
            cargas[transporte] = {
                "transporte": transporte,
                "data": data,
                "produtos": []
            }

        cargas[transporte]["produtos"].append({
            "codigo": row[COL_CODIGO],
            "descricao": row[COL_DESC],
            "quant": row[COL_QTD]
        })

    return cargas
