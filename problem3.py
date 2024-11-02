edad =int(input("Digite su edad:  "))
salario=int(input("Digite su salario en colones:  "))

if(edad>=18) and (salario>= 500000):
    print("Usted está autorizado a tramitar el impuesto")
else:
    print("Usted no se encuentra autorizado para tramitar este impuesto")