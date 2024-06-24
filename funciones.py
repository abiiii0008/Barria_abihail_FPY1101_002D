import time
# Definimos una lista para almacenar los trabajadores registrados
biblioteca = [];
#Comenzamos con el proceso de crear funciones
def agregar_libro():#funcion de agregar un libro
    nombre = input(" --// Ingrese Nombre del Libro : ").lower();
    autor = input(" -- // Ingrese el Autor del Libro  : ").lower();
    año = input(" -- // Ingrese el año de publicación : ");
    genero = input(" -- // Ingrese el Genero del libro : ").lower();
    #Creamos un diccionario con los parametros asignados anteriormente
    libro = {    
        "Nombre del libro": nombre,
        "Autor": autor,
        "Año de publicacion": año,
        "Genero": genero,
    }
    #almacenamos los datos en una lista
    biblioteca.append(libro)    
    print(" ---- Libro Agregado con exito a la Biblioteca ----");#mensaje de comprobación

def lista_libros(biblioteca): #Funcion de ver la lista de libros
    print(f"{'Nombre del libro':<20} {'Autor':<20} {'Año de publicación':<15} {'Genero':<25}");
    print("_" * 105) # linea de separacion 
    for libro in biblioteca: #Creamos un bucle que va imprimiendo los libros en el o
        print(f"{libro['Nombre del libro']:<20}  {libro['Autor']:<20}{libro['Año de publicacion']:<15} {libro['Genero']:<25}");

def modificar_libro(biblioteca):#Funcion de modificar un libro
    nombre_libro=input("Ingrese el nombre del libro que desea modificar: ").lower();
    for libro in biblioteca:#Creamos una sentencia de rep para verificar que el libro ingresado se enc
        if libro['Nombre del libro'] == nombre_libro:#mandamos a buscar el 
            nuevo_autor = input("Nuevo autor: ")
            nuevo_año = input("Nuevo año de publicación: ")
            nuevo_genero = input("Nuevo género: ")
            libro["Autor"] = nuevo_autor
            libro["Año de publicacion"] = nuevo_año
            libro["Genero"] = nuevo_genero
            print(f"Libro '{nombre_libro}' actualizado con éxito.")
            break  # Importante: salir del bucle una vez que se encuentra el libro
    else:
        print(f"No se encontró el libro '{nombre_libro}' en la biblioteca.")

def guardar_colleccion(biblioteca):#Creacion de Archivo TXT.
    with open('biblioteca.txt','w',encoding='utf-8',newline='') as archivo:
        archivo.write(f"{'Nombre':<20}{'Autor':<20}{'Año de publicacion':<15}{'Genero':<25}"); #Creacion de TITULOS
        archivo.write("-" * 105 + "\n") # Linea de separacion 
        
        for libro in biblioteca: #Bucle que va escribiendo en el archivo.txt
                archivo.write(f"{libro['Nombre del libro']:<20} {libro['Autor']:<20}{libro['Año de publicacion']:<15} {libro['Genero']:>25} ");
    print(" Creando el archivo"),time.sleep(2);#Mensaje de salida
    print(" Cargando ..."),time.sleep(1);#Mensaje de salida

def eliminar_libro(biblioteca):#Funcion para eliminar un libro de la lista
    nombre_libro=input("Ingrese el nombre del libro que desea eliminar: ").lower();
    for libro in biblioteca:
        if libro['Nombre del libro'] == nombre_libro:
            biblioteca.remove(libro);
            print(" -- // -- Libro Borrado ocon Exito --//-- ");
        else:
            print(" -- // -- No se encontro el libro --//-- ")
    

def menu(biblioteca):
    while True: #Hud de bienvenida
        print("_" * 105);
        print(" -- // ---- Biblioteca -------\n");
        print(" -- // 1) Agregar Libro ------");
        print(" -- // 2) Ver Libros ---------");
        print(" -- // 3) Modificar Libro ----");
        print(" -- // 4) Eliminar Libro -----");
        print(" -- // 5) Guardar Colleccion -");
        print(" -- // 6) Salir --------------");
        print("_" * 106);
        #try/except que nos ayudara a evitar errores
        try:
            opciones=int(input("\n -- // -- Ingrese: "));
        except:
            print("\n -- // -- El comando ingresado no es valido  -- // --");
        else:
            if (opciones==1):# Registramos los libros en la lista
                agregar_libro()

            elif(opciones==2):# Muestra Lista de libros
                print("\n\n");
                print("_" * 105);
                lista_libros(biblioteca);
                print("_" * 105);
                print("\n\n");
            elif(opciones==3):#modifica un libro ingresado
                modificar_libro(biblioteca);
            elif(opciones==4):#Elimina un libro de la lista
                eliminar_libro(biblioteca)
            elif (opciones==5):#Guarda una colección a un archivo txt
                guardar_colleccion(biblioteca);
                print(" -- // --  El archivo a sido creado con exito -- // -- ")
            else:
                break;
