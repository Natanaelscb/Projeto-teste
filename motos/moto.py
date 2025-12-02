class Moto:
    def __init__(self, nome, marca, modelo, ano,cor,registro):
        self.nome = nome
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.registro = registro

    def __str__(self):
        return f"A motocicleta {self.nome} foi cadastrada"