
def funcion(num_ecuacion,numeros):
    print(numeros)
    if(num_ecuacion==1):
        print("x^4+2x^3+x^2+5x")
        for i in numeros:
            result= i**4+2*i**3+i**2+i*5
            print("Resultado del numero",i,"es igual a  : ",result)
        num_ecuacion+=1
        funcion(num_ecuacion,numeros)
    elif(num_ecuacion==2):
        print("4x^3+6x^2+2x+5")
        for i in numeros:
            result =4*i**3+6*i**2+2*i+5
            print("Resultado del numero", i, "es igual a  : ", result)
        num_ecuacion += 1
        funcion(num_ecuacion, numeros)
    elif(num_ecuacion==3):
        print("12x^2+12x+2")
        for i in numeros:
            result = 12*i**2+12*i+2
            print("Resultado del numero", i, "es igual a  : ", result)
        num_ecuacion += 1
opc='1'
while opc!='0':
    numeros= []
    numeros.append(int(input("Ingresa el primer numero:")))
    numeros.append(int(input("Ingresa el segundo numero:")))
    numeros.append(int(input("Ingresa el tercer numero:")))
    num_ecuacion=1
    funcion(num_ecuacion,numeros)
    opc=input("1=Ingresar otros tres numeros\n0=salir \n")