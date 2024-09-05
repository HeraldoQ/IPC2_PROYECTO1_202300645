import os,time
from xml.dom import minidom
archivo = ""
#DEFINICION DE LA CLASE MATRIZ
class matriz1:
    i = 0
    j = 0
    dato = 0
    def __init__(self, nombre, i, j, dato):
        self.nombre = nombre
        self.i = i
        self.j = j
        self.dato = dato


#DEFINICION DE LA CLASE NODO
class nodo:

    #se puede asignar un valor por defecto a los parametros en python
    def __init__(self, matriz1 = None, siguiente = None):
        self.matriz1 = matriz1
        self.siguiente = siguiente


#DEFINICION DE LA CLASE LISTA CIRCULAR

class lista_circular:
    def __init__(self):
        self.primero = None
    
    def insertar(self, matriz1):
        if self.primero is None:
            self.primero = nodo(matriz1 = matriz1)
            self.primero.siguiente = self.primero
        else:
            actual = nodo(matriz1 = matriz1, siguiente = self.primero.siguiente)
            self.primero.siguiente = actual
            
        
    def recorrer(self):
        contadorsss = 0

        if self.primero is None:
            print("La lista esta vacia")
            return
        
        actual = self.primero
        print( actual.matriz1.nombre, " i ", actual.matriz1.i, " j ", actual.matriz1.j, " d: ", actual.matriz1.dato, "\n")        
        contadorsss += 1
        
        
        while actual.siguiente != self.primero:
            actual = actual.siguiente
            print( actual.matriz1.nombre, " i", actual.matriz1.i, " j", actual.matriz1.j, " d: ", actual.matriz1.dato, "\n")         
            contadorsss += 1
        return contadorsss
    
    def recorrer2(self):
        contadorsss = 0

        if self.primero is None:
            print("La lista esta vacia")
            return
        
        actual = self.primero
        contadorsss += 1
        
        
        while actual.siguiente != self.primero:
            actual = actual.siguiente
            contadorsss += 1
        return contadorsss



    def  buscar(self, nombre, i, j):
        actual = self.primero
        anterior = None
        no_encontrado = False

        while actual != None  and (actual.matriz1.nombre != nombre or int(actual.matriz1.i) != i or int(actual.matriz1.j) != j):
            anterior = actual
            actual = actual.siguiente

            if actual == self.primero:
                no_encontrado = True
                
                break
            
        if not no_encontrado:
            #print("nombre encontrado")
            #print(actual.matriz1.nombre, " i ", actual.matriz1.i, " j ", actual.matriz1.j, " d: ", actual.matriz1.dato, "\n")    
            return int(actual.matriz1.dato)
    

    def recorrer3(self, nombre):
        contadorsss = 0

        if self.primero is None:
            print("La lista esta vacia")
            return
        
        actual = self.primero
        
        while True:
            if actual.matriz1.nombre == nombre:
                contadorsss += 1
            
            actual = actual.siguiente
            
            if actual == self.primero:
                break
        
        return contadorsss


    def  buscar2(self, nombre):
        actual = self.primero
        anterior = None
        no_encontrado = False

        while actual != None  and (actual.matriz1.nombre != nombre):
            anterior = actual
            actual = actual.siguiente

            if actual == self.primero:
                no_encontrado = True
                
                break
            
        if not no_encontrado:
            #print("nombre encontrado")
            #print(actual.matriz1.nombre, " i ", actual.matriz1.i, " j ", actual.matriz1.j, " d: ", actual.matriz1.dato, "\n")    
            return actual.matriz1.nombre

    def  editar(self, nombre, i, j, ndato):
        actual = self.primero
        anterior = None
        no_encontrado = False

        while actual != None  and (actual.matriz1.nombre != nombre or int(actual.matriz1.i) != i or int(actual.matriz1.j) != j):
            anterior = actual
            actual = actual.siguiente

            if actual == self.primero:
                no_encontrado = True
                print("No se encontro la matriz1")
                break
            
        if not no_encontrado:

            actual.matriz1.dato = ndato
               
            return actual.matriz1.dato            
    
    def eliminar(self, nombre, i, j):
        if self.primero is None:
            print("La lista está vacía")
            return

        actual = self.primero
        anterior = None
        encontrado = False

        while True:
            if actual.matriz1.nombre == nombre and actual.matriz1.i == i and actual.matriz1.j == j:
                encontrado = True
                break
            anterior = actual
            actual = actual.siguiente
            if actual == self.primero:
                break

        if not encontrado:
            print("No se encontró la matriz1")
            return

        if actual == self.primero and actual.siguiente == self.primero:
            # Solo hay un nodo en la lista
            self.primero = None
        elif actual == self.primero:
            # El nodo a eliminar es el primero
            while actual.siguiente != self.primero:
                actual = actual.siguiente
            actual.siguiente = self.primero.siguiente
            self.primero = self.primero.siguiente
        else:
            # El nodo a eliminar está en el medio o al final
            anterior.siguiente = actual.siguiente

        ###print("Matriz eliminada")

    
    def reemplazar_indices(self, tamaño,tamaño2):
        if self.primero is None:
            print("La lista está vacía")
            return
    
        actual = self.primero
        actual = actual.siguiente
        nuevo_indice = tamaño
        contador = 0
    
        while True:
            actual.matriz1.i = nuevo_indice
            contador += 1
            if contador == tamaño2: #este tamaño lo debo arreglar
                ###print("tamaño: ",tamaño)
                nuevo_indice -= 1
                contador = 0
            actual = actual.siguiente
            if actual == self.primero:
                break
        self.primero.matriz1.i = 1
        nuevo_indice = tamaño
                    


                
    def  editarindices(self, nombre, i, j,ni,nj):
        actual = self.primero
        anterior = None
        no_encontrado = False

        while actual != None  and (actual.matriz1.nombre != nombre or int(actual.matriz1.i) != i or int(actual.matriz1.j) != j):
            anterior = actual
            actual = actual.siguiente

            if actual == self.primero:
                no_encontrado = True
                print("No se encontro la matriz1")
                break
            
        if not no_encontrado:

            actual.matriz1.i = ni
            actual.matriz1.j = nj
               
            return actual.matriz1.dato
