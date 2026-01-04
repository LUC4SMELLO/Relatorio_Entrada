from flask import Blueprint, render_template, jsonify, request
from scripts.cargas import carregar_cargas_excel

from backend.constants.arquivos import CAMINHO_PEDIDOS_EXCEL


cargas = carregar_cargas_excel(CAMINHO_PEDIDOS_EXCEL)


relatorio_entrada_bp = Blueprint("relatorio_entrada", __name__)

@relatorio_entrada_bp.route("/relatorio_entrada", methods=["GET"])
def relatorio_entrada():

    return render_template("relatorio_entrada_2.html")



@relatorio_entrada_bp.route("/relatorio_entrada/opcoes")
def opcoes():
    transportes = sorted(cargas.keys())
    return jsonify({"transportes": transportes})




@relatorio_entrada_bp.route("/relatorio_entrada/carga")
def carga():
    transporte = request.args.get("transporte")
    carga = cargas.get(transporte)

    if not carga:
        return jsonify({"produtos": []})

    return jsonify(carga)


@relatorio_entrada_bp.route("/relatorio_entrada/salvar", methods=["POST"])
def salvar_relatorio():
    dados = request.json

    print("DADOS RECEBIDOS:")
    print(dados)

    transporte = dados["transporte"]

    for produto in dados["produtos"]:
        codigo = produto["codigo"]
        descricao = produto["descricao"]

        for lote in produto["lotes"]:
            quantidade = int(lote["quantidade"])
            estoque = lote["estoque"]
            fabricacao = lote["fabricacao"]
            vencimento = lote["vencimento"]

            alterar_fefo = lote["alterar_fefo"]
            pallet_danificado = lote["pallet_danificado"]
            vazamento = lote["vazamento"]
            observacao = lote["observacao"]

        print(transporte)
        print(codigo)
        print(descricao)
        print(quantidade)
        print(estoque)
        print(fabricacao)
        print(vencimento)
        print(alterar_fefo)
        print(pallet_danificado)
        print(vazamento)
        print(observacao)
    

    # SALVAR NO BANCO DE DADOS

    return jsonify({"status": "ok"})