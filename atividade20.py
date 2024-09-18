# Crie um programa que utilize uma estrutura de repetição para somar todos os números pares de 1 a 100 e exiba o resultado.

def somar_pares():
    soma = 0
    for i in range(1, 101):  
        if i % 2 == 0:  
            soma += i  

    return soma

resultado = somar_pares()
print(f"A soma dos números pares de 1 a 100 é: {resultado}")