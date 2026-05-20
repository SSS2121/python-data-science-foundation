Acceso = False  # Variable global


def Validar_Username(username):

    if not isinstance(username, str):
        raise ValueError("El nombre de usuario debe ser una cadena de texto.")

    if len(username) < 3 or len(username) > 20:
        raise ValueError("El nombre de usuario debe tener entre 3 y 20 caracteres.")

    username = username.strip()
    return True,username

def Validar_Password(password):

    Caracteres_Especiales = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/"

    if not isinstance(password, str):
        raise ValueError("La contraseña debe ser una cadena de texto.")

    if len(password) < 8 or len(password) > 128:
        raise ValueError("La contraseña debe tener entre 8 y 128 caracteres.")

    for Caracter in password:
        if Caracter in Caracteres_Especiales:
            break

    else:
        raise ValueError("La contraseña debe contener al menos un carácter especial.")

    password = password.strip()
    
    return True, password



def Validar_Contraseña(username, password):
    global Acceso 
    try:
        Validar_Username(username)
        Validar_Password(password)
        Acceso = True
    except ValueError:
        Acceso = False
    
    return Acceso


Validar_Contraseña("Juan", "ContraseñaSegura123!")
if Acceso is True:
    print("Acceso concedido.")
else:
    print("Acceso denegado.")