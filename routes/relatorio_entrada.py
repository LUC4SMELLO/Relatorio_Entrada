from flask import Blueprint, render_template, jsonify, request
from scripts.cargas import carregar_cargas_excel

from backend.constants.arquivos import CAMINHO_PEDIDOS_EXCEL


cargas = carregar_cargas_excel(CAMINHO_PEDIDOS_EXCEL)


relatorio_entrada_bp = Blueprint("relatorio_entrada", __name__)

@relatorio_entrada_bp.route("/relatorio_entrada", methods=["GET"])
def relatorio_entrada():

    return render_template("relatorio_entrada.html")



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