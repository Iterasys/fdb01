# Referencias a bibliotecas, arquivos e frameworks


# (Opcional) Classe - forma de organização do código

# Definition = def - ações do programa

import datetime
import time
import os


def main():
    print("########## MENU PRINCIPAL ##########")
    print("1 - Soma de dois números")
    print("2 - Subtração de dois números")
    print("3 - Multiplicação de dois números")
    print("4 - Divisão de dois números [If Else]")
    print("5 - Divisão de dois números [Try Except]")
    print("6 - Contagem progressiva")
    print("7 - Contagem regressiva")
    print("8 - Consultar data e hora")
    
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
        case "3":
            multiplicar_dois_numeros()
        case "4":
            dividir_dois_numeros_if_else()
        case "5":
            dividir_dois_numeros_try_except()
        case "6":
            contagem_progressiva()
        case "7":
            contagem_regressiva()
        case "8":
            consultar_data_hora()
        case _:
            print("Opção inválida, execute o programa novamente")


# sintaxe camelCase - comum em Java, JavaScript e C#
# def somarDoisNumeros

# sintaxa snake_case - comum em Python
def somar_dois_numeros():
    try:
        num1 = float(input("Digite o valor do 1º número: "))
        num2 = float(input("Digite o valor do 2º número: "))
        print(f"Soma = {num1 + num2}")
    except ValueError:
        print("Erro: digite apenas numeros e use ponto como decimal")

def subtrair_dois_numeros():
    try:
        num1 = float(input("Digite o valor do 1º número: "))
        num2 = float(input("Digite o valor do 2º número: "))
        print(f"Subtração = {num1 - num2}")
    except ValueError:
        print("Erro: digite apenas numeros e use ponto como decimal")

def multiplicar_dois_numeros():
    try:
        num1 = float(input("Digite o valor do 1º número: "))
        num2 = float(input("Digite o valor do 2º número: "))
        print(f"Multiplicação = {num1 * num2}")
    except ValueError:
        print("Erro: digite apenas numeros e use ponto como decimal")

def dividir_dois_numeros_if_else():
    try:
        num1 = float(input("Digite o valor do 1º número: "))
        num2 = float(input("Digite o valor do 2º número: "))
        if num2 != 0:
            print(f"Divisão = {num1 / num2}")
        else:
            print("Não é possível dividir por zero")
    except ValueError:
        print("Erro: digite apenas numeros e use ponto como decimal")

def dividir_dois_numeros_try_except():
    try:
        num1 = float(input("Digite o valor do 1º número: "))
        num2 = float(input("Digite o valor do 2º número: "))
        print(f"Divisão = {num1 / num2}")
    except ZeroDivisionError:
        print("Não é possível dividir por zero")
    except ValueError:
        print("Erro: digite apenas numeros e use ponto como decimal")
    finally:
        print("Terminou")

def contagem_progressiva():
    try:
        num = int(input("Contar até o número: "))
        for i in range(num + 1):
            print(i, end=' ')
            print()    # pula uma linha (imprime uma linha vazia)

    except ValueError:
        print("Erro: digite apenas numeros e sem parte decimal")

def contagem_regressiva():
    try:
        num = int(input("Contar a partir número: "))
        for i in range(num, -1, -1):
            # To Do: limpar linha via system
            # os.system('clear')
            print(i, end=' ')
            print()
            # time.sleep(1) #espera de 1 segundo

    except ValueError:
        print("Erro: digite apenas numeros e sem parte decimal")

def consultar_data_hora():
    agora = datetime.datetime.now()
    print(f'Data e hora atual: {agora.strftime("%d/%m/%Y, %H:%M:%S")}')

if __name__ == "__main__":
    main()