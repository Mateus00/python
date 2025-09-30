import string

# Crie uma função que retorne a letra do alfabeto correspondente a um índice
# (por exemplo, 1 para "A", 2 para "B"). 
def letra_por_numero(numero, maiuscula=False):
    #print(string.ascii_lowercase)  # letras minúsculas - ascii_lowercase
    #print(string.ascii_uppercase)  # letras maiúsculas - ascii_uppercase
    #print(string.ascii_letters)    # minúsculas + maiúsculas - ascii_letters
    n = int(numero)-1
    letra = ''
    if maiuscula != False:
        letra = string.ascii_uppercase[n]
    else:
        letra = string.ascii_lowercase[n]
        
    print(f"A letra é {letra}")
    return letra
    
    
if __name__ == "__main__":
    letra_por_numero(input("Qual o numero?"),  True if input("Maiúscula? (s/n): ").lower() == "s" else False)