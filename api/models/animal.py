class Animal:
    def __init__(self, id=None, nome="", especie="", idade=0, descricao=""):
        self.id = id
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.descricao = descricao

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "especie": self.especie,
            "idade": self.idade,
            "descricao": self.descricao
        }