from database.banco_dados_usuarios import conectar_banco_dados_usuarios

from backend.constants.banco_dados import TABELA_USUARIOS


class Usuario:
    """
    Representa um usuário.

    Attributes
    ----------
        usuario_id : int | None
            O ID do usuário (gerado automaticamente pelo banco).
        nome_completo : str
            O nome completo do usuário.
        senha : str
            A senha do usuário.
    """


    def __init__(self, nome_completo: str, senha: str, usuario_id=None):
        """
        Inicializa um novo objeto usuário.

        Parameters
        ----------
            nome_completo : str
                O nome completo do usuário.
            senha : str
                A senha do usuário.
            usuario_id : int, opcional
                O ID do usuário (usado apenas ao buscar do banco).
        """
        self.usuario_id = usuario_id
        self.nome_completo = nome_completo
        self.senha = senha


    def inserir_usuario(self):
        """Insere um novo usuário no banco de dados e atualiza o ID no objeto."""

        conexao = conectar_banco_dados_usuarios()
        cursor = conexao.cursor()

        cursor.execute(
            f"""
            INSERT INTO {TABELA_USUARIOS} (nome_completo, senha)
            VALUES (?, ?)
            """,
            (self.nome_completo, self.senha),
        )

        self.usuario_id = cursor.lastrowid

        conexao.commit()
        conexao.close()


    @staticmethod
    def excluir_usuario(usuario_id: int):
        """
        Exclui um usuário do banco de dados.

        Parameters
        ----------
            usuario_id : int
                O ID do usuário a ser excluído.
        """
        conexao = conectar_banco_dados_usuarios()
        cursor = conexao.cursor()

        cursor.execute(
            f"DELETE FROM {TABELA_USUARIOS} WHERE usuario_id = ?", (usuario_id,)
        )

        conexao.commit()
        conexao.close()
    

    @staticmethod
    def buscar_usuarios(nome_completo, senha):
        """
        Busca um usuário no banco de dados.

        Parameters
        ----------
            nome_completo
                O nome completo do usuário.
            senha
                A senha do usuário.
        Returns
        -------
            Um objeto Usuario.
        """

        conexao = conectar_banco_dados_usuarios()
        cursor = conexao.cursor()

        cursor.execute(
        f"""
        SELECT * FROM {TABELA_USUARIOS}
        WHERE nome_completo = ? AND senha = ?
        """, (nome_completo, senha)
        )

        resultado = cursor.fetchone()

        conexao.commit()
        conexao.close()

        return resultado