def cargar(archivos):
    global archivo
    print("cargando archivo")
    print("archivo cargado")
    archivo = archivos
    o = (input('enter para continuar: '))
    return archivo




lista_c = lista_circular()
lista_b = lista_circular()
lista_f = lista_circular()
lista_ff = lista_circular()
lista_frec = lista_circular()
def cargarArchivo():
    os.system('cls')
    


    #añade a la lista C la matriz original
    xml = minidom.parse("prueba.xml")
    matrices = xml.getElementsByTagName("matriz")
    contador = 0
    
    for matriz in matrices:
        
        dato = matriz.getElementsByTagName("dato")
        
        for i in range(int(matriz.getAttribute("n"))):
            for j in range(int(matriz.getAttribute("m"))):
                
                pos = matriz1(matriz.getAttribute("nombre"), i+1, j+1, dato[contador].firstChild.data)

                lista_c.insertar(pos)
                contador += 1
            
        contador = 0
#n = fila m = columna
      
    print('')
    #recorre y al mismo tiempo añade a la lista B la matriz binaria (no juntar pues sino se entreveran los datos)
    for matriz in matrices:
        print("-------------------------------------------\n\n")
        print(matriz.getAttribute("nombre"),"\n")
        for i in range(int(matriz.getAttribute("n"))):
            for j in range(int(matriz.getAttribute("m"))):
                a = lista_c.buscar(matriz.getAttribute("nombre"), i+1, j+1)


                print(a, ' ', end=' ')
            print()
        print("\nmatriz reducida de ",matriz.getAttribute("nombre"))


        for i in range(int(matriz.getAttribute("n"))):
            for j in range(int(matriz.getAttribute("m"))):
                a = int(lista_c.buscar(matriz.getAttribute("nombre"), i+1, j+1))
                if a >0:
                    a =1
                else:
                    a = 0
                bin = matriz1(matriz.getAttribute("nombre"), i+1, j+1, a)
                lista_b.insertar(bin)
                print(a, ' ', end=' ')
            print()
#N = 5 M = 4

