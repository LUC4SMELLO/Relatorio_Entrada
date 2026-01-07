from flask import Blueprint, render_template, jsonify, request, session, url_for
import json

from scripts.cargas import carregar_cargas_excel

from backend.constants.arquivos import CAMINHO_PEDIDOS_EXCEL

from backend.models.relatorios import Relatorio
from backend.models.relatorios_temporarios import RelatoriosTemporarios


cargas = carregar_cargas_excel(CAMINHO_PEDIDOS_EXCEL)


relatorio_entrada_bp = Blueprint("relatorio_entrada", __name__)

@relatorio_entrada_bp.route("/relatorio_entrada", methods=["GET"])
def relatorio_entrada():

    return render_template("relatorio_entrada.html")

@relatorio_entrada_bp.route("/relatorio_entrada/visualizar_relatorios", methods=["GET"])
def visualizar_relatorios():

    return "Em construção...."


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

@relatorio_entrada_bp.route("/relatorio_entrada/exibir_mensagem_salvamento", methods=["GET"])
def exibir_mensagem_salvamento():

    return render_template("salvar_relatorio.html")


@relatorio_entrada_bp.route("/relatorio_entrada/salvar", methods=["POST"])
def salvar_relatorio():
    dados = request.json


    usuario_id = session.get("usuario_id")
    nome_usuario = session.get("username")

    transporte = dados["transporte"]

    data_envio_relatorio = dados["data_envio_relatorio"]

    data_prevista_carga = dados["data_prevista_carga"]

    motorista = dados["nome_motorista"]

    origem = dados["origem"]

    ordens = dados["ordens"]

    for produto in dados["produtos"]:
        codigo_produto = produto["codigo"]
        descricao = produto["descricao"]

        for lote in produto["lotes"]:

            quantidade = int(lote.get("quantidade") or 0)
            estoque = lote["estoque"]
            fabricacao = lote["fabricacao"]
            vencimento = lote["vencimento"]

            alterar_fefo = lote["alterar_fefo"]
            pallet_danificado = lote["pallet_danificado"]
            vazamento = lote["vazamento"]
            observacao = lote["observacao"]


            novo_relatorio = Relatorio(
                transporte=transporte,
                origem=origem,
                ordens=ordens,
                usuario_id=usuario_id,
                nome_usuario=nome_usuario,
                data_relatorio=data_envio_relatorio,
                data_carga=data_prevista_carga,
                codigo_produto=codigo_produto,
                quantidade=quantidade,
                data_estoque=estoque,
                data_fabricacao=fabricacao,
                data_vencimento=vencimento,
                alterar_fefo=alterar_fefo,
                pallet_danificado=pallet_danificado,
                vazamento=vazamento,
                observacao=observacao
            )
            novo_relatorio.inserir_relatorio()
        
    RelatoriosTemporarios.excluir(usuario_id)


    return jsonify({"status": "sucesso", "url": url_for('relatorio_entrada.exibir_mensagem_salvamento')}), 200


@relatorio_entrada_bp.route("/relatorio_entrada/salvar_rascunho", methods=["POST"])
def salvar_rascunho():
    usuario = session.get("usuario_id")
    dados = request.json

    RelatoriosTemporarios.salvar(usuario, dados)

    return {"status": "ok"}

@relatorio_entrada_bp.route("/relatorio_entrada/carregar_rascunho", methods=["GET"])
def carregar_rascunho():
    usuario = session.get("usuario_id")
    rascunho = RelatoriosTemporarios.buscar(usuario)

    if not rascunho:
        return {"existe": False}

    return {
        "existe": True,
        "dados": rascunho
    }