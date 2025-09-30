def criar_lista():
    lista = []
    c = ''
    while True:
        elm = input("Digite um elemento para a lista. 'exit' para sair")
        if elm.lower() == 'exit':
            break
        else:
            if len(elm) == 1:
                lista.append(elm)
            else:
                print("a entrada deve conter somente 1 digito")
                
    print("A lista criada foi ", lista)
    return lista

def ordenar_lista_asc(lista):
    lista.sort()
        
    
def ordenar_lista_dsc(lista):
    lista.sort(reverse=True)
    
def verificar_lista(lista):
    tem_numero = any(l.isdigit() for l in lista)
    tem_letra = any(not l.isdigit() for l in lista)
    
    ordenadas_asc = all(str(lista[i]) <= str(lista[i+1]) for i in range(len(lista)-1))
    ordenadas_dsc = all(str(lista[i]) >= str(lista[i+1]) for i in range(len(lista)-1))
    
    ordem = 'Não está Ordenada! '
    
    if ordenadas_asc:
        ordem = 'Está Ordenada asc! '
    
    if ordenadas_dsc:
        ordem = 'Está Ordenada desc! '
        
        
    return (ordem, " Tem Numero! " if tem_numero else " Não tem Numero! ", " Tem Letra! " if tem_letra else " Não tem Letra! ")

def verificacao_rapida(lista):
    return "Está ordenada!" if all(str(lista[i]) <= str(lista[i+1]) for i in range(len(lista)-1)) else "Não está ordenada!"

    

def main():
    lista = ["1","2","3","4","5"]
    choice = ''
    while True:
        choice = input("Escolha a opção: ")
        if choice == 'c':
            lista = criar_lista()
        elif choice == 'oc':
            ordenar_lista_asc(lista)
            print(lista)
        elif choice == 'od':
            ordenar_lista_dsc(lista)
            print(lista)
        elif choice == 'v':
            #print("Está Ordenada" if verificar_lista(lista) else "Está desordenada")
            print(verificar_lista(lista))
        elif choice == 'fv':
            print(verificacao_rapida(lista))
        elif choice == 'q':
            break
        
def mostrar_menu():
    print("Digite a opção que Deseja.")
    print("c  - para CRIAR ou EDITAR lista na memoria")
    print("oc - para ORDENAR lista de maneira CRECENTE")
    print("od - para ORDENAR lista de maneira DECRESCENTE")
    print("v  - para VERIFICAR lista")
    print("fv - para VERIFICAÇÂO RAPIDA")
    print("q  - para SAIR")
        
if __name__ == "__main__":
    main()