#hacer lo de la coincidencia antes
    #hacemos la matriz 1 primero

    
    coincidencia = 0
    for matriz in matrices:
        
        print("-------------------------------------------\n\n")
        print("\nmatriz final de ",matriz.getAttribute("nombre"),"\n")
        rep = 0
        for i in range(1,int(matriz.getAttribute("n"))+1):
            terc = int(matriz.getAttribute("n"))
            #repitencia de la fila que se esta buscando 
            
            for j in range(int(matriz.getAttribute("n")),i,-1):
                
                for k in range(1,int(matriz.getAttribute("m"))+1):
                    ###print("comparando ", i,k, " y ", terc,k)
                    if int(lista_b.buscar(matriz.getAttribute("nombre"), i, k)) == int(lista_b.buscar(matriz.getAttribute("nombre"), terc, k)):
                        
                        coincidencia += 1
                        #print("coincidencia en ", i,k, " y ", terc,k , " en lista: ",matriz.getAttribute("nombre"))
                
                if coincidencia == int(matriz.getAttribute("m")):
                    ###print("coincidencia= ",coincidencia)
                    for l in range(1,int(matriz.getAttribute("m"))+1):
                        ###print("i y l= ",i,l, "terc y l= ",terc,l)
                        ###print("repeticiones ",rep)
                        if rep >= 1:
                            bs1 = lista_f.buscar(matriz.getAttribute("nombre"), i, l)
                            
                            bs2 = lista_c.buscar(matriz.getAttribute("nombre"), terc, l)
                            bs3 = bs1 + bs2

                            lista_f.editar(matriz.getAttribute("nombre"), i, l, bs3)
                            ###print("editado ",bs3)
                            
                            ###print(lista_f.buscar(matriz.getAttribute("nombre"), i, l))
                            lista_c.editar(matriz.getAttribute("nombre"), terc, l, 0)
                            lista_frec.insertar(matriz1(matriz.getAttribute("nombre")+"s", i, 0, rep)) 
                        
                        else:
                            a =   lista_c.buscar(matriz.getAttribute("nombre"), i, l) + lista_c.buscar(matriz.getAttribute("nombre"), terc, l)
                            ###print("a = ", a)
                            
                            w = matriz1(matriz.getAttribute("nombre"), i, l, a)
                            lista_c.editar(matriz.getAttribute("nombre"), terc, l, 0) 
                            lista_f.insertar(w)
                            ###print("añadido elementos",a)
                            lista_frec.insertar(matriz1(matriz.getAttribute("nombre")+"s", i, 0, rep)) 
                        
                    rep += 1
                elif i == 1 and coincidencia != int(matriz.getAttribute("m")):
                    for m in range(1,int(matriz.getAttribute("m"))+1):
                        
                        j = matriz1(matriz.getAttribute("nombre"), terc, m, lista_c.buscar(matriz.getAttribute("nombre"), terc, m))
                        lista_f.insertar(j)
                        ###print("añadido elementoz",j.dato)
                coincidencia = 0
                terc = terc-1 

                
                 
            rep = 0
        contadorcc = 0
        for i in range(1,int(matriz.getAttribute("n"))+1):
            for j in range(1,int(matriz.getAttribute("m"))+1):
                if (lista_f.buscar(matriz.getAttribute("nombre"), i, j)) == 0:
                    
                    contadorcc += 1
            if contadorcc == int(matriz.getAttribute("m")):
                ###print("eliminando fila ", i)
                for k in range(1,int(matriz.getAttribute("m"))+1):
                    lista_f.eliminar(matriz.getAttribute("nombre"), i, k)
            contadorcc = 0

            
        
        

        


        for i in range(1,int(matriz.getAttribute("n"))+1):
                for j in range(1,int(matriz.getAttribute("m"))+1):
                    if (lista_f.buscar(matriz.getAttribute("nombre"), i, j)) != None:
                        a = matriz1(matriz.getAttribute("nombre"), i, j, lista_f.buscar(matriz.getAttribute("nombre"), i, j))
                        lista_ff.insertar(a)
                    else:
                        break
                    
        #aquí se pone ese código            
                    
            ###print()
        a = lista_ff.recorrer2() / int(matriz.getAttribute("m"))
        ###print("contador de elementos: ",a)
        
        lista_ff.reemplazar_indices(a,int(matriz.getAttribute("m")))

        ###lista_ff.recorrer()
        
        
        for i in range(1,int(a)+1):
                for j in range(1,int(matriz.getAttribute("m"))+1):
                    if (lista_ff.buscar(matriz.getAttribute("nombre"), i, j)) != None:     
                        print(lista_ff.buscar(matriz.getAttribute("nombre"), i, j), ' ', end=' ')
                    
                        
                    
                print()  
        w = lista_ff.recorrer3(matriz.getAttribute("nombre"))/int(matriz.getAttribute("m"))
        print("contador de elementos: ",w)

        

        

