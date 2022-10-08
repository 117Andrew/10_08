import os                                                               ###Comienzo de la importacion de librerias###
import pickle   
import os.path
import datetime    

class operaciones:                                                      ###Comienzo de la declaracion de clases###
    def __init__(self):
        self.patente = ""
        self.codProd = 0
        self.fechaCupo = datetime.date.today()
        self.estado = ""
        self.bruto = 0
        self.tara = 0
class productos:
    def __init__(self):
        self.codigo = 0
        self.nombre = ""
        self.estado = True
class rubro:
    def __init__(self):
        self.codigo = 0
        self.nombre = ""
class rubros_x_producto:
    def __init__(self):
        self.codRubro = 0
        self.codProd = 0
        self.min = 0.0
        self.max = 0.0
class silo:
    def __init__(self):
        self.codSilo = 0
        self.nombre = 0
        self.codProd = 0
        self.stock = 0 

afop = "./operaciones.dat"                                              ###Comienzo de la declaracion de archivos fisicos###
afprod = "./productos.dat"
afrub = "./rubros.dat"
afrubxprod = "./rubros_x_productos.dat"
afsilos = "./silos.dat"

if not os.path.exists(afop):                                            ###Comprueba exisitencia del archivo###
    alop = open(afop, "w+b")                                            ###Crea el archivo si no existe###
else:
    alop = open(afop, "r+b")                                            ###Abre el archivo para lectura y escritura###
if not os.path.exists(afprod):                                          ###Comprueba exisitencia del archivo###
    alprod = open(afprod, "w+b")                                        ###Crea el archivo si no existe###
else:
    alprod = open(afprod, "r+b")                                        ###Abre el archivo para lectura y escritura###
if not os.path.exists(afrub):                                           ###Comprueba exisitencia del archivo###
    alrub = open(afrub, "w+b")                                          ###Crea el archivo si no existe###
else:
    alrub = open(afrub, "r+b")                                          ###Abre el archivo para lectura y escritura###
if not os.path.exists(afrubxprod):                                      ###Comprueba exisitencia del archivo###
    alrubxprod = open(afrubxprod, "w+b")                                ###Crea el archivo si no existe###
else:
    alrubxprod = open(afrubxprod, "r+b")                                ###Abre el archivo para lectura y escritura###
if not os.path.exists(afsilos):                                         ###Comprueba exisitencia del archivo###
    alsilos = open(afsilos, "w+b")                                      ###Crea el archivo si no existe###
else:
    alsilos = open(afsilos, "r+b")

vrprod = productos()
def cerrar():
    alprod.close()
    alop.close()
    alrubxprod.close()
    alsilos.close()
    alrub.close()

def printmenuprincipal():                                               ###Funcion del print del menu principal###
    
    print ("\n\nMENU_PRINCIPAL")
    print ("\n\t1_Administracion")
    print ("\t2_Entrega de cupos")
    print ("\t3_Recepcion")
    print ("\t4_Registrar calidad")
    print ("\t5_Registrar peso bruto")
    print ("\t6_Registrar descarga")
    print ("\t7_Registrar tara")
    print ("\t8_Reportes")
    print ("\t\t0_Fin del programa")

def printmenuadmin():                                                   ###Funcion del print del menu administracion###

    print ("\n\nMENU_ADMINISTRACIONES")
    print ("\n\tA_Titulares")
    print ("\tB_Productos")
    print ("\tC_Rubros")
    print ("\tD_Rubros X productos")
    print ("\tE_Silos")
    print ("\tF_Sucursales")
    print ("\tG_Producto X titular")
    print ("\t\tV_Volver al menu principal")

def printmenuterciario():                                               ###Funcion del print de los tercer menus###
    print ("\n\nMENU_TERCIARIO")
    print ("\n\tA_Alta")
    print ("\tB_Baja")
    print ("\tC_Consulta")
    print ("\tM_Modificacion")
    print ("\t\tV_Volver_al_menu_administraciones")

def formatearprod(p):
    p = productos()
    p.codigo = str (p.codigo).ljust(3)
    p.nombre = str (p.nombre).ljust(8)
    p.estado = str (p.estado).ljust(5)

def posicionarseEnProd(codigo):                                     ###Funcion para conseguir la posicion
    global alprod, afprod
    p = productos()
    t = os.path.getsize(afprod)
    alprod.seek(0, 0)
    while alprod.tell()<t and p.codigo != codigo:
        pos = alprod.tell()
        p = pickle.load(alprod)
    return pos

