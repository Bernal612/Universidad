from re import sub
import subprocess
import sys
import getpass

#class perro:
#    def __init__():
#        pass
#
#    def getRaza():
#        pass
#
#    def calcularEdad():
#        pass


# Usuario ------------------------------------------------------------------------------------

def crearUsuario():
    try:
        usuario = input("Ingresar Username: ")
        password = input("Ingresar Password: ")
        subprocess.run(['sudo', 'adduser', usuario], shell = True)
        subprocess.run(password)
        subprocess.run(password)
    except:
        print(f"Se ha producido un error")
        sys.exit(1)

def cambiarNombre():
    try:
        subprocess .run(['/etc/passwd'])
        oldnombre = input("Seleccionar Usuario: ")
        newnombre = input("Ingrese El Nuevo Nombre De Usuario: ")
        subprocess.run(['sudo','usermod','-l', newnombre, oldnombre], shell = True)
        print("")
    except:
        print(f"Se ha producido un error")
        sys.exit(1)


def cambiarContrasena():
    try:
        subprocess.run(['/etc/passwd'])
        pswUsuario = input("Seleccionar Usuario")
        old_psw = input("Ingrese Actual Contrseña")
        new_psw = input("Ingrese Nueva Contraseña")
        subprocess.run(['sudo','passwd',pswUsuario, new_psw, old_psw], shell= True)
        print("Se ha cambiado la contraseña de: ", )
    except:
        print(f"Se ha producido un error")
        sys.exit(1)

def eliminarUsuario():
    try:
        subprocess.run(['/etc/passwd'])
        elimUsuario = input("Ingrese el usuario que desea eliminar")
        subprocess.run=(['sudo','deluser', elimUsuario])
        print("Se ha eliminado a ",elimUsuario)
    except:
        print(f"Se ha producido un error")
        sys.exit(1)


# Administración ------------------------------------------------------------------------------------

def Iniciar():
    try:
        programa = input("Seleccione El Programa Que Desea Ejecutar: ")
        subprocess.run(['chmod','a',])
    except:
        print(f"Se ha producido un error")
        sys.exit(1)

def Actualizar():
    try:
        subprocess.run(['sudo','apt-get','update'])    
        subprocess.run(['sudo','apt-get','upgrade'])
    except:
        print(f"Se ha producido un error")
        sys.exit(1)

def Respaldo():
    try:
        subprocess.run(['cp'])
    except:
        print(f"Se ha producido un error")
        sys.exit(1)

def Monitorear ():
    try:
        subprocess.run(['top'], shell = True)
    except:
        print(f"Se ha producido un error")
        sys.exit(1)

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------

operacion = int(input("Seleccione Una Opcion: \n Manipulacion De Usuario (1) \n Administracion De Tareas (2)\n Configuracion De Servicios \n"))

if operacion == 1:
    
    opcionesUser = ["Crear Usuario(1)","Modificar Usuario(2)", "Eliminar Usuario(3)"]

    for i in opcionesUser:
        print(i)

    opcionU = int(input("Selecciona una opción: "))

    #  Crear Usuario
    if opcionU == 1:
         crearUsuario()

    # Modificar Usuario        
    elif opcionU == 2:
        
        opcionesMod = ["Cambiar Nombre(1)","Cambiar Contrseña (2)"]
        
    #Cambiar Nombre
        if opcionesMod == 3:
           cambiarNombre()
    
    #Cambiar Contraseña
        elif opcionesMod == 4:
           cambiarContrasena()

    # Eliminar Usuario
    elif opcionU == 3:
        eliminarUsuario()
    
    else:
        print("Opcion no valida")

elif operacion == 2:

    opcionesAdmin = ["Iniciar Sistema(1)", "Actualizar(2)", "Copia De Respaldo Y Recuperación(3)", "Monitoreo Del Sistema(4)", "Programación De Tareas(5)", "Detener El Sistema(6)"]

    for i in opcionesAdmin:
        print(i)
    
    opcionA = int(input("Seleccione Una Opción: "))

    #Iniciar Sistema
    if opcionA == 1:
        pass

    #Actualizar
    elif opcionA == 2:
        pass

    #Copia De Respaldo Y Recuperación
    elif opcionA == 3:
        pass

    #Monitoreo Del Sistema
    elif opcionA == 4:
        pass

    #Programación De Tareas
    elif opcionA == 5:
        pass

    #Detener El Sistema

elif operacion == 3:

    opcionesRed = ["Montaje De Servicios(1)", "Servidor De Impresión(2)", "Servidores De Atchivos(3)", "Servicios De Red(4)", "Redes TCP/IP(5)","Configuración(6)", "Direcciones Dinámicas(7)","Servicios De Nombres(8)"]

    opcionesR = int(input("Selecciones Una Opción: "))

    #
    if opcionesR == 1:
        pass
    if opcionesR == 2:
        pass
    if opcionesR == 3:
        pass
    if opcionesR == 4:
        pass
    if opcionesR == 5:
        pass
    if opcionesR == 6:
        pass
    if opcionesR == 7:
        pass