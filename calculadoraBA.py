prosseguir = True

while prosseguir:
    
        print("====Calculadora====")

        num1 = float(input("Digite seu primeiro valor: "))
        num2 = float(input("Digite seu segundo valor: "))

        print("""ESCOLHA UMA DAS SEGUINTES OPERAÇÕES:
        [1] Soma
        [2] Subtração 
        [3] Multiplicação 
        [4] Divisão""")
        
        operacao = input("Digite a operação desejada: ")

        if operacao == "1":
                resultado = num1 + num2
                print(f"RESULTADO {resultado:.2f}")
        elif operacao == "2":
                resultado = num1 - num2
                print(f"RESULTADO {resultado:.2f}")
        elif operacao == "3":
                resultado = num1 * num2
                print(f"RESULTADO {resultado:.2f}")
        elif operacao == "4":
                if num2 == 0:
                        print("ERROR...Divisor por zero!")
                else:
                        resultado = num1 / num2
                        print(f"RESULTADO {resultado:.2f}")
        else:
                print("Operação Inválida")
    
opcao = input("Deseja continuar? (S/N): ").lower()

while opcao not in ("s", "n"):
    opcao = input("Resposta inválida. Digite S ou N: ").lower()
    if opcao == "n":
        print("ENCERRANDO PROGRAMA...")
    prosseguir = False
