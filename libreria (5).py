# -*- coding: utf-8 -*-
"""libreria.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14EF-D1cbBdusxO1lsG5jy-CB0yV5H45V
"""

#1
def sumar(p1,p2):
  resultado=p1+p2
  return resultado
  #2
def es_par_o_impar(numero):
  if numero % 2 == 0:
    return "par"
  else:
    return "impar"
    #3
def saludar_usuario():
  nombre_usuario = input("por favor, ingresa tu nombre: ")
  print(f"¡hola,{nombre_usuario}! bienvenido/a.")
  #4
def calcular_area_circulo(radio):
  area =  3.1416 * radio ** 2
  return area
  #5
def clasificar_numero(numero):
  if numero > 0:
    return "positivo."
  elif numero < 0:
      return "negativo"

  else:
      return "cero"
#6
def celsius_a_fahrenheit(celsius):
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit
  #7
def obtener_cuadrado(numero):
  return numero ** 2
  #8
def calcular_factorial(n):
  if n < 0:
    return "El factorial no está definido para números negativos."
  factorial = 1
  for i in range(1, n + 1 ):
     factorial *= i
  return factorial
  #9
def contar_vocales(palabra):
  #definir las vocales en minusculas
  vocales = "aeiouáéíóú"
  # convertir la palabra a minusculas para evitar distincion entre mausculas y minusculas
  palabra = palabra.lower()
  # contar cuantas veces aparece cada vocal en la palabra
  conteo = sum(1 for letra in palabra if letra in vocales)
  return conteo
#10
def mostrar_tabla_multiplicar():


      # solicitar al usuario el numero para la tabla de multiplicar
      numero = int(input("ingresa el numero para mostrar su tabla de multiplicar: "))
      # mostrar la tabla de multiplicar del numero ingresado
      print(f"\ntabla de multiplicar del {numero}:\n")
      for i in range(1,11):
        print(f"{numero} x {i} = {numero * i}")
        #11
def area_circulo(radio):
    return math.pi * radio ** 2

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_rectangulo(base, altura):
    return base * altura

def mostrar_menu():
    print("\nCalculadora de Áreas")
    print("1. Círculo")
    print("2. Triángulo")
    print("3. Rectángulo")
    print("4. Salir")

def obtener_valores(figura):
    if figura == 1:  # Círculo
        radio = float(input("Introduce el radio del círculo: "))
        return radio,
    elif figura == 2:  # Triángulo
        base = float(input("Introduce la base del triángulo: "))
        altura = float(input("Introduce la altura del triángulo: "))
        return base, altura
    elif figura == 3:  # Rectángulo
        base = float(input("Introduce la base del rectángulo: "))
        altura = float(input("Introduce la altura del rectángulo: "))
        return base, altura
    else:
        print("Opción no válida.")
        return None

def main():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Selecciona una opción (1/2/3/4): "))
            if opcion == 4:
                print("Saliendo del programa.")
                break
            valores = obtener_valores(opcion)
            if valores:
                if opcion == 1:
                    radio = valores[0]
                    print(f"El área del círculo es: {area_circulo(radio):.2f}")
                elif opcion == 2:
                    base, altura = valores
                    print(f"El área del triángulo es: {area_triangulo(base, altura):.2f}")
                elif opcion == 3:
                    base, altura = valores
                    print(f"El área del rectángulo es: {area_rectangulo(base, altura):.2f}")
        except ValueError:
            print("Por favor, ingresa un número válido.")