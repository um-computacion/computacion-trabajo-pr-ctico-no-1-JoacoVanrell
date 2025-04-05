def decimal_a_romano(numero):
    
    valores = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    resultado = ''
    for valor, simbolo in valores:
        while numero >= valor:
            resultado += simbolo
            numero -= valor
    return resultado

print("Ingresa un numero decimal entre 1 y 3999:")
numero = int(input())
resultado = decimal_a_romano(numero)
print(f"El número {numero} en romano es: {resultado}")

print("Fin del programa")
