#Importamos lo modulos necesarios
import datetime
import hug

#Indica que será de solo acceso local
@hug.local()

#Definimos la función say_hello
def say_hello(name: hug.types.text, age: hug.types.number, hug_timer=3):#hug.types, define el tipo de dato que es
    year_of_birth = datetime.datetime.now().year - age
    return {#Decimos hola al usuario y calculamos su año de nacimiento
        'message': "Hola {0}, naciste el año {1}".format(name, year_of_birth),
        'took': float(hug_timer)
    }

if __name__ == '__main__':
    print(say_hello("panchito", 50))
