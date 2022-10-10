'''
Comision: 111
Integrantes del grupo
Albanesi, Julian Andres
Martinez, Valentina
Vallejos, Tomas
'''

###El posicionamiento cambia el estado en recepcion pero no en registrar calidad, no se pudo probar el resto de cosas
###A partir registrar peso bruto esta todo hecho logicamente

###---Importacion de librerias---###
from msilib.schema import Registry                                      
import os                                                               ###Comienzo de la importacion de librerias###
import pickle   
import os.path
import datetime
from re import A                                                        

###--------------------------------------------------------- ###

###---Declaracion de constructores---###

class operaciones:                                                      
    def __init__(self):
        self.patente = ""
        self.codProd = 0
        self.fechaCupo = datetime.date.fromisoformat("2022-10-01")
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
class reportes:
	def __init__(self):
		self.codpro = 0
		self.contprod = 0
		self.patmen = " "


###--------------------------------------------------------- ###

###--- Declaracion de archivos fisicos ---###

afop = "./operaciones.dat"                                              ###Comienzo de la declaracion de archivos fisicos###

afprod = "./productos.dat"

afrub = "./rubros.dat"

afrubxprod = "./rubros_x_productos.dat"

afsilos = "./silos.dat"

afreportes = "./reportes.dat"

###--- Declaracion de archivos logicos ---###

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

###--- Declaracion de variables auxiliares ---###

vrprod = productos()

canttot = 0

cantrec = 0


###--------------------------------------------------------- ###

###--- Declaracion de metodo para cerrar archivos ---###

def cerrar():

    alprod.close()

    alop.close()

    alrubxprod.close()

    alsilos.close()

    alrub.close()


###--------------------------------------------------------- ###

###--- Declaracion de metodos para prints de menu ---###

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


###--------------------------------------------------------- ###

###--- Declaracion de metodos de formateo ---###

def formatearoperaciones(op):
    op = operaciones()
    op.patente= str (op.patente).ljust(7, ' ')
    op.codProd= str (op.codProd).ljust(3, ' ')
    print(type(op.fechaCupo))
    op.fechaCupo = str (op.fechaCupo).ljust(10, ' ')
    print(type(op.fechaCupo))
    op.estado= str (op.estado).ljust(1, ' ')
    op.bruto= str (op.bruto).ljust(5, ' ')
    op.tara= str (op.tara).ljust(5, ' ')

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

def formatearreportes(reporte):
	reporte.codpro = str(reporte.codpro).ljust(3," ")
	reporte.contprod = str(reporte.contprod).ljust(4," ")
	reporte.patmen = str(reporte.patmen).ljust(7," ")


###--------------------------------------------------------- ###

###--- Declaracion de metodos para posicionamiento, ordenamiento y auxiliares ---###

def calculos():
	global afop, alop, afprod, alprod, afreportes, canttot, cantrec
	alrepor = open(afreportes, "w+b")
	vrrepor = reportes()
	vrprod = productos()
	vrop = operaciones()
	Tprod = os.path.getsize(afprod)
	Toper = os.path.getsize(afop)
	alprod.seek(0,0)
	alop.seek(0,0)

	while alprod.tell() < Tprod:
		menor = 99999999
		Trepor = os.path.getsize(afreportes)
		alrepor.seek(Trepor, 0)
		while alop.tell() < Toper:
			
			if int(vrprod.codigo) == int(vrop.codProd): #Guarda codigo de prod, cuenta la cantidad, y acumula el peso.
				vrrepor.codpro = int(vrprod.codigo)
				vrrepor.contprod += 1
				formatearreportes(vrrepor)
				pickle.dump(vrrepor, alrepor)
				alrepor.flush()
				
				if (int(vroper.br) - int(vroper.tr)) <= menor: # Guarda la patente que menor peso neto descargo
					menor = (int(vroper.br) - int(vroper.tr))
					vrrepor.patmen = vroper.pat
					formatearreportes(vrrepor)
					pickle.dump(vrrepor, alrepor)
					alrepor.flush()
			vroper = pickle.load(alop)
		vrprod = pickle.load(alprod)