#sumarla y hacerla o hacerlas todas 0

        
        #seguir aqui con el codigo:)
        


def escribirxml():
    xml = minidom.parse("prueba.xml")
    matrices = xml.getElementsByTagName("matriz")
    contador = 0

    




    with open("salida.xml", "w") as file_object:
        

       
        file_object.write('<matrices>\n',)
        matrices = xml.getElementsByTagName("matriz")
        
        for matriz in matrices:
            
            w = lista_ff.recorrer3(matriz.getAttribute("nombre"))/int(matriz.getAttribute("m"))
            file_object.write('\t<matriz nombre="'+matriz.getAttribute("nombre")+'" n="'+str(int(w))+'" m="'+matriz.getAttribute("m")+'">\n')
            a = lista_ff.recorrer2()
    
            for i in range(1,a):
                for j in range(1,int(matriz.getAttribute("m"))+1):
                    if (lista_ff.buscar(matriz.getAttribute("nombre"), i, j)) != None:     
                        file_object.write('\t\t<dato x="'+str(i)+'" y="'+str(j)+'">'+str(lista_ff.buscar(matriz.getAttribute("nombre"), i, j))+'</dato>\n')
                    
            for i in range(1,100):
                if (lista_frec.buscar(matriz.getAttribute("nombre")+"s", i, 0)) != None:     
                            file_object.write('\t\t<Frecuencia g="'+str(i)+'">'+str(lista_frec.buscar(matriz.getAttribute("nombre")+"s", i, 0))+'</frecuencia>\n')
                        
                    
                
            file_object.write('\t</matriz>\n')
            file_object.write('\n') 
            
        file_object.write('</matrices>\n')
        file_object.close()


def main():
   
    os.system('cls')

    
    print("---------- Menu Principal P----------")
    print('1. Cargar Archivo')
    print('2. Procesar Archivo')
    print('3. Escribir Archivo de Salida')
    print('4. Mostrar Datos del Estudiante')
    print('5. Generar Grafica')
    print('6. Salir')
    print('------------------------------------')

    opcion = (input('Seleccione una opcion: '))

    

    try:
        opcion = int(opcion)
    except ValueError:
        opcion = 0 


    while True:

        if int(opcion) != 1 and int(opcion) != 2 and int(opcion) != 3 and int(opcion) != 4 and int(opcion) != 5 and int(opcion) != 6 :
            os.system('cls')
            print('Opcion no valida')
            print('///////////////////////////////////////////////////////////////////')
            print('')
            print("---------- Menu Principal ----------")
            print('1. Cargar Archivo')
            print('2. Procesar Archivo')
            print('3. Escribir Archivo de Salida')
            print('4. Mostrar Datos del Estudiante')
            print('5. Generar Grafica')
            print('6. Salir')
            print('------------------------------------')

            opcion = (input('Seleccione una opcion: ')) 
            try:
             opcion = int(opcion)
            except ValueError:
                opcion = 0 

        
        
        else:    
            break
        
    
    if opcion == 1:
        print('Cargar Archivo')
        archivo = input('Ingrese el nombre del archivo con extensión: ')
        cargar(archivo)
        o = (input('enter para continuar: '))
        os.system('cls')
        main()
    elif opcion == 2:
        print('Procesar Archivo')
        cargarArchivo()
        o = (input('enter para continuar: '))
        os.system('cls')
        main()
    elif opcion == 3:
        print('Escribir Archivo de Salida')
        escribirxml()
        o = (input('enter para continuar: '))
        os.system('cls')
        main()
    elif opcion == 4:
        print('Mostrar Datos del Estudiante')
        o = (input('enter para continuar: '))
        os.system('cls')
        main()
    elif opcion == 5:
        print('Generar Grafica')
        o = (input('enter para continuar: '))
        os.system('cls')
        main()
    elif opcion == 6:
        print('Saliendo...')
        o = (input('enter para continuar: '))
        os.system('cls')
        exit()


main()

