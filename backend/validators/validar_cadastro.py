from backend.models.usuarios import Usuario

def validar_cadastro(nome_completo, senha) -> bool:
    """
    Valida as informações do cadastro do usuário.

    Parameters
    ----------
        nome_completo
            O nome completo do usuário.
        senha
            A senha do usuário.

    Returns
    ----------
        bool
            True se válido, False caso contrário.
        mensagem
            Explicando o motivo do valor booleano.
    """

    if not nome_completo or not senha:
        return False, "Todos os Campos Devem ser Preechidos."
    
    if len(senha) < 8:
        return False, "Tamanho da Senha Inválido."
    
    resultado = Usuario.buscar_usuarios(nome_completo, senha)
    if resultado:
        return False, "Nome de Usuário Já Encontrado."
    
    return True, "Cadastro Bem Sucedido!"
    