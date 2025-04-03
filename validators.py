def validar_nome(nome):
    if not nome.strip():
        raise ValueError("Nome não pode ser vazio.")
    elif not nome.isalpha():
        raise ValueError("Nome deve conter apenas letras.")
    elif len(nome) < 3:
        raise ValueError("Nome deve ter pelo menos 3 caracteres.")
    return nome