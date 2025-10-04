class Palavra:
    def __init__(self, palavra, dica=''):
        self._palavra = palavra.upper()
        self._dica = dica
        self._tela = ['_ ' for i in palavra]
        
    def completada(self):
        return all(p == t for p, t in zip(self._palavra, self._tela))
    
    def tela(self):
        return self._tela, self._dica
    
    def tem_letra(self, letra):
        encontrado  = False
        for i, l in enumerate(self._palavra):
            if l.upper() == letra.upper():
                self._tela[i] = l.upper()
                encontrado = True
        return encontrado
    
    @staticmethod
    def valida(palavra):
        return all(not l.isdigit() for l in palavra)
    
    