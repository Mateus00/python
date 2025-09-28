# Escreva os códigos em Python modularizados e com tratamento de exceções para
# resolver os problemas a seguir:
# A) Desenvolver um algoritmo que construa uma lista de tuplas com nome e salário de
# funcionários. Em seguida, o código deve recalcular os salários considerando os seguintes
# aumentos:
#  • 20% para salários de até R$2.000,00;
#  • 15% para salários entre R$2.000,00 e R$5.000,00;
#  • 5% para salários maiores que R$5.000,00;
# Por fim, o código deve exibir o total de aumento (total dos salários novos menos o total de
# salários antigos e os nomes dos funcionários com salários menores que R$2.000,00.
def principal():
    funcionarios = list()
    show = False

    while True:
        
        def bemvindo():
            print("Bem Vindo ao Programa de calculos de salario. Você será feliz aqui.")
            print("Digite 'list' p LISTAR funcionarios.")
            print("Digite 'a' para ADICIONAR funcionario.")
            print("Digite 'b' para EDITAR um funcionario já criado.")
            print("Digite 's' para AUMENTAR o salário de um funcionario.")
            print("Digite 'd' para SER FELIZ.")
            print("Digite 'h' para EXIBIR este menu.")
            print("Digite 'x' para SAIR.")
        
        if not show:
            show = True
            bemvindo()
        
        choice = input()

        if choice == 'a':
            nome = input("Digite o nome do funcionario:")
            valor = input("Dig o salario do funcionario:")

            funcionarios.append((nome, valor))
            
        elif choice == 'b':
            nome = input("Digite o nome do funcionario que você quer editar: ")
            valor = input("Digite o novo Salário a ser atribuido: ")

            for i, f in enumerate(funcionarios):
                if f[0] == nome:
                    funcionarios[i] = (f[0], valor)
            
            
        elif choice == 's':
            fs = list()
            ms = list()
            total = 0
            
            for i, funcionario in enumerate(funcionarios):
                nome, salario = funcionario[0], int(funcionario[1])
                
                if salario <= 2000:
                    ms.append(nome)
                    novo = salario * 1.2
                    fs.append({'nome':nome, 'antigo':salario, 'novo':novo, 'dif':novo-salario})
                    funcionarios[i] = (nome, novo)
                    
                elif salario > 2000 and int(f[1]) <= 5000:
                    novo = salario * 1.15
                    fs.append({'nome':nome, 'antigo':salario, 'novo':novo, 'dif':novo-salario})
                    funcionarios[i] = (nome, novo)
                    
                else:
                    novo = salario * 1.05
                    fs.append({'nome':nome, 'antigo':salario, 'novo':novo, 'dif':novo-salario})
                    funcionarios[i] = (nome, novo)
                    
            for x in fs:
                total += x['dif']
                print(x)
            print("Total: ", total)
            print("Menores que 2000:", ms)
            
        elif choice == 'd':
            nome = input("Digite o nome do funcionario que você quer ver feliz: ")
            for i, f in enumerate(funcionarios):
                if f[0] == nome:
                    funcionarios[i] = (f[0], int(f[1])*2)
            
        elif choice == 'h':
            bemvindo()
            
        elif choice == 'list':
            print(funcionarios)
            
        elif choice == 'x':
            break

    print(funcionarios)

if __name__ == '__main__':
    principal()
    