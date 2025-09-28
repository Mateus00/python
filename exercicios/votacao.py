# B) Construir um simulador de urna eletrônica. Inicialmente, o simulador deve permitir o
# cadastro de candidatos. O usuário pode cadastrar quantos candidatos desejar. O cadastro
# de um candidato envolve um número e seu nome. O número deve ser armazenado em
# formato textual, mas deve possuir exatamente dois dígitos numéricos. A função isdigit() do
# tipo textual pode ser usada para verificar se o texto é um número válido. Por fim, os
# candidatos cadastrados devem ser mantidos em um dicionário (número: nome).
# Após o cadastro de candidatos, o simulador deve iniciar a votação. O simulador
# deve permitir uma quantidade indeterminada de votos. Para votar, o usuário deve informar
# o número do candidato. O sistema deve mostrar o nome do candidato para o usuário
# confirmar. Números inválidos devem ser computados como votos nulos. Já o texto vazio
# deve ser contabilizado como voto em branco. A sumarização dos votos deve ser feita
# usando um dicionário. Ao término da votação, o simulador deve mostrar o total e a
# porcentagem de votos de cada candidato, nulos e brancos.
candidatos = {
    "14": "Juninho", 
    "22": "Zezinho", 
    "31": "Luizinho", 
    "13": "Ladraozinho"
}
eleitores = {}

def bemvindo():
    print("Bem Vindo ao Programa Eleitoral da sua cidade. Você será Triste aqui. :(")
    print("Digite 'ls' p LISTAR ELEITORES.")
    print("Digite 'lc' p LISTAR CANDIDATOS.")
    print("Digite 'a' para ADICIONAR eleitor.")
    print("Digite 'b' para EDITAR um eleitor já criado.")
    print("Digite 's' para COMEÇAR a votação.")
    print("Digite 'h' para EXIBIR este menu.")
    print("Digite 'q' para SAIR.")

def principal():
    global candidatos, eleitores
    show = False
    while True:
        if not show:
            show = True
            bemvindo()
        
        choice = input("")
        if choice == 'ls': #lista eleitores
            for digito, nome in eleitores.items():
                print(f"Número: {digito}, Nome: {eleitores[digito]}")
                
        elif choice == 'lc': #lista candidatos
            for digito, nome in candidatos.items():
                print(f"Número: {digito}, Nome: {candidatos[digito]}")
                
        elif choice == 'a': #adiciona eleitor
            digito = input("Numero do Eleitor: ")
            nome = input("Nome do Eleitor: ")
            if len(digito) != 2 or not digito.isdigit() or digito in eleitores:
                print('Cadastro inválido!')
            else:
                eleitores[digito] = nome

        elif choice == 'b':
            d = input("Digite o numero do eleitor: ")
            eleitores[d] = input("Digite o novo nome para alterar: ")
            print("Processo Concluído\nO nome foi alterado para: ", eleitores[d])
            
        elif choice == 's':
            eleitores_votaram = {}
            votos = {num: 0 for num in candidatos}
            
            while True:
                print(" -- Ao final da votação, digite encerrar para ver os resultados. -- ")
                c = input("Digite o numero do eleitor: ")
                
                if c == "encerrar":
                    print(votos)
                    total_votos = sum(votos.values())
                    for candidato, vts in votos.items():
                        porcentagem = 0
                        if vts > 0: porcentagem = (vts/total_votos) *100
                        print(f"Candidato {candidatos[candidato]} recebe {vts} votos! %: ({porcentagem:.2f}%)")
                    candidato_mais_votado = max(votos, key=votos.get)
                    print("\nCandidato mais votado:", candidatos[candidato_mais_votado])
                    break
                
                elif len(c) != 2 or not c.isdigit() or c not in eleitores:
                    print("Numero Digitado não encontrado Tente novamente.")
                    
                elif c in eleitores_votaram:
                    print("Eleitor já votou.")
                    
                else:
                    eleitores_votaram[c] = eleitores[c]
                    print("Candidatos:")
                    for digito, nome in candidatos.items():
                        print(f"Número: {digito}, Nome: {nome}")
                    num = input("Digite o numero do candidato: ")
                    if num in votos:
                        votos[num] += 1
                        print(f"Voto para {candidatos[num]} registrado!")
                    else:
                        print("Voto inválido!")
        
        elif choice == 'h':
            bemvindo()
        elif choice == 'q':
            break
    
    print(candidatos)
    print(eleitores)

if __name__ == '__main__':
    principal()