class Jogador:
    def __init__(self, nome, numeros):
        self._nome = nome
        self._numeros = set(numeros)
        self._numeros_marcados = set()
        
    @property
    def nome(self):
        return self._nome
    
    def marca(self, numero_sorteado):
        if numero_sorteado in self._numeros:
            self._numeros_marcados.add(numero_sorteado)
            
    def faltantes(self):
        return self._numeros - self._numeros_marcados
    
    def imprime(self):
        texto = f"Jogador: {self._nome}. Números Restantes = '{self._numeros - self._numeros_marcados}'"