def posicionarseEnProd(codigo):                                     ###Funcion para conseguir la posicion
    global alprod, afprod
    p = productos()
    t = os.path.getsize(afprod)
    alprod.seek(0, 0)
    while alprod.tell()<t and p.codigo != codigo:
        pos = alprod.tell()
        p = pickle.load(alprod)
    return pos

def posicionarse_silo(producto):
	global afsilos, alsilos
	t = os.path.getsize(afsilos)
	vrsil = silo()

	pos = -1

	if t == 0:
		pos = -1
	else:
		while alsilos.tell() < t and int(vrsil.codProd) != producto:
			pos = alsilos.tell()
			vrsil = pickle.load(alsilos) 
	
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

def BusqDic(codigoRubro):
    global afrub, alrub, vrrubro
    vrrubro = rubro()
    alrub.seek(0)
    t = os.path.getsize(afrub)

    if t == 0:
        return False

    vrrubro = pickle.load(alrub)
    tamReg = alrub.tell()
    cantReg = t // tamReg

    inicio = 0
    fin = cantReg-1
    encontrado = False
    while not encontrado and inicio <= fin:
        medio = (inicio + fin) // 2
        alrub.seek(medio*tamReg, 0)
        vrrubro = pickle.load(alrub)
        pos = alrub.tell()
        if int(vrrubro.codigo) == codigoRubro:
            encontrado = True
        else:
            if codigoRubro < (int(vrrubro.codigo)):
                fin = medio - 1
            else:
                inicio = medio + 1
    if int(vrrubro.codigo) == codigoRubro:
        return codigoRubro
    else:
        codigoRubro = -1
        return codigoRubro

def Busqxd(patente):
    global alop, afop
    vrop = operaciones()

    t = os.path.getsize(afop)
    alop.seek(0)
    vrop = pickle.load(alop)

    while (alop.tell() < t) and (vrop.patente != patente):
        pos = alop.tell()
        vrop = pickle.load(alop)
    if vrop.patente == patente:
        vrop.estado == "P"
        pos = alop.tell()
    else:
        pos = -1
    return pos

def BusqCProd(patente):
    global afop, alop, vrop
    vrop = operaciones()
    t = os.path.getsize(afop)
    alop.seek(0,0)
    if t != 0:
        while (alop.tell() < t) and (vrop.patente != patente):
            pos = alop.tell()
            vrop = pickle.load(alop)
    if (vrop.patente == patente):
        if vrop.estado == "A":
            codpro = int(vrop.codProd)
            return codpro
        else:
            print("No se encuentra en estado arribado.")
            codpro = -1
    else:
        codpro = -1
    return -1

def BusqCProd2(cod):
    global afrubxprod, alrubxprod
    vrRxP = rubros_x_producto()
    t = os.path.getsize(afrubxprod)
    alrubxprod.seek(0,0)
    if t != 0:
        while (alrubxprod.tell() < t) and (vrRxP.codRubro != cod):
            pos = alop.tell()
            vrRxP = pickle.load(alrubxprod)
        if (vrRxP.codRubro == cod):
            return pos
        else:
            print("No se ha encontrado el rubro.")
            return -1

def BusqPat(patente):
    global alop, afop
    vrop = operaciones()

    t = os.path.getsize(afop)
    alop.seek(0)
    vrop = pickle.load(alop)

    while (alop.tell() < t) and (vrop.patente != patente):
        pos = alop.tell()
        vrop = pickle.load(alop)
    if vrop.patente == patente:
        pos = alop.tell()
    else:
        pos = -1
    return pos


###--------------------------------------------------------- ###

###--- Declaracion de metodos de validacion ---###

def validarPatente (patente):                                        ###Funcion para validar largo de la patente
    r = False
    if (len(patente) >= 6) and (len (patente) <= 7):
        r = True
        return r
    else:
        print ("La patente ingresada no es valida")
        return r

def validarProd(codigo):
    global alprod, afprod
    vrprod = productos()
    t = os.path.getsize(afprod)
    r = False
    alprod.seek(0,0)
    while codigo != vrprod.codigo and alprod.tell() < t:
        if codigo == vrprod.codigo:
            r = True
        vrprod = pickle.load(alprod)
    return r

