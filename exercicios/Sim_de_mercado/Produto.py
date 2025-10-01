class Produto:
    def __init__(self, descricao, preco):
        self._descricao = descricao
        self._preco = float(preco)
        
    def __str__(self):
        return f"{self._descricao} (R${self._preco:.2f})"
    
    
class ProdutoEstoque(Produto):
    def __init__(self, descricao, preco):
        super().__init__(descricao, preco)
        self._estoque = 0.0
        
    def __str__(self):
        texto = super().__str__()
        texto += f", Estoque: {self._estoque:.0f}"
        return texto
    
    @property
    def descricao(self):
        return self._descricao
    
    @descricao.setter
    def descricao(self, descricao):
        self._descricao = descricao
        
    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, preco):
        self._preco = preco
        
    def entrada(self, quantidade):
        self._estoque += quantidade
        
    def saida(self, quantidade):
        if quantidade <= self._estoque:
            self._estoque -= quantidade
            return True
        return False
    
class ProdutoVenda(Produto):
    def __init__(self, descricao, preco, quantidade):
        super().__init__(descricao, preco)
        self._quantidade = quantidade
        
    def __str__(self):
        texto = super().__str__()
        texto += f", Qtde: {self._quantidade:.0f}"
        texto += f", Total: {self.total:.2f}"
        return texto
    
    @property
    def total(self):
        return self._quantidade * self._preco
        
if __name__ == "__main__":
    p = ProdutoEstoque("Caixa de Pinga", "67")
    print(p)