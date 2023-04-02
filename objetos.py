from typing import List, Dict, Union
from persona import Persona
import json


def addPersona(nuevo: Persona = None):
    personas: List[Persona] = [
        Persona(nombre="gerardo", edad=30, url="falta Url")
    ]
    if nuevo is not None:
        if type(nuevo) == Persona:
            personas.append(nuevo)
            for x in personas:
                print("personas: ", x.nombre, x.edad, x.url)
        else:
            nueva_persona = Persona(**nuevo)
            personas.append(nueva_persona)
            for x in personas:
                print("personas: ", x.nombre, x.edad, x.url)
    else:
        for x in personas:
            print("personas: ", x.nombre, x.edad, x.url)


def addPersonas(nuevos: List[Persona] | Persona = None):
    personas = []
    if nuevos is not None:
        if isinstance(nuevos, list):
            personas.extend(nuevos)
        elif isinstance(nuevos, Persona):
            personas.append(nuevos)
    else:
        print("la persona es None")
    for x in personas:
        print("personas: ", x.nombre, x.edad, x.url)


def _calculadora(num1: int = 0, num2: int = 0):
    return num1 * num2


def operacion(num1: int, num2: int, operador: str, ) -> int | float | None:
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        resultado = num1 / num2
    else:
        print("Operación no válida.")
        return None
    return resultado


def getData() -> List[Persona]:
    with open('datos.json', 'r') as archivo:
        datos = json.load(archivo)
    personas = []
    for diccionario in datos['personas']:
        persona = Persona(
            nombre=diccionario['nombre'], edad=diccionario['edad'], url=diccionario['url'])
        personas.append(persona)
    return personas


addPersonas(getData())
# addPersona()

print("Resultado: ", operacion(1, 2, "*"))