def validarExisteFecha(fecha, patente):
    global alop, afop
    vrop = operaciones()
    t = os.path.getsize(afop)
    r = False
    if t == 0:
        r = False
    else:
        alop.seek(0,0)
        while alop.tell() < t and r == False:
            if vrop.patente == patente:
                if vrop.fechaCupo == fecha:
                    r = True
                else:
                    vrop = pickle.load(alop)
            else:
                vrop = pickle.load(alop)
    return r


###--------------------------------------------------------- ###

###--- Declaracion de altas, bajas, modificacion y consulta para administracion ---###

def CargaSilos(Tara, Bruto, codpro):
	global afsilos, alsilos
	vrsilos = silo()
	neto = Bruto - Tara
	posicion = posicionarse_silo(codpro)
	if posicion != -1:
		alsilos.seek(posicion, 0)
		vrsilos.stock += neto
		formatearSilos(vrsilos)
		pickle.dump(vrsilos, alsilos)
		alsilos.flush()
	else:
		print("No se pudo cargar el silo")

def altaProd():
    global alprod, afprod
    vrprod = productos()
    t = os.path.getsize(afprod)
    if t == 0:
        vrprod.nombre = str (input("Ingrese el nombre del producto. 0 para salir"))
        vrprod.nombre = vrprod.nombre.upper()
        while  vrprod.nombre!= "0":
            vrprod.codigo = input("Ingrese codigo del producto")
            vrprod.estado = True
            formatearprod(vrprod)
            pickle.dump(vrprod,alprod)
            alprod.flush()
            vrprod.nombre = str (input("Ingrese el nombre del producto. 0 para salir"))
            vrprod.nombre = vrprod.nombre.upper()
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
    os.system("cls")
    printmenuterciario()

def altaRubros():
    global afrub, alrub
    vrrubro= rubro()
    t = os.path.getsize(afrub)
    if t == 0:
        vrrubro.codigo = int(input("Ingrese el código del rubro. 0 para cancelar. "))
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
    os.system("cls")
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
    os.system("cls")
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
    os.system("cls")
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
    os.system("cls")
    printmenuterciario()

def consultaProd():
    global afprod, alprod, vrprod
    t = os.path.getsize(afprod)
    print("Listado de productos\n")
    alprod.seek(0,0)
    while alprod.tell() < t:
        vrprod = pickle.load(alprod)
        print(vrprod.nombre, vrprod.codigo)
    os.system("cls")
    printmenuterciario()

def modProd():
    global afprod, alprod
    vrprod = productos()
    t = os.path.getsize(afprod)
    alprod.seek(0,0)
    if t != 0:
        codigo = (input("Ingrese el codigo del producto a cambiar. 0 para salir"))
        while codigo != 0: 
            pos = posicionarseEnProd(codigo)
            alprod.seek(pos)
            vrprod.codigo = int (input("Ingrese el nuevo codigo para el producto"))
            vrprod.nombre = str (input("Ingrese el nuevo nombre para el producto"))
            vrprod.nombre = vrprod.nombre.upper()
            formatearprod(vrprod)
            pickle.dump(vrprod,alprod)
            alprod.flush()
            codigo = (input("Ingrese el codigo del producto a cambiar. 0 para salir"))
    os.system("cls")
    printmenuadmin()


###--------------------------------------------------------- ###

###--- Declaracion de metodos para los menus terciarios dentro de administracion ---###

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
    os.system("cls")
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
            oprubros = input("Ingrese una opcion: ")
            oprubros = oprubros.upper()
    os.system("cls")
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
            oprubrosxProd = input("Ingrese una opcion: ")
            oprubrosxProd = oprubrosxProd.upper()
    os.system("cls")
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
            opsilos = input("Ingrese una opcion: ")
            opsilos = opsilos.upper()
    os.system("cls")
    printmenuadmin()


###--------------------------------------------------------- ###

###--- Declaracion del metodo para el menu principal--###

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
    os.system("cls")
    printmenuprincipal()

