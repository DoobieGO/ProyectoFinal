#Ruleta del 1 al 9
name=input("Digite su nombre:  ")
lastname=input("Digite su apellido:  ")
age=int(input("Digite su edad:  "))
number=int(input("Digite un número del 1 al 9:  "))
secret= 8

if(number!=secret):
    print("Gracias por su participación")
elif(number==secret):
    print("¡Felicidades!",name,lastname,"a la grandiosa edad de",age,"lograste adivinar nuestro numero secreto")
else:
    print("error inesperado")
