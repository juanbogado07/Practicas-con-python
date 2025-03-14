num1= input(" ingrese un valor ")
num2= input("ingrese otro valor ")
print("Los números ingresados son",num1, "y", num2)
if num1<num2:
    print(f"el número mayor es: {num2}")
elif num2<num1:
    print(f"el número mayor es: {num1}")
else:
    print( "Ambos numeros son iguales")
