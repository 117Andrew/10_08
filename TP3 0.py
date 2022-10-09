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
    p.codigo = str (p.codigo).ljust(3, ' ')
    p.nombre = str (p.nombre).ljust(8, ' ')
    p.estado = str (p.estado).ljust(5, ' ')

def formatearrubros(r):
    r = rubro()
    r.codigo= str (r.codigo).ljust(3, ' ')
    r.nombre= str (r.nombre).ljust(8, ' ')

def formatearRubrosxProd (rxp):
    rxp = rubros_x_producto()
    rxp.codRubro= str (rxp.codRubro).ljust(3, ' ')
    rxp.codProd= str (rxp.codProd).ljust(3, ' ') 
    rxp.min= str (rxp.min).ljust(3, ' ')
    rxp.max= str (rxp.max).ljust(3, ' ')

def formatearSilos(s):
    s = silo()
    s.codSilo= str (s.codSilo).ljust(14, ' ')
    s.nombre= str (s.nombre).ljust(67, ' ')
    s.codProd= str (s.codProd).ljust(12, ' ')
    s.stock= str (s.stock).ljust(32, ' ')

def posicionarseEnProd(codigo):                                     ###Funcion para conseguir la posicion
    global alprod, afprod
    p = productos()
    t = os.path.getsize(afprod)
    alprod.seek(0, 0)
    while alprod.tell()<t and p.codigo != codigo:
        pos = alprod.tell()
        p = pickle.load(alprod)
    return pos

def ordenarrubros():
    global alrub, afrub
    alrub.seek (0, 0)
    aux = pickle.load(alrub)
    tamReg = alrub.tell() 
    t = os.path.getsize(afrub)
    cant = int(t / tamReg)  
    for i in range(0, cant-1):
        for j in range (i+1, cant):
            alrub.seek (i*tamReg, 0)
            auxi = pickle.load(alrub)
            alrub.seek (j*tamReg, 0)
            auxj = pickle.load(alrub)
            if (auxi.codigo > auxj.codigo):
                alrub.seek (i*tamReg, 0)
                pickle.dump(auxj, alrub)
                alrub.seek (j*tamReg, 0)
                pickle.dump(auxi,alrub)
                alrub.flush()

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
    printmenuterciario()

def altaRubros():
    global afrub, alrub
    vrrubro= rubro()
    t = os.path.getsize(afrub)
    if t == 0:
        vrrubro.codigo = input("Ingrese el código del rubro. 0 para cancelar. ")
        while vrrubro.codigo != 0:
            vrrubro.nombre = str (input("Ingrese el nombre del rubro"))
            vrrubro.nombre = vrrubro.nombre.upper()
            formatearrubros(vrrubro)
            pickle.dump(vrrubro,alrub)
            alrub.flush()
            vrrubro.codigo = int(input("Ingrese el codigo del rubro. 0 para cancelar. "))
    else:
        alrub.seek(0,2)
        vrrubro.codigo = int(input("Ingrese el codigo del rubro. 0 para cancelar. "))
        while vrrubro.codigo != 0:
            vrrubro.nombre = str(input("ingrese el nombre del rubro. 0 para salir. "))
            vrrubro.nombre = vrrubro.nombre.upper() 
            ordenarrubros()
            formatearrubros(vrrubro)
            pickle.dump(vrrubro,alrub)
            alprod.flush()
            vrrubro.codigo = int(input("Ingrese el codigo del rubro. 0 para cancelar. "))
    printmenuterciario()

def altaRubrosxProd():
    global afrubxprod, alrubxprod
    vrRxP = rubros_x_producto()
    t = os.path.getsize(afrubxprod)
    if t == 0:
        vrRxP.codRubro = int(input("ingrese el codigo del rubro x producto. 0 para salir: "))
        while vrRxP.codRubro != 0:
            vrRxP.codProd = int(input("ingrese el codigo del producto: "))
            vrRxP.min = int(input("Ingrese la mínima cantidad: "))
            vrRxP.max = int(input("Ingrese la máxima cantidad: "))
            formatearRubrosxProd(vrRxP)
            pickle.dump(vrRxP, alrubxprod)
            alrubxprod.flush()
            vrRxP.codRubro = int(input("ingrese el codigo del rubro x producto. 0 para salir: "))
    else:
        alrubxprod.seek (0,2)
        vrRxP.codRubro = int(input("ingrese el codigo del rubro x producto. 0 para salir: "))
        while vrRxP.codRubro != 0:
            vrRxP.codProd = int(input("ingrese el codigo del producto: "))
            vrRxP.min = int(input("Ingrese la mínima cantidad: "))
            vrRxP.max = int(input("Ingrese la máxima cantidad: "))
            formatearRubrosxProd()
            pickle.dump(vrRxP, alrubxprod)
            alrubxprod.flush()
            vrRxP.codRubro = int(input("ingrese el codigo del rubro x producto. 0 para salir: "))
    printmenuterciario()

def altaSilos():
    global afsilos, alsilos
    vrsilos = silo()
    t = os.path.getsize(afsilos)
    if t == 0:
        vrsilos.codSilo = int(input("Ingrese el código del silo. 0 para salir: "))
        while vrsilos.codSilo != 0:
            vrsilos.nombre = str(input("Ingrese el nombre del Silo: "))
            vrsilos.codProd = int(input("Ingrese el código del producto: "))
            vrsilos.stock = int(input("Ingrese el stock a ingresar: "))
            formatearSilos(vrsilos)
            pickle.dump(vrsilos,alsilos)
            alsilos.flush()
            vrsilos.codSilo = int(input("Ingrese el código del silo. 0 para salir: "))
    else:
        alsilos.seek(0,2)
        vrsilos.codSilo = int(input("Ingrese el código del silo. 0 para salir: "))
        while vrsilos.codSilo != 0:
            vrsilos.nombre = str(input("Ingrese el nombre del Silo: "))
            vrsilos.codProd = int(input("Ingrese el código del producto: "))
            vrsilos.stock = int(input("Ingrese el stock a ingresar: "))
            formatearSilos(vrsilos)
            pickle.dump(vrsilos,alsilos)
            alsilos.flush()
            vrsilos.codSilo = int(input("Ingrese el código del silo. 0 para salir: "))
    printmenuterciario()

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

def rubros():
    printmenuterciario()
    oprubros = input("Ingrese una opcion: ")
    oprubros = oprubros.upper()
    while oprubros != "V":
        if (oprubros == "A"):
            altaRubros()
            oprubros = input("Ingrese una opcion: ")
            oprubros = oprubros.upper()
        else:
            print("Esta funcionalidad esta en construccion")
    printmenuadmin()

def rubrosxProd():
    printmenuterciario()
    oprubrosxProd = input("Ingrese una opcion: ")
    oprubrosxProd = oprubrosxProd.upper()
    while oprubrosxProd != "V":
        if (oprubrosxProd == "A"):
            altaRubrosxProd()
            oprubrosxProd = input("Ingrese una opcion: ")
            oprubrosxProd = oprubrosxProd.upper()
        else:
            print("Esta funcionalidad esta en construccion")
    printmenuadmin()

def silos():
    printmenuterciario()
    opsilos = input("Ingrese una opcion: ")
    opsilos = opsilos.upper()
    while opsilos != "V":
        if (opsilos == "A"):
            altaSilos()
            opsilos = input("Ingrese una opcion: ")
            opsilos = opsilos.upper()
        else:
            print("Esta funcionalidad esta en construccion")
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
