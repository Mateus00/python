class Tabuleiro:
    def __init__(self):
        self._posicoes = [
            ['@', '@', '@'],
            ['@', '@', '@'],
            ['@', '@', '@']
        ]
        
    def imprime(self):
        print('\n  |A|B|C')
        for cont, linha in enumerate(self._posicoes):
            print(cont+1, " |", "|".join(linha), sep='')
            
    def jogada(self, posicao, simbolo):
        # Entrada será do tipo "C3, B2, A3, C1, ..."
        try:
            linha = int(posicao[1])-1
            coluna = ord(posicao[0].upper()) - ord("A")
            if self._posicoes[linha][coluna] == '@':
                self._posicoes[linha][coluna] = simbolo
                return True
        except:
            print("jogada invalida!")
            pass
        return False
    
    def tem_jogada(self):
        return any('@' in linha for linha in self._posicoes)
    
    def todas_as_linhas(self):
        todas = []
        
        for cont, linha in enumerate(self._posicoes):
            todas.append(tuple(linha))
            
        for cont in range(3):
            coluna = [self._posicoes[0][cont],
                      self._posicoes[1][cont],
                      self._posicoes[2][cont]]
            todas.append(tuple(coluna))
            
        diagonal = []
        transversal = []
        for cont in range(3):
            diagonal.append(self._posicoes[cont][cont])
            transversal.append(self._posicoes[2-cont][cont])
        todas.append(tuple(diagonal))
        todas.append(tuple(transversal))
        
        return todas
    