def EntregaCupos():
    global afop, alop
    vrop = operaciones()
    t = os.path.getsize(afop)
    patenteAux = str (input("Ingrese la patente para solicitar el cupo. 0 para salir\n"))
    patenteAux = patenteAux.upper()
    while patenteAux != "0":
        if validarPatente(patenteAux) != False:
            codigoAux = int (input("Ingrese el codigo del producto a entregar\n"))
            if validarProd(codigoAux) != True:
                fechaAux = str (input("Ingrese la fecha para el cupo en el formato 'aaaa-mm-dd'\n"))
                fechaAux = datetime.date.fromisoformat(fechaAux)
                print(fechaAux)
                if validarExisteFecha(fechaAux, patenteAux) == False :
                    if t == 0:
                        vrop.patente = patenteAux
                        vrop.codProd = codigoAux
                        vrop.fechaCupo = fechaAux
                        vrop.estado = "P"
                        formatearoperaciones(vrop)
                        print (vrop.fechaCupo)
                        pickle.dump(vrop,alop)
                        alop.flush()
                    else:
                        alop.seek(t)
                        vrop.patente = patenteAux
                        vrop.codProd = codigoAux
                        vrop.fechaCupo = fechaAux
                        vrop.estado = "P"
                        formatearoperaciones(vrop)
                        pickle.dump(vrop,alop)
                        alop.flush()
                else:
                    print("Ya hay un cupo otorgado en esa fecha")
            else:
                print("Ingrese un codigo de producto valido")
        elif patenteAux == "F":
            alop = open(afop, "w+b")
        else:
            print("Ingrese la patente correctamente")
            patenteAux = 0
        patenteAux = str (input("Ingrese la patente para solicitar el cupo. 0 para salir\n"))
        patenteAux = patenteAux.upper()
    os.system("cls")
    printmenuprincipal()

def Reception():
    global alop, afop
    vrop = operaciones()
    optionRep = input("Desea seguir con el menú de Recepción, S o N: ")
    optionRep = optionRep.upper()
    while optionRep != "N":
        patente = input("Ingrese la patente")
        patente = patente.upper()
        while (not validarPatente(patente)):
            print("Ingrese una patente válida:")
            patente = input("Ingrese la Patente del camión: ")
        

        alop.seek(0, 0)
        aux = pickle.load(alop)
        tamReg = alop.tell() 

        Pos = Busqxd(patente)
        
        if (Pos != -1):
            alop.seek(Pos-tamReg, 0)
            vrop = pickle.load(alop)
            alop.seek(Pos, 0)
            if datetime.date.today() == vrop.fechaCupo:
                vrop.estado = "A"
                alop.seek(Pos-tamReg, 0)
                formatearoperaciones(vrop)
                pickle.dump(vrop,alop)
                alop.flush()
                print("El camión se encuentra en estado Arribado")
            else:
                print("Este camión no tiene esta fecha asignada.")
        else:
            print("La patente no se encuentra en estado Pendiente.")
        optionRep = input("Desea seguir con el menú de Recepción, S o N: ")
        optionRep = optionRep.upper()
    os.system("cls")
    printmenuprincipal()

