from palavra import Palavra
from arquivo import Arquivo

lista_palavras = Arquivo("default.txt")

class Forca:
    def __init__(self, palavra):
        self.palavra = palavra
        self._erros = 0
        self._digitadas = []

    def mostrar(self):
        palavra, dica = self.palavra.tela()
        print("\n"*10)
        if dica != '':
            print("Dica: ", dica)
        print("\n", ', '.join(l for l in palavra))
        print("Erros: ", "X"*self._erros)

    def errou_e_perdeu(self):
        self._erros += 1
        if self._erros >= 5:
            return True
        return False

    @staticmethod
    def eh_letra_valida(letra):
        return not letra.isdigit()

    def jogar(self):
        while True:
            letra = ''
            self.mostrar()
            
            while True:
                letra = input("Digite uma Letra: ").upper().strip()
                if Forca.eh_letra_valida(letra): break
                print("Letra Inválida. Tente novamente.")
            
            if letra in self._digitadas:
                print("Letra já Utilizada. Tente novamente.")
                if self.errou_e_perdeu():
                    print("Você Perdeu.")
                pass
            
            self._digitadas.append(letra)
            print("Letras já digitadas: ", ", ".join(l for l in self._digitadas))
                
            if not self.palavra.tem_letra(letra):
                if self.errou_e_perdeu():
                    print("Você Perdeu.")
            
            if self.palavra.completada():
                print("Você ganhou")
                break


if __name__ == "__main__":
    palavra = ''
    c = input("Deseja sortear uma palavra? (s/n)")
    if c.upper() != 'S':
        while True:
            p = input("Digite a palavra: ")
            dica = input('Infome uma dica (ou deixe em branco): ')
            if not Palavra.valida(p):
                print("palavra Invalida")
                pass
            print("Palavra salva" if lista_palavras.escrever_palavra(p, dica) else "Falaha ao salvar palavra")
            palavra = Palavra(p, dica)
            break
    else:
        p, d = lista_palavras.sorteia_palavra()
        palavra = Palavra(p, d)
        
    forca = Forca(palavra)
    forca.jogar()
    