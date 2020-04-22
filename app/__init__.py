#duplicados.py

import os
import sys
import hashlib
 
def duplicados(parentFolder):
    """
    Función *duplicados* se utiliza en la opción "2" del :func:`menu`.  Esta función identifica archivos duplicados al generar un hash utilizando el algoritmo SHA256 para cada archivo evaluado.  Si el hash se repite entre dos archivos, se marca el duplicado.

    :param parentFolder: Ruta que será utilizada para la busqueda
    :type parentFolder: str
    :return: Retorna diccionario que incluye path, y hash de cada archivo
    :rtype: str

    Variables utilizadas en :func:`duplicados`
    
    :param duplicado: Diccionario que contendrá la ruta de los archivos y los hash generados.
    :param root: Directorio raíz dentro de la busqueda, como parte de funcion :func:`os.walk()`. 
    :type root: str
    :param dirs: Subdirectorios dentro de la busqueda, como parte de función :func:`os.walk()`.
    :type dirs: str
    :param files: Archivos dentro de la busqueda, como parte de función :func:`os.walk()`.
    :type files: str
    :param path: Obtiene la ruta de cada archivo mediante :func:`os.path.join()`.
    :type path: str
    :param nomarchivo: Nombre de archivo dentro de la carpeta buscada (parentFolder).
    :type nomarchivo: str
    :param file_hash: Toma el valor hash generado por :func:`hashfile`.
    :type file_hash: str

    """
    duplicado = {}
    for root, dirs, files in os.walk(parentFolder):
        #Recorrido de carpeta parentFolder
        print ('\nRevisando carpeta:  ', root)
        for nomarchivo in files:
            path = os.path.join(root, nomarchivo)
            # Calcular el hash
            file_hash = hashfile(path)
            # Append del path a diccionario duplicado
            if file_hash in duplicado:
                duplicado[file_hash].append(path)
                print ('*Alerta* Duplicaodos: ', duplicado[file_hash])
            else:
                duplicado[file_hash] = [path]
    return duplicado

def borrado(parentFolder):
    """
    Función *borrado* es utilizada por la opción "2" del :func:`menu`.  Esta función hace una busqueda en la carpeta (parentFolder).  Cada vez que identifique un archivo duplicado mediante el uso del hash SHA256, borra el archivos duplicando.

    :param parentFolder: Ruta que será utilizada para la busqueda
    :type parentFolder: str
    :return: Retorna diccionario que incluye path, y hash de cada archivo
    :rtype: str

    Variables utilizadas en función :func:`borrado`
    
    :param duplicado: Diccionario que contendrá la ruta de los archivos y los hash generados.
    :param root: Directorio raíz dentro de la busqueda, como parte de funcion :func:`os.walk()`. 
    :type root: str
    :param dirs: Subdirectorios dentro de la busqueda, como parte de función :func:`os.walk()`.
    :type dirs: str
    :param files: Archivos dentro de la busqueda, como parte de función :func:`os.walk()`.
    :type files: str
    :param path: Obtiene la ruta de cada archivo mediante :func:`os.path.join()`.
    :type path: str
    :param nomarchivo: Nombre de archivo dentro de la carpeta buscada (parentFolder).
    :type nomarchivo: str
    :param file_hash: Toma el valor hash generado por :func:`hashfile`.
    :type file_hash: str
    """    
    borrador = {}
    for root, dirs, files in os.walk(parentFolder):
        print ('\nBuscando Duplicados:  ', root)
        for nomarchivo in files:
            path = os.path.join(root, nomarchivo)
            file_hash = hashfile(path)
            if file_hash in borrador:
                 print ('\nBorrando archivo duplicado: ' + path)
                 os.remove(path)
            else:
                 borrador[file_hash] = [path]
 
def hashfile(path, bloque = 65536):
    """
    Función *hashfile* se encarga de la abrir los archivo leidos por :func:`duplicados`o :func:`borrado` y genera el hash utilizando el algoritmo SHA256.  Los archivos son cargados en memoria en bloques de 65536 bytes para prevenir un desbordamiento de memoria al abrir archivos muy grandes.

    :param path: Ruta que será utilizada para la busqueda
    :type path: str
    :param bloque: Constante que asigna el tamaño del buffer o bloques de bits que serán leidos en cada archivo.
    :type bloque: int
    :return: Retorna el hash (SHA256) de cada archivo leido.
    :rtype: str

    Variables utilizadas en función :func:`hashfile`
    
    :param archivo: Variable con el archivo que será abierto.
    :param hasher: Permite la generación del hash SHA256. 
    :type hasher: str
    :param buff: Contiene bloques de información de cada archivo.  Al momento de la lectura, cada archivo es partido en bloques que son leidos con variable *buff*.
    :type buff: str

    """   
    archivo = open(path, 'rb')
    hasher = hashlib.sha256()
    buff = archivo.read(bloque)
    while len(buff) > 0:
        hasher.update(buff)
        buff = archivo.read(bloque)
    archivo.close()
    return hasher.hexdigest()