def RegistrarCalidad():
    global afop, alop, afprod, alprod, vrRxP, Cont
    vrprod= productos()
    vrop = operaciones()
    vrrubro = rubro()
    vrRxP = rubros_x_producto()
    alop.seek(0, 0)
    aux = pickle.load(alop)
    tamReg = alop.tell()

    option = str(input("¿Desea continuar? S/N"))
    option = option.upper()
    while option != "N":
        
        Cont = 0
        patente = input("Ingrese la Patente del camión: ")
        patente = patente.upper()
        while (not validarPatente(patente)):
            print("Ingrese una patente válida:")
            patente = input("Ingrese la Patente del camión: ")
        
        alop.seek(0, 0)
        aux = pickle.load(alop)
        tamReg = alop.tell() 

        codprod = BusqCProd(patente)
         
        if (codprod != -1):   
            alrubxprod.seek(0)
            vrRxP = pickle.load(alrubxprod)
            t = os.path.getsize(afrubxprod)
            while alrubxprod.tell() < t and vrRxP.codProd != codprod:
                vrRxP = pickle.load(alrubxprod)
            
            if int(vrRxP.codProd) == codprod:
                aux = int(vrRxP.codRubro)
                s = os.path.getsize(afrub)
                alrub.seek(0)
                while alrub.tell() < s and option != "N":
                    Cod = BusqDic(aux)
                    if Cod != -1:      #REVISAR IF, NO SÉ SI ES POSIBLE QUE TENGA -1#
                        vrrubro.codigo = Cod
                        print(vrrubro.codigo)
                        print(vrrubro.nombre)        #NO IMPRIME NOMBRE#
                    else:
                        print("No se ha encontrado rubro cargado en el archivo")    
                    
                    alrubxprod.seek(0)
                    t = os.path.getsize(afrubxprod)
                    while alrubxprod.tell() < t and option != "N":
                        cod = int(input("Ingrese el codigo del Rubro a comparar, 0 terminar: "))   #Preguntar si va a ir avanzando uno por uno con el load y comparando a todos#
                        pos = 0
                        while cod !=0 and pos !=1:
                            pos = BusqCProd2(cod)
                            if pos != -1:
                                alrubxprod.seek(pos, 0)
                                valor = int(input("Ingrese un Valor: "))
                                if int(vrRxP.max) > valor and int(vrRxP.min) < valor:
                                    print("El producto es apto.")
                                else:
                                    Cont = Cont + 1
                                    vrRxP = pickle.load(alrubxprod)
                                    if Cont >= 2:
                                        print("Este camión no es apto. Su estado es actualizado a Rechazado.")
                                        vrop.estado = "R"
                                        option = "N"
                                cod = int(input("Ingrese el codigo del Rubro a comparar, 0 terminar: "))
                        option = str(input("¿Desea continuar? S/N"))
                        option = option.upper()      
                    if Cont < 2:
                        alop.seek(pos-tamReg, 0)
                        vrop = pickle.load(alop)
                        alop.seek(pos, 0)
                        print("El producto cumple con las condiciones.")
                        vrop.estado = "C"
                        formatearoperaciones(vrop)
                        pickle.dump(vrop,alop)
                        alop.flush()
            else:
                print("Este camión no se encuentra en Estado Arribado")
                option = str(input("¿Desea continuar? S/N"))
                option = option.upper()
        else:
            print("No se ha encontrado un camión con esa patente registrada.")
            option = str(input("¿Desea continuar? S/N"))
            option = option.upper()
    os.system("cls")
    printmenuprincipal()

def registrarBruto():
    global afop, alop
    vrop = operaciones()
    t = os.path.getsize(afop)

    alop.seek(0, 0)
    aux = pickle.load(alop)
    tamReg = alop.tell() 

    patenteAux = str (input("Ingrese la patente a la que se quiere registrar el peso bruto. \n 0 para salir: "))
    patenteAux = patenteAux.upper()
    while patenteAux != "0":
        pos = BusqPat(patenteAux)
        if pos != -1:
            alop.seek(pos-tamReg, 0)
            vrop = pickle.load(alop)
            alop.seek(pos, 0)
            if vrop.estado == "C":
                vrop.estado = "B"
                alop.seek(pos-tamReg, 0)
                vrop.bruto = int(input("Ingrese el peso bruto del camion: "))
                formatearoperaciones(vrop)
                pickle.dump(vrop,alop)
                alop.flush()
                print("Se encuentra cargado el peso bruto del camion y se actualizo su estado")
            else:
                print("El caminion no tiene registrada su calidad")
                patenteAux = str (input("Ingrese la patente a la que se quiere registrar el peso bruto. \n 0 para salir: "))

def RegistrarTara():
    global afop, alop
    vrop = operaciones()
    t = os.path.getsize(afop)

    alop.seek(0, 0)
    aux = pickle.load(alop)
    tamReg = alop.tell() 

    patenteAux = str (input("Ingrese la patente a la que se quiere registrar la tara. \n 0 para salir: "))
    patenteAux = patenteAux.upper()
    while patenteAux != "0":
        pos = BusqPat(patenteAux)
        if pos != -1:
            alop.seek(pos-tamReg, 0)
            vrop = pickle.load(alop)
            alop.seek(pos, 0)
            if vrop.estado == "B":
                vrop.estado = "F"
                alop.seek(pos-tamReg, 0)
                vrop.tara = int(input("Ingrese la tara del camion: "))
                if vrop.tara >= int(vrop.bruto):
                    vrop.tara = int(input("Ingrese un valor de tara válido: "))
                else:
                    CargaSilos(vrop.tara, int(vrop.bruto), int(vrop.codpro))
                    vrop.estado = "F"
                    formatearoperaciones(vrop)
                    pickle.dump(vrop, alop)
                    alop.flush()
                    formatearoperaciones(vrop)
                    pickle.dump(vrop,alop)
                    alop.flush()
                    print("Se encuentra cargado la tara del camion y se actualizo su estado a finalizado")
            else:
                print("El caminion no tiene registrado su peso bruto")
                patenteAux = str (input("Ingrese la patente a la que se quiere registrar la tara. \n 0 para salir: "))
    os.system("cls")
    printmenuprincipal()

