class Mensagem:
    def __init__(self, remetente, conteudo):
        # Inicializa os atributos da mensagem
        self.remetente = remetente
        self.conteudo = conteudo

    def exibir(self):
        # Retorna a mensagem formatada conforme o padrão requisitado
        return f"Remetente: {self.remetente}\nConteúdo: {self.conteudo}"


# Lê o nome do remetente (primeira linha da entrada)
remetente = input("Rementente:=> ")
# Lê o conteúdo da mensagem (segunda linha da entrada)
conteudo = input("Conteúdo:=> ")

# Cria o objeto Mensagem com os dados recebidos
mensagem = Mensagem(remetente, conteudo)

# Imprime a mensagem formatada pela função exibir (saída conforme especificação)
print(mensagem.exibir())