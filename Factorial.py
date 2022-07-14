def Factorial(resultado, numero):
    if (numero == 1):
        print("El factorial es =" + str(resultado))
    else:
        resultado *= numero
        numero -= 1
        Factorial(resultado, numero)
opc='1'
while opc!='0' :
    resultado = 1
    numero = int (input("ingresa el número a sacar el factorial: "))
    Factorial(resultado, 5)
    opc=input("1=Sacar el Factorial de otro numero\n0=salir \n")