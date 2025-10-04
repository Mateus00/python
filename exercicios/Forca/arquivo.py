from random import shuffle
from os.path import isfile

class Arquivo:
    def __init__(self, arquivo):
        self._arquivo = arquivo
        self._dict_palavras = {}
        if isfile(self._arquivo):
            with open(self._arquivo) as arq:
                for linha in arq:
                    palavra, dica = tuple(linha.strip().split(":"))
                    self._dict_palavras[palavra] = dica
                    
        print(self._dict_palavras)
    
    def sorteia_palavra(self):
        lista_palavras = list(self._dict_palavras.keys())
        shuffle(lista_palavras)
        palavra = lista_palavras[0]
        dica = self._dict_palavras[palavra]
        return palavra, dica
    
    def escrever_palavra(self, palavra, dica=''):        
        with open(self._arquivo, "a", encoding="utf-8") as arq:
            arq.write(palavra.upper()+":"+dica+"\n")
            return True
    
    @staticmethod
    def criar_arquivo(nome_arquivo):
        with open(nome_arquivo, "a", encoding="utf-8"): 
            pass
        
        
    
