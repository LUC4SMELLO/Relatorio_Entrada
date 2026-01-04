from flask import Blueprint, render_template


selecionar_opcoes_bp = Blueprint("selecionar_opcoes", __name__)

@selecionar_opcoes_bp.route("/selecionar_opcoes", methods=["GET"])
def selecionar_opcoes():

    return render_template("selecionar_opcoes.html")