class Venda():
    def __init__(self):
        self._produtos = []
        self._total = 0.00
        
    @property
    def total(self):
        return self._total
    
    @property
    def numero_produtos(self):
        return len(self._produtos)
    
    def adiciona_produto(self, produto):
        self._produtos.append(produto)
        self._total += produto.total
        
    def __str__(self):
        texto = '\n' + '-'*50
        texto += '\nProdutos:'
        for produto in self._produtos:
            texto += '\n' + str(produto)
        texto += '\n' + '-'*50
        texto += f"Total da venda: R${self._total:0.2f}"
        texto += '\n' + '-'*50
        return texto
    