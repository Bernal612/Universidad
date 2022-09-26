from os import system
from re import sub
import subprocess
import sys
import getpass
from tkinter.tix import Tree

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
        subprocess.run(['chmod','a', programa])
        print(programa, " se ha ejecutado exitosamente")
    except:
        print(f"Se ha producido un error")
        sys.exit(1)

def Actualizar():
    try:
        subprocess.run(['sudo','apt-get','update'])    
        subprocess.run(['sudo','apt-get','upgrade'])
        print("Se han actualizado lo sepositorios existosamente")
    except:
        print(f"Se ha producido un error")
        sys.exit(1)

def Respaldo():
    try:
        subprocess .run(['/etc/passwd'])
        usuario_cop = input("Elija el usuario al que se le hará una copia: ")
        archivo_cop = input("Seleccione el archivo o directorio al cual se le hará la copia")
        host = input("Escriba el host al que pertenece(ejepmlo: @host-remoto): ")
        guardar_arc = input("Elija el directorio/lugar en donde se guardará la copia: ")
        subprocess.run(['scp',archivo_cop,usuario_cop,host,guardar_arc], shell = True)
    except:
        print(f"Se ha producido un error")
        sys.exit(1)

def Monitorear ():
    try:
        subprocess.run(['top'], shell = True)
    except:
        print(f"Se ha producido un error")
        sys.exit(1)

def Programar():
    try:
        print("A continuación se realizarán una serie de preguntas para programar la ejecución de un archivo o programa a su elección. Se requiere que llene todas las preguntas, en caso de que necesite que el programa se ejecute siempre en tal dia de la semana o en todos los meses, escribir '*'")
        programa = input("Seleccione un programa (URL/Dirección), o comando que desee programar para ser ejecutado: ")
        minuto = int(input("Selecciona un minuto en el que se ejecutará este programa(0-59): "))
        hora = int(input("Seleccione una hora en la que se ejecutará este programa (0-24): "))
        dia = int(input("Seleccione el dia del mes en el que se ejecutará este programa(1-31): "))
        mes = int(input("Seleccione el mes en el que se ejecutará este programa(1-12/JAN-DEC): "))
        semana = int(input("Seleccione el dia de la semana en el que se ejecutará este programa(0-6/SUN-SAT): "))
        subprocess.run([minuto,hora,dia,mes,semana,programa], shell = True)
    except:
        subprocess.run(['sudo','apt','update'], shell = True)
        subprocess.run(['sudo','apt','install','cron'], shell = True)
        subprocess.run(['sudo','systemctl','enable','cron'], shell = True)
        print(f"Se ha producido un error, puede que no tenga Cron instalado. \n Cron se ha instalado \n Vuelva a intentar")
        sys.exit(1)

def Detener():
    try:
        subprocess.run(['top'], shell = True)
        programa = input("Seleccione el programa que desea cerrar: ")
        subprocess.run(['killall',programa], shell = True)
    except:
        subprocess.run(['sudo','apt','update'], shell = True)
        subprocess.run(['sudo','apt-get','install','xorg-xkill'], shell = True)
        subprocess.run(['sudo','systemctl','enable','cron'], shell = True)
        print(f"Se ha producido un error, puede que no tenga xkill instalado. \n xkill se ha instalado \n Vuelva a intentar")
        sys.exit(1)

# Redes ------------------------------------------------------------------------------------

def Instalar():
    try:
        subprocess.run(['apt-get','install','samba'])
        print("Se ha instalado el servidor exitosamente")
    except:
        print(f"Se ha producido un error")
        sys.exit(1)

def Impresion():
        subprocess.run(['apt-get','install','cups'], shell = True)
        subprocess.run(['sudo','systemctl','start','cups'], shell = True)
        subprocess.run(['sudo','enable','cups'], shell = True)
        print(f"El servidor de impresión se encuentra activo, se solicita monitorearlo desde la web")
        sys.exit(0)

def Archivos():
    try:
        subprocess.run(['/etc/samba/passwd'])
        Agg_user_grp = input("Seleccionar el usuario que desea añadir al grupo: ")
        subprocess.run(['sudo','usermod','-aG','sambashare',Agg_user_grp])
        subprocess.run(['sudo','service','smbd','reload'])
        print("Se ha agregado a ",Agg_user_grp," al grupo.")
    except:
        print(f"Se ha producido un error.")
        sys.exit(1)

def Configuracion():
    try:
        subprocess.run(['sudo','ifconfig','-a'], shell = True)
        subprocess.run(['sudo', 'nano', '/etc/network/interfaces'], shell = True)
        nombre = input("Seleccionar la interfaz de red de ethernet (Ejemplo: eth0,wifi0,wlan0): ")
        ip = input(["IP que desee asignar: "])
        estado = int(input("Activar(1) \n Desactivar(2)"))
        if estado == 1:
            subprocess.run(['sudo','ifconfig', nombre, ip, 'netmask 255.255.255.0', '[promisc]', 'up'], shell = True)

        elif estado ==2:
            subprocess.run(['sudo','ifconfig', nombre, ip, 'netmask 255.255.255.0', '[promisc]', 'down'], shell = True)
    except:
        print(f"Se ha producido un error.")
        sys.exit(1)

