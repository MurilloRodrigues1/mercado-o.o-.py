
from classse import *
Pedro = Comprador("Pedro")

Arroz = Produto("Arroz", "Grâo")

Feijão = Produto("Feijão", "Broto")

Pedro.add_produto(Arroz)
Pedro.add_produto(Feijão)

for i in Pedro.getProdutos():
    print(i.getNome())