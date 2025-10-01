import tabuleiro

class Velha:
    def __init__(self):
        self._tabuleiro = tabuleiro.Tabuleiro()
        self._jogador = 'O'
        
    def imprime(self):
        print('\n'*2)
        print('Jogo da velha')
        self._tabuleiro.imprime()
        
    def troca_jogador(self):
        self._jogador = 'O' if self._jogador == 'X' else 'X'
        
    def pega_jogada(self):
        while True:
            self.imprime()
            print("Jogador", self._jogador)
            posicao = input("Informe a Jogada: ")
            if self._tabuleiro.jogada(posicao, self._jogador):
                break
            
    def e_vencedor(self, jogador):
        return True if tuple([jogador]*3) in self._tabuleiro.todas_as_linhas() else False
    
    def jogar(self):
        while True:
            if self._tabuleiro.tem_jogada():
                self.pega_jogada()
                print(self.e_vencedor(self._jogador))
                if self.e_vencedor(self._jogador):
                    print("Jogador vencedor é", self._jogador)
                    break
                else:
                    self.troca_jogador()
            else:
                print("Empate!")
                break
        
            
if __name__ == "__main__":
    velha = Velha()
    velha.jogar()