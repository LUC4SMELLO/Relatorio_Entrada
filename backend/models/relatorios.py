from database.banco_dados_relatorios import conectar_banco_dados_relatorios

from backend.constants.banco_dados import TABELA_RELATORIOS


class Relatorio:
    """
    Representa um relatório.

    Attributes
    ----------
        transporte : str
            O número do transporte.
        usuario_id : str
            O id do usuário que preencheu o relatório.
        nome_usuario : str
            O nome do usuário que preencheu o relatório.
        data_relatório : str
            A data que o relatório foi enviado.
        data_carga : str
            A data prevista para a carga chegar.
        codigo_produto : str
            O código do produto.
        quantidade : str
            A quantidade do produto
        data_estoque : str
            A data vencimento do produto em estoque.
        data_fabricacao : str
            A data de fabricação do produto que chegou na carga.
        data_vencimento : str
            A data de vencimento do produto que chegou na carga.
        alterar_fefo : str
            Necessidade de alterar FEFO ou não.
        pallet_danificado : str
            Indica se o pallet veio quebrado / danificado da carga.
        vazamento : str
            Mostra se houve vazamento de produto da carga.
        observacao : str
            Alguma observação feita pelo usuário.


    """

    def __init__(
            self,
            transporte: str,
            origem : str,
            usuario_id: str,
            nome_usuario: str,
            data_relatorio: str,
            data_carga: str,
            codigo_produto: str,
            quantidade: str,
            data_estoque: str,
            data_fabricacao: str,
            data_vencimento: str,
            alterar_fefo: str,
            pallet_danificado: str,
            vazamento: str,
            observacao: str
    ):
        """
        Inicializa um novo objeto relatório.

        Parameters
        ----------
            transporte : str
                O número do transporte.
            origem : str
                A origem da carga.
            usuario_id : str
                O id do usuário que preencheu o relatório.
            nome_usuario : str
                O nome do usuário que preencheu o relatório.
            data_relatório : str
                A data que o relatório foi enviado.
            data_carga : str
                A data prevista para a carga chegar.
            codigo_produto : str
                O código do produto.
            quantidade : str
                A quantidade do produto
            data_estoque : str
                A data vencimento do produto em estoque.
            data_fabricacao : str
                A data de fabricação do produto que chegou na carga.
            data_vencimento : str
                A data de vencimento do produto que chegou na carga.
            alterar_fefo : str
                Necessidade de alterar FEFO ou não.
            pallet_danificado : str
                Indica se o pallet veio quebrado / danificado da carga.
            vazamento : str
                Mostra se houve vazamento de produto da carga.
            observacao : str
                Alguma observação feita pelo usuário.
        """
        self.transporte = transporte
        self.origem = origem
        self.usuario_id = usuario_id
        self.nome_usuario = nome_usuario
        self.data_relatorio = data_relatorio
        self.data_carga = data_carga
        self.codigo_produto = codigo_produto
        self.quantidade = quantidade
        self.data_estoque = data_estoque
        self.data_fabricacao = data_fabricacao
        self.data_vencimento =data_vencimento 
        self.alterar_fefo = alterar_fefo
        self.pallet_danificado = pallet_danificado
        self.vazamento = vazamento
        self.observacao = observacao

    def inserir_relatorio(self):
        """Insere um novo relatório no banco de dados."""

        conexao = conectar_banco_dados_relatorios()
        cursor = conexao.cursor()

        cursor.execute(
            f"""
            INSERT INTO {TABELA_RELATORIOS} (
            transporte,
            origem,
            usuario_id,
            nome_usuario,
            data_relatorio,
            data_carga,
            codigo_produto,
            quantidade,
            data_estoque,
            data_fabricacao,
            data_vencimento,
            alterar_fefo,
            pallet_danificado,
            vazamento,
            observacao
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                self.transporte,
                self.origem,
                self.usuario_id,
                self.nome_usuario,
                self.data_relatorio,
                self.data_carga,
                self.codigo_produto,
                self.quantidade,
                self.data_estoque,
                self.data_fabricacao,
                self.data_vencimento,
                self.alterar_fefo,
                self.pallet_danificado,
                self.vazamento,
                self.observacao
            )
        )

        conexao.commit()
        conexao.close()

    @staticmethod
    def excluir_relatorio(transporte: str, data_relatorio: str):
        """
        Exclui um relatório do banco de dados.

        Parameters
        ----------
            transporte : str
                O número do carga.
            data_relatorio : str
                A data de envio do relatório.
        """

        conexao = conectar_banco_dados_relatorios()
        cursor = conexao.cursor()

        cursor.execute(
            f"""
            DELETE FROM {TABELA_RELATORIOS}
            WHERE transporte = ? AND data_relatorio = ?
            """,
            (
                transporte,
                data_relatorio
            )
        )

        conexao.commit()
        conexao.close()