def altaProd():
    global alprod, afprod
    vrprod = productos()
    t = os.path.getsize(afprod)
    if t == 0:
        vrprod.nombre = str (input("Ingrese el nombre del producto. 0 para salir"))
        while  vrprod.nombre!= "0":
            vrprod.codigo = input("Ingrese codigo del producto")
            vrprod.estado = True
            formatearprod(vrprod)
            pickle.dump(vrprod,alprod)
            alprod.flush()
            vrprod.nombre = str (input("Ingrese el nombre del producto. 0 para salir"))
    else:
        alprod.seek(t)
        vrprod.nombre = str (input("Ingrese el nombre del producto. 0 para salir"))
        vrprod.nombre = vrprod.nombre.upper()
        while  vrprod.nombre!= "0":
            vrprod.codigo = input("Ingrese codigo del producto. 0 para salir")
            vrprod.estado = True
            formatearprod(vrprod)
            pickle.dump(vrprod,alprod)
            alprod.flush()
            vrprod.nombre = str(input("Ingrese el nombre del producto. 0 para salir"))
            vrprod.nombre = vrprod.nombre.upper()

def bajaProd():
    global afprod, alprod
    vrprod = productos()
    t = os.path.getsize(afprod)
    if t != 0:
        codigo = str(input("Ingrese el codigo del producto. 0 para salir"))
        while codigo != "0": 
            pos = posicionarseEnProd(codigo)
            alprod.seek(pos)
            vrprod.estado = False
            formatearprod(vrprod)
            pickle.dump(vrprod,alprod)
            alprod.flush()
            print("Se ha eliminado correctamente el producto\n")
            codigo = str(input("Ingrese el codigo del producto. 0 para salir"))
    else:
        print("No hay productos cargados")
    printmenuterciario()

def consultaProd():
    global afprod, alprod, vrprod
    t = os.path.getsize(afprod)
    print("Listado de productos\n")
    alprod.seek(0,0)
    while alprod.tell() < t:
        vrprod = pickle.load(alprod)
        print(vrprod.nombre, vrprod.codigo)
    printmenuterciario()

def prod():
    printmenuterciario()
    opprod = input("Ingrese una opcion. V para salir: ")
    opprod = opprod.upper()
    while opprod != "V":
        if (opprod == "A"):
            altaProd()
        elif (opprod == "B"):
           bajaProd()
        elif (opprod == "C"):
           consultaProd()
        elif (opprod == "M"):
            modProd()
        elif (opprod == "F"):
            alprod = open(afprod, "w+b")
        else:
            print ("Ingrese una opcion correcta")
        opprod = input("Ingrese una opcion. V para salir: ")
        opprod = opprod.upper()
    printmenuadmin()

def admin():                                                            ###funcion de administraciones
    printmenuadmin()
    opcionadmin = (input("Ingrese la opcion deseada. 'V' para salir: "))
    opcionadmin = opcionadmin.upper()
    while opcionadmin != "V":
        if (opcionadmin == "A" or opcionadmin == "F" or opcionadmin == "G"):
            print(opcionadmin)
            print("Esta funcionalidad esta en construccion")
        elif (opcionadmin == "B"):                                      ###Lleva al menu productos###
            prod()
        elif (opcionadmin == "C"):                                      ###Lleva al menu rubros###
            rubros()
        elif (opcionadmin == "D"):                                      ###Lleva al menu rubros x productos###
            rubrosxProd()
        elif (opcionadmin == "E"):                                      ###Lleva al menu silos###
            silos()
        opcionadmin = (input("Ingrese la opcion deseada. 'V' para salir: "))
        opcionadmin = opcionadmin.upper() 
    printmenuprincipal()

def menuPrincipal():            
    printmenuprincipal()
    opcionprincipal = int(input("Ingrese la opcion que desee: "))
    while opcionprincipal != 0:
        if opcionprincipal == 1:
            admin()
        elif opcionprincipal == 2:
            EntregaCupos()
        elif opcionprincipal == 3:
            print()#Recepcion()
        elif opcionprincipal == 4:
            print()#RegistrarCalidad()
        elif opcionprincipal == 5:
            print()#registrarPesoBruto()
        elif opcionprincipal == 6:
            print("Proceso en construccion")
        elif opcionprincipal == 7:
            print()#RegistrarTara()
        elif opcionprincipal == 8:
            print()#Reportes
        elif opcionprincipal == 9:
            print()#ListSilosyRechazos
        opcionprincipal = int(input("Ingrese la opcion que desee: "))
    if opcionprincipal == 0:
        cerrar()
menuPrincipal()