def RedDinamica():
    try:
        subprocess.run(['sudo','ifconfig','-a'], shell = True)
        subprocess.run(['sudo', 'nano', '/etc/network/interfaces'], shell = True)
        nombre = input("Seleccionar la interfaz de red de ethernet (Ejemplo: eth0,wifi0,wlan0): ")
        subprocess.run(['auto', nombre], shell =  True)
        subprocess.run(['iface', nombre,'inet','dhcp'], shell = True)
        subprocess.run(['sudo', '/etc/init.d/networking', 'restart'], shell = True)
    except:
        print(f"Se ha producido un error.")
        sys.exit(1)

def AggUsuario():
    try:
        subprocess .run(['/etc/passwd'])
        server_user = input("Ingresar el nombre del usuario: ")
        server_pssw = input("Ingresar la contraseña del usuario: ")
        subprocess.run(['sudo','smbpasswd','-a',server_user, server_pssw], shell = True)
        subprocess.run(['sudo','service','smbd','reload'])
        print("Se ha agregado a ",server_user," al servidor exitosamente.")
    except:
        print(f"Se ha producido un error")
        sys.exit(1)

def ElimUsuario():
    try:
        subprocess .run(['/etc/samba/passwd'])
        server_user = input("Ingresar el nombre del usuario que desea ELIMINAR del servidor: ")
        subprocess.run(['sudo','smbpasswd','xa',server_user], shell = True)
        subprocess.run(['sudo','service','smbd','reload'])
        print("Se ha eliminado a ",server_user," del servidor exitosamente.")
    except:
        print(f"Se ha producido un error")
        sys.exit(1)

def DesUsuario():
    try:
        subprocess .run(['/etc/samba/passwd'])
        server_user = input("Ingresar el nombre del usuario: ")
        subprocess.run(['sudo','smbpasswd','-d',server_user], shell = True)
        subprocess.run(['sudo','service','smbd','reload'])
        print("Se ha deshabilitado a ",server_user," del servidor exitosamente.")
    except:
        print(f"Se ha producido un error")
        sys.exit(1)

def HabUsuario():
    try:
        subprocess .run(['/etc/samba/passwd'])
        server_user = input("Ingresar el nombre del usuario: ")
        subprocess.run(['sudo','smbpasswd','-e',server_user], shell = True)
        subprocess.run(['sudo','service','smbd','reload'])
        print("Se ha habilitado a ",server_user," del servidor exitosamente.")
    except:
        print(f"Se ha producido un error")
        sys.exit(1)

def AggUsuario():
    try:
        subprocess .run(['/etc/passwd'])
        server_user = input("Ingresar el nombre del usuario: ")
        server_pssw = input("Ingresar la contraseña del usuario: ")
        subprocess.run(['sudo','smbpasswd','-a',server_user, server_pssw], shell = True)
        subprocess.run(['sudo','service','smbd','reload'])
        print("Se ha agregado a ",server_user," al servidor exitosamente.")
    except:
        print(f"Se ha producido un error")
        sys.exit(1)

# ------------------------------------------------------------------------------------

operacion = int(input("Seleccione Una Opcion: \n Manipulacion De Usuario (1) \n Administracion De Tareas (2)\n Manejo De Servicios \n"))

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

        for i in opcionesMod:
            print(i)

        opcionesMod_S = int(input("Seleccione una opción: "))
    #Cambiar Nombre
        if opcionesMod_S == 1:
           cambiarNombre()
    
    #Cambiar Contraseña
        elif opcionesMod_S == 2:
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
        Iniciar()

    #Actualizar
    elif opcionA == 2:
        Actualizar()

    #Copia De Respaldo Y Recuperación
    elif opcionA == 3:
        Respaldo()

    #Monitoreo Del Sistema
    elif opcionA == 4:
        Monitorear()

    #Programación De Tareas
    elif opcionA == 5:
        Programar()

    #Detener El Sistema
    elif opcionA == 6:
        Detener()

elif operacion == 3:

    opcionesRed = ["Montaje De Servicios(1)", "Servidor De Impresión(2)", "Servidores De Atchivos(3)", "Configuración(4)", "Direcciones Dinámicas(5)","Servicios De Usuarios(6)"]

    for i in opcionesRed():
        print (i)

    opcionesR = int(input("Selecciones Una Opción: "))

    #Montaje De Servidor
    if opcionesR == 1:
        Instalar()

    #Servidor De impresión
    if opcionesR == 2:
        Impresion()

    #Servidor De Archivos
    if opcionesR == 3:
        Archivos()

    #Configuracion
    if opcionesR == 4:
        Configuracion()

    #Red Dinamica
    if opcionesR == 5:
        RedDinamica()

    #Usuarios
    if opcionesR == 6:
        opcionesR_User = ["Agregar Usuario(1)","Eliminar Usuario(2)","Deshabilitar Usuario(3)","Habilitar Usuario(4)"]

        for i in opcionesR_User:
            print(i)
        
        opcionesR_SU = int(input("Seleccione Una Opción: "))

        #Agregar Usuario
        if opcionesR_SU == 1:
            AggUsuario()
        
        #Eliminar Usuario
        if opcionesR_SU == 2:
            ElimUsuario()
        
        #Deshabilitar Usuario
        if opcionesR_SU == 3:
            DesUsuario()
        
        #Habilitar Usuario
        if opcionesR_SU == 4:
            HabUsuario()