def reportes():
	global afreportes, afprod, alprod, canttot, cantrec
	calculos()
	alrepor = open(afreportes, "r+b")
	Trepor = os.path.getsize(afreportes)
	vrrepor = reportes()
	vrprod = productos()
	vrsil = silo()
	print("REPORTES")
	if Trepor == 0:
		print("No hay Datos cargados")
	else:
		print("Cantidad de cupos otorgados: ", canttot)
		print("Cantidad de camiones recibidos: ", cantrec)
		while alrepor.tell() < Trepor:
			posicionnombre= posicionarseEnProd(int(vrrepor.codpro))
			posicionsilo = posicionarse_silo(int(vrrepor.codpro))
			alprod.seek(posicionnombre,0)
			alsilos.seek(posicionsilo,0)
			print("Cantidad de camiones de ",vrprod.nombre, ": ",vrrepor.contprod)
			print("Peso neto total de ",vrprod.nombre,": ", vrsil.stock)
			if int(vrrepor.contprod) != 0:
				print("Promedio del peso neto de ",vrprod.nombre,"por camión: ", (int(vrsil.stock)/int(vrrepor.contprod)))
			print("Patente del camión que menor cantidad ",vrprod.nombre," descargó: ", vrrepor.patmen)
			vrrepor = pickle.load(alrepor)

def listadosilosyrec():
	global afop, alop, afsilos, alsilos
	
	print("Listado de Silos y Rechazados")
	print("1- Silo con mayor cantidad de Producto \n 2- Camiones rechazados por fecha")
	opcion = int(input("Ingrese una opción: "))
	while opcion <= 0 or opcion >= 3:
		opcion = int(input("Ingrese una opción válida: "))
	
	if opcion == 1:
		Tsilo = os.path.getsize(afsilos)
		mayor = 0
		vrsil = silo()
		while alsilos.tell() < Tsilo:
			if vrsil.stock >= mayor:
				mayor = vrsil.stock
				pos = alsilos.tell()
			vrsil = pickle.load(alsilos)
		alsilos.seek(pos, 0)
		print("El silo con mayor Stock es: ",vrsil.codSilo, vrsil.nombre, vrsil.codProd, vrsil.stock )
	
	elif opcion == 2:
		Toper = os.path.getsize(afop)
		vrop = operaciones()
		fecha = str(input("Ingrese una fecha (aa/mm/dd): "))
		print("Camiones rechazados en la fecha: ", fecha)
		while alop.tell() < Toper:
			if vroper.fechac.strip() == fecha and vroper.est.strip() == "R":
				print(vroper.pat)
			vroper = pickle.load(alop)

def menuPrincipal():            
    printmenuprincipal()
    opcionprincipal = int(input("Ingrese la opcion que desee: "))
    while opcionprincipal != 0:
        if opcionprincipal == 1:
            admin()
        elif opcionprincipal == 2:
            EntregaCupos()
        elif opcionprincipal == 3:
            Reception()
        elif opcionprincipal == 4:
            RegistrarCalidad()
        elif opcionprincipal == 5:
            registrarBruto()
        elif opcionprincipal == 6:
            print("Proceso en construccion")
        elif opcionprincipal == 7:
            RegistrarTara()
        elif opcionprincipal == 8:
            print()#Reportes
        elif opcionprincipal == 9:
            print()#ListSilosyRechazos
        opcionprincipal = int(input("Ingrese la opcion que desee: "))
    if opcionprincipal == 0:
        cerrar()

menuPrincipal()