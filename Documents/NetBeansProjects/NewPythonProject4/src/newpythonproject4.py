# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "TERLY"
__date__ = "$24/10/2015 02:28:03 PM$"

if __name__ == "__main__":
    print "Hello World"
#1)
num =input('introduce un numero :')
if num%2==0:
    print 'este numero es par'
else:
    print 'este numero es impar'
    
#2)    
print("1)archivo")
print("2)buscar")
print("3)salir")
archivo =1
buscar = 2
salir = 3
opcion=input("ingresar opcion:")
if (opcion==1 or opcion==2 or opcion==3):
    print("la operacion es incorrecta")
else:
    print ("la operacion es correcta")

#3)
existe = 1000    
while existe >= 200:
    entrega = input('Introdusca la cantidad entregada : ')
    existe = existe - entrega
    
print("el inventario a bajado de 200 unidades")


#4)
def  Menu():
    """Funcion que Muestra el Menu"""
    print """************
Calculadora
************
Menu
------------
1) Suma
2) Resta
3) Multiplicacion
4) Division
5) Salir"""

def calculadora():
    
    """Funcion Para Calcular Operaciones Aritmeticas"""
    Menu()
    opc = int(input("Selecione Opcion\n"))
    while (opc >0 and opc <5):
        a = int(input("Ingrese Numero\n"))
        b = int(input("Ingrese Otro Numero\n"))
        if (opc==1):
            print "La Suma es:", a+b
            opc = int(input("Selecione Opcion\n"))
        elif(opc==2):
            print "La Resta es:", a-b
            opc = int(input("Selecione Opcion\n"))
        elif(opc==3):
            print "La Multiplicacion es:", a*b
            opc = int(input("Selecione Opcion\n"))
        elif(opc==4):
            try:
              print "La Division es:", a/b
              opc = int(input("Selecione Opcion\n"))
            except ZeroDivisionError:
                
              print "No se Permite la Division Entre 0"
              
              opc = int(input("Selecione Opcion\n"))

calculadora()