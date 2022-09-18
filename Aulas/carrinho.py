from Produto import produto 

class carrinho:
    def __init__(self):
        self.__produto = produto

    def valorTotal(self):
        total = 0.0
        for p in self.__produtos:
            total += p.preco
        return total    



