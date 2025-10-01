import random
from Jogador import Jogador

espaco = "\n" + "-"*100 + "\n"

class Bingo:
    def __init__(self, qtd_numeros=75):
        self._numeros = random.sample(range(1, qtd_numeros + 1), qtd_numeros)
        self._numeros_sorteados = set()
        self._jogadores = []
        self._vencedores = []
        
    def adiciona_jogador(self, nome):
        if any(jogador.nome == nome for jogador in self._jogadores):
            print("Jogador já está jogando")
            print(espaco)
            return False
        
        numeros = random.sample(self._numeros, 24)
        self._jogadores.append(Jogador(nome, numeros))
        print(f"Jogador {nome} entrou no Bingo!")
        print(espaco)
        return True
    
    def imprime(self):
        print(f"{espaco}Os numeros sorteados foram: \n", end='')
        print("-- ", f", ".join(str(n) for n in self._numeros_sorteados), end=" --\n")
        
        print(f"{espaco}Os numeros que faltam sortear são: \n", end='')
        print("--", f", ".join(str(n) for n in set(self._numeros) - self._numeros_sorteados), end=" --\n")
        print(espaco)
        
        for jogador in self._jogadores:
            faltantes = jogador.faltantes()
            print(f"Para o jogador {jogador.nome}, faltam {len(faltantes)} peças:")
            print(", ".join(str(n) for n in faltantes))
            print(espaco)
        
    def sorteia(self):
        numero_sorteado = self._numeros.pop()
        self._numeros_sorteados.add(numero_sorteado)
        print(f"O numero sorteado foi: '{numero_sorteado}'")
        
        for jogador in self._jogadores:
            faltantes = jogador.faltantes()
            
            if numero_sorteado in faltantes:
                jogador.marca(numero_sorteado)
            
    def tem_vencedor(self):
        for jogador in self._jogadores:
            if len(jogador.faltantes()) == 0:
                print(f"{jogador.nome} grita 'Bingo!!!!!!'")
                self._vencedores.append(jogador)
        return bool(self._vencedores)
            
    def jogar(self):
        if not self._jogadores:
            print("Vamos iniciar o Bingo! Digite 'iniciar' quando adicionar pelo menos 1 jogador.")
            print(espaco)
            while True:
                nome = input("Digite o nome do jogador: ").strip()
                if nome.lower().strip() == 'iniciar':
                    break
                self.adiciona_jogador(nome)
        
        print(f"{espaco}Lista com nuemros: {', '.join(str(n) for n in self._numeros)}{espaco}")
        print("Começando sorteio de Números!")
        
        while True:
            input("Tecle Enter para sortear o proximo núemro!")
            print("\n"*5, end='')
            self.sorteia()
            self.imprime()
            if self.tem_vencedor():
                break
        
        print("Fim de Jogo.\nLista de Ganhadores:\n", end='')
        for vencedor in self._vencedores:
            print(vencedor.nome)

if __name__ == "__main__":
    bingo = Bingo()
    bingo.jogar()