"""
Este programa calcula el Índice de Masa Corporal (IMC) de una persona.
El IMC se calcula dividiendo el peso en kilogramos entre la altura en metros al cuadrado.
"""

def calcular_imc(peso, altura):
    """
    Calcula el Índice de Masa Corporal.

    Args:
        peso (float): Peso de la persona en kilogramos.
        altura (float): Altura de la persona en metros.

    Returns:
        float: El valor del IMC.
    """

    imc = peso / (altura ** 2)
    return imc

# Solicitar datos al usuario
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

# Calcular el IMC
resultado = calcular_imc(peso, altura)

# Mostrar el resultado
print("Su IMC es:", resultado)

# Clasificar el IMC según la OMS
if resultado < 18.5:
    print("Bajo peso")
elif 18.5 <= resultado < 25:
    print("Peso normal")
elif 25 <= resultado < 30:
    print("Sobrepeso")
else:
    print("Obesidad")