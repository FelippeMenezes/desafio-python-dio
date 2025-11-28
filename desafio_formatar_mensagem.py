def formatar_mensagem(texto):
    """
    Formata uma mensagem de texto aplicando as seguintes regras:
    - Remove espaços extras do início e do fim
    - Converte para letras minúsculas
    - Garante apenas um espaço entre as palavras
    - Retorna string vazia se o texto ficar vazio após remoção de espaços
    """
    # Remove espaços extras do início e do fim da string
    texto = texto.strip()
    
    # Se a string ficou vazia após o strip, retorna a string vazia
    if texto == "":
        return ""
    
    # Processa o texto para garantir:
    # - letras minúsculas
    # - apenas um espaço separando as palavras
    texto_minusculo = texto.lower()
    palavras = texto_minusculo.split()
    mensagem_formatada = " ".join(palavras)
    
    return mensagem_formatada

# Lê a mensagem enviada ao robô via input padrão
entrada = input()  # Tipo de dado esperado: str

# Chama a função formatar_mensagem (você irá implementar a lógica)
saida = formatar_mensagem(entrada)

# Exibe a mensagem padronizada
print(saida)