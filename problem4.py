user=(input("Digite su nombre:  "))
edad=int(input("Digite su edad:  "))

if(edad<=10):
    print("¡Hola!",user,"Para poder ingresar tu monto es de 3000 colones")
elif(edad<=15):
    print("¡Hola!",user,"Para poder ingresar tu monto es de 5000 colones")
elif(edad<18):
     print("¡Hola!",user,"Para poder ingresar tu monto es de 7500 colones")
elif(edad>=18):
     print("¡Hola!",user,"Para poder ingresar tu monto es de 10000 colones")