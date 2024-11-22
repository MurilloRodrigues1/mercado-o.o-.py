import os

def pause():
    os.system("pause")

def limpa():
    os.system("cls")

class Comprador:
    def _init_(self, nome):
        self.nome = nome
        self.carrinho_de_compras = []

    def add_produto(self, produto):
        self.carrinho_de_compras.append(produto)

    def getProdutos(self):
        return self.carrinho_de_compras

class Produto:
    def _init_(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo

    def getNome(self):
        return self.nome
    
    def _str_(self):
        return self.nome