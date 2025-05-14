# Referencias a bibliotecas, arquivos e frameworks


# (Opcional) Classe - forma de organização do código

# Definition = def - ações do programa

def main():
    print("########## MENU PRINCIPAL ##########")
    print("1 - Soma de dois números")
    print("2 - Subtração de dois números")
    
    opcao = input("Digite o número da opção desejada: ")

    # Antes do Python versão 3.10
    # if opcao == "1":
    #     num1 = int(input("Digite o valor do 1º número: "))
    #     num2 = int(input("Digite o valor do 2º número: "))
    #     # jeito mais antigo
    #     # soma = num1 + num2
    #     # print("Soma =",soma)

    #     # jeito mais atual
    #     print(f"Soma = {num1 + num2}")
    # elif opcao == "2":
    #     num1 = int(input("Digite o valor do 1º número: "))
    #     num2 = int(input("Digite o valor do 2º número: "))
    #     print(f"Subtração = {num1 - num2}")
    # else:
    #     print("Opção inválida, execute o programa novamente")

    match opcao:
        case "1":
            somar_dois_numeros()
        case "2":
            subtrair_dois_numeros()
        #ToDo: criar as opções para multiplicar e dividir dois números
        case _:
            print("Opção inválida, execute o programa novamente")


# sintaxe camelCase - comum em Java, JavaScript e C#
# def somarDoisNumeros

# sintaxa snake_case - comum em Python
def somar_dois_numeros():
    num1 = float(input("Digite o valor do 1º número: "))
    num2 = float(input("Digite o valor do 2º número: "))
    print(f"Soma = {num1 + num2}")

def subtrair_dois_numeros():
    num1 = float(input("Digite o valor do 1º número: "))
    num2 = float(input("Digite o valor do 2º número: "))
    print(f"Subtração = {num1 - num2}")

if __name__ == "__main__":
    main()