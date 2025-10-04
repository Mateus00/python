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
    
    def __len__(self):
        return len(self._dic_palavras)

    def show(self):
        print('-'*50)
        print('Lista de palavras')
        print('-'*50)
        if len(self._dict_palavras) == 0:
            print('Nenhuma palavra cadastrada!')
        else:
            lista_palavras = list(self._dict_palavras.keys())
            lista_palavras.sort()
        for palavra in lista_palavras:
            dica = self._dict_palavras[palavra]
            print(palavra, ' (', dica, ')', sep='')
        print('-'*50)
    
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
        
        
    