def menu(rutatemp):
    """
    Genera el menú del programa.

    :param rutatemp: Ruta que será utilizada para la busqueda
    :type rutatemp: str

    Variables utilizadas en función :func:`menu`
    
    :param opcion: Variable para la selección de la opción.
    :type opcion: str

    """ 
    while True:
        print ('|---------------------------------|')
        print ('|              MENU               |')
        print ('|---------------------------------|')
        print ('| 1. Listar archivos (Dir/SubDir) |')
        print ('| 2. Listar archivos duplicados   |')
        print ('| 3. Borrar archivos duplicados   |')
        print ('| 4. Cambiar ruta                 |')
        print ('| 0. SALIR                        |')
        print ('|---------------------------------|\n')
        opcion = input ('Seleccionar su opción: ')
        if opcion == '1':
            listdir(rutatemp)
        elif opcion == '2':
            duplicados(rutatemp)
        elif opcion == '4':
            getruta()
        elif opcion == '3':
            borrado(rutatemp)
        elif opcion == '0':
            #break
            sys.exit()
        else:
            print ('Opción no es válida.  Intente nuevamente')
            
def getruta():
    """
    Función *getruta* se encarga de solicitar al usuario la ruta que será revisada por la aplicación para la identificación de los duplicados.  Esta función hace una validación previa si la ruta introducida existe en el sistema operativo o no.

    Variables utilizadas en función :func:`getruta`
    
    :param x: Variable para cotrol del ciclo *while*.
    :type x: str
    :param ruta: Variable que introduce el usuario con la ruta para la búsqueda. 
    :type ruta: str
    :param buff: Contiene bloques de información de cada archivo.  Al momento de la lectura, cada archivo es partido en bloques que son leidos con variable *buff*.
    :type buff: str

    """ 
    x = 1
    while x == 1 :
        ruta = input ('Introduzca la ruta de la carpeta: ')
        isExist = os.path.exists(ruta)
        if isExist:
            x = 0
            menu(ruta)
        else:
            print (ruta + ' no es una ruta válida, por favor introducir la ruta correcta')

def listdir(rutatemp):
    """
    Función *listdir* es usada para listar los archivos en la carpeta seleccionada.

    :param rutatemp: Ruta que será utilizada para la busqueda
    :type rutatemp: str

    Variables utilizadas en función :func:`listdir`
    
    :param contar: Cuenta la cantidad de archivos listados en la(s) carpeta(s) revisada(s).
    :type contar: int
    :param r: Directorio raíz dentro de la busqueda, como parte de funcion :func:`os.walk()`. 
    :type r: str
    :param d: Subdirectorios dentro de la busqueda, como parte de función :func:`os.walk()`.
    :type d: str
    :param f: Archivos dentro de la busqueda, como parte de función :func:`os.walk()`.
    :type f: str
    :param files: Arreglo que consolida la ruta con el nombre de los archivos
    :type files: str

    """ 
    contar = 0
    files = []
    for r, d, f in os.walk(rutatemp):
        for fil in f:
            files.append(os.path.join(r,fil))
        for f in files:
            print (f)
            contar = contar + 1
    print ('\nTotal de archivos revisados: '+ str(contar) + '\n\n')

 
if __name__ == "__main__":
    """
    Inicio del programa que imprime datos del proyecto y hace el llamado a :func:`getruta`.

    :param ruta: Permite el llamado de la función :func:`getruta`.
    :type ruta: str

    """ 
    print ('UNIVERSIDAD INTERAMERICANA')
    print ('PROYECTO FINAL - PROGRAMACIÓN III')
    print ('Por: Rubén Fernández\n\n\n')
    print ('*************************************************')
    print ('* SISTEMA PARA DETECCIÓN DE ARCHIVOS DUPLICADOS *')
    print ('*************************************************\n\n')
    ruta = getruta()