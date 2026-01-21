import re

comprobar= r'^[a-z0-9]+@(gmail|alumnos|hotmail|outlook)\.(com|mx|net)$'
dominios_usuarios = r'^@(gmail|hotmail|alumnos|outlook)$'
"""
Se necesita un analisis por IA para reconocer imagenes tipo credenciales y obtener una certificacion de la persona
"""

def comprobar_rol(email):
    if re.match(comprobar,email):
        print("Correo valido")

        nombre,orgnizacion = email.split('@')
        del nombre
        nombre_dominio = orgnizacion.split(".")[0]
        if nombre_dominio == 'alumnos':
            return 'usuario'
        else:
            print("Dominio invalido")
    else:
        print("Correo invalido")

