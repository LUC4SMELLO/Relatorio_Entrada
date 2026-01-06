import json
from datetime import datetime

from database.banco_dados_relatorios_temporarios import conectar_banco_dados_relatorios_temporarios
from backend.constants.banco_dados import TABELA_RELATORIOS_TEMPORARIOS


class RelatoriosTemporarios:
    """
    Representa um rascunho de relatório de entrada.
    """

    @staticmethod
    def salvar(usuario_id: str, dados: dict):
        """
        Salva ou atualiza o rascunho do relatório do usuário.
        """

        conexao = conectar_banco_dados_relatorios_temporarios()
        cursor = conexao.cursor()

        cursor.execute(
            f"""
            INSERT INTO {TABELA_RELATORIOS_TEMPORARIOS} (
                usuario_id,
                dados_json,
                data_atualizacao
            )
            VALUES (?, ?, ?)
            ON CONFLICT(usuario_id)
            DO UPDATE SET
                dados_json = excluded.dados_json,
                data_atualizacao = excluded.data_atualizacao
            """,
            (
                usuario_id,
                json.dumps(dados, ensure_ascii=False),
                datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            )
        )

        conexao.commit()
        conexao.close()

    @staticmethod
    def buscar(usuario_id: str) -> dict | None:
        """
        Retorna o rascunho do usuário, se existir.
        """

        conexao = conectar_banco_dados_relatorios_temporarios()
        cursor = conexao.cursor()

        cursor.execute(
            f"""
            SELECT dados_json
            FROM {TABELA_RELATORIOS_TEMPORARIOS}
            WHERE usuario_id = ?
            """,
            (usuario_id,)
        )

        row = cursor.fetchone()
        conexao.close()

        if not row:
            return None

        return json.loads(row[0])
    
    @staticmethod
    def excluir(usuario_id: str):
        """
        Exclui o rascunho do usuário após envio do relatório.
        """

        conexao = conectar_banco_dados_relatorios_temporarios()
        cursor = conexao.cursor()

        cursor.execute(
            f"""
            DELETE FROM {TABELA_RELATORIOS_TEMPORARIOS}
            WHERE usuario_id = ?
            """,
            (usuario_id,)
        )

        conexao.commit()
        conexao.close()


