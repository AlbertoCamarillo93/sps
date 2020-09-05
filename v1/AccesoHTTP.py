import datetime
import hug
 
 
@hug.get(examples="name=pepe perez&amp;age=30")#Metodo get solicita información
@hug.local()
def say_hello(name: hug.types.text, age: hug.types.number, hug_timer=3):
    """Decimos hola al usuario y calculamos su año de nacimiento"""
    year_of_birth = datetime.datetime.now().year - age
    return {
        'message': "Hola {0}, naciste el año {1}".format(name, year_of_birth),
        'took': float(hug_timer)
    }
 
 
if __name__ == '__main__':
    print(say_hello("Juanito", 23))

