"""
    Proyecto Bimestral
    Segundo Bimestre
    
    Problemática:
"""

def crearFacebook():

    n = input("Ingrese su nombre: ")
    e = int(input("Ingrese su edad: "))
    ciudad = input("Ingrese su cuidad: ")
    p = input("Ingrese su país: ")
    correo = input("Ingrese su correo electrónico: ")    
    cadena = "Cuenta de facebook con los datos:\nNombre de usuario: " + n + "\nEdad: " + str(e) + "\nCiudad: " + ciudad + "\nPaís: " + p  + "\nCorreo electrónico: " + correo
    return cadena

def crearTwitter():
    n = input("Ingrese su nombre: ")
    name = input("Ingrese su nombre de usuario: ")
    lname = input("Ingrese su apellido: ")
    e = int(input("Ingrese su edad: "))
    ciudad = input("Ingrese su ciudad: ")
    p = input("Ingrese su país: ")
    i = input("Ingrese su idioma: ")
    correo = input("Ingrese su correo electrónico: ")
    print("Cuenta de Twitter con los datos: \nnombre de usuario: " + name + "\nNombre: " + n + "\nApellido: " + lname + "\nEdad: " + str(e) + "\nCiudad: " + ciudad + "\nPaís: " + p + "\nIdioma: " + i +"\nCorreo electronico: " + correo + "\n")


def crearWhatsapp():
    n = input("Ingrese su nombre: ")
    phone = input("Ingrese su número de telefono: ")
    e = int(input("Ingrese su edad:"))
    ciudad = input("Ingrese su ciudad: ")
    p = input("Ingrese su país: ")
    cadena = "Cuenta de Whatsapp con los datos: \nnombre de usuario: " + n + "\nNúmero de teléfono: " + str(phone) + "\nEdad: " + str(e) + "\nCiudad: " + ciudad + "\nPaís: " + p + "\n"
    return cadena

def crearTelegram():
    n = input("Ingrese su nombre de usuario: ")
    phone = int(input("Ingrese su número de teléfono: "))
    ciudad =  input("Ingrese su ciudad: ")
    p = input("Ingrese su país: ")
    area = input("Ingrese su área de interés:")
    print("Cuenta de telegram con los datos:    \nNombre de usuario: " + n + "\nNúmero de teléfono: " + str(phone) + "\nCiudad: " + ciudad + "\nPaís: " + p + "\nÁrea de interés: " + area + "\n")

def crearSignal():
    n = input("Ingrese su nombre: ")
    phone = int(input("Ingrese su número de teléfono: "))
    ciudad =  input("Ingrese su ciudad: ")
    p = input("Ingrese su país: ")
    hobby = input("Ingrese su hobby principal:")
    cadena = "Cuenta de Signal con los datos:   \nNombre de usuario: " + n + "\nNúmero de teléfono: " + str(phone) + "\nCiudad: " + ciudad + "\nPaís: " + p + "\nHobby principal: " + hobby + "\n" 
    return cadena

def crearInstagram():
    n = input("Ingrese su nombre: ")
    e = int(input("Ingrese su edad: "))
    ciudad =  input("Ingrese su ciudad: ")
    correo = input("Ingrese su correo electrónico:")
    print( "Cuenta de Instragram con los datos: \nNombre de usuario: " + n +    "\nEdad: " + str(e) + "\nCiudad: " + ciudad + "\nCorreo electronico: " + correo + "\n")

def crearFlickr():
    n = input("Ingrese su nombre: ")
    correo = input("Ingrese su correo electrónico: ")
    cadena = "Cuenta de Flickr con los datos: \nNombre de usuario: " + n + "\nCoreo electrónico: " + correo
    return cadena

def obtenerMensaje(i):
    mensajeFinal = ["Campaña con poca afluencia", "Campaña moderada siga adelante", "Excelente campaña"]
    if (i <= 5  and  i > 0):
        return mensajeFinal[0]
    elif (i >= 6 and i <= 15):
        return mensajeFinal[1]
    elif (i >= 16):
        return mensajeFinal[2]



if __name__ == "__main__":
    bandera = True
    i = 0
    m = ""
    while (bandera):
        d = int(input("Ingresa la cuenta que deseas crear:\n(1) Para crear Facebook\n(2) Para crear Whatsapp\n(3) Para crear Telegram \n(4) Para crear Signal \n(5) Para crear Instagram\n(6) Para crear Flickr\n(7) Para crear Twitter.\n(0) Para no crear cuenta\n"))
        if (d == 1):
            m = crearFacebook()
        elif (d == 2):
            m = crearWhatsapp()
        elif (d == 3):
            crearTelegram() # no devuelve valor
        elif (d == 4):
            m = crearSignal()
        elif (d == 5):
            crearInstagram() # no no devuelve valor
        elif (d == 6): 
            m = crearFlickr()
        elif (d == 7):
            crearTwitter() # no no devuelve valor
        elif (d == 0):
        	bandera == False
        	m = obtenerMensaje(i)        
    
        elif (d < 0 or d > 7 ):
        	print("Fuera de rango")

        print(m) 
        i += 1

