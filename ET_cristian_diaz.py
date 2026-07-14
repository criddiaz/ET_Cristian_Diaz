#git push
#git commit -m ""  

def main():
    prendas = {
    'S001': ['Polera Basica', 'polera', 'M', 'negro', 'algodon',
    True],
    'S002': ['Jeans Slim', 'pantalon', 'L', 'azul', 'denim', False],
    'S003': ['Chaqueta Urban', 'chaqueta', 'M', 'gris', 'poliester',
    True],
    'S004': ['Vestido Sol', 'vestido', 'S', 'rojo', 'lino', False],
    'S005': ['Poleron Cozy', 'poleron', 'XL', 'verde', 'algodon',
    True],
    'S006': ['Camisa Formal', 'camisa', 'M', 'blanco', 'algodon',
    False],
    
    }
    bodega = {
        'S001': [7990, 12],
        'S002': [19990, 0],
        'S003': [29990, 3],
        'S004': [24990, 6],
        'S005': [17990, 8],
        'S006': [14990, 2],

        }
    
    menu(prendas, bodega)

def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese la opción que desea: "))
            if opcion >= 1 or opcion <= 6:
                return opcion
                
            else:
                print("Debe seleccionar una opción válida")
        except:
            print("El valor debe ser un entero del 1 al 6")

def eliminar_hechizos(bodega, prendas, codigo):
    if buscar_codigo(prendas, bodega, codigo):
        for datos in list(bodega.keys()):
            del prendas[datos]
            del bodega[datos]
            print("El codigo se ha eliminado")
            return True
    print("No se encontro el codigo")
    return False



def actualizar_precio(codigo, nuevo_precio, prendas, bodega):
    if buscar_codigo(prendas, bodega,codigo):
        for clave in prendas:
            if clave.lower() == codigo.lower():
                bodega[clave][0] = nuevo_precio
                print("Precio actualizado")
                return True
    print("El codigo no existe")        
    return False


def unidades_categoria(prendas, bodega, categoria):
    total_unidades = 0
    encontrado = False
    for codigo, datos in prendas.items():
        if datos[1].lower() == categoria .lower():
            total_unidades += bodega[codigo][1]
            encontrado = True
    if encontrado:
        print(f"El total de unidades disponibles es: {total_unidades}")
    else:
        print(f"No se encontro ninguna categoria llamada {categoria}")

def buscar_codigo(prendas,bodega, codigo,):
    for datos in prendas:
        if datos.lower() == codigo.lower():
            return True
    return False

def agregar_prenda(prendas, bodega, codigo, nombre, categoria, talla,color, material, es_unisex, precio,unidades):
    if buscar_codigo(prendas,bodega, codigo):
        print("El código ya existe")
        return False
    talla_int = int(talla)
    precio_int = int(precio)
    unidades_int = int(unidades)
    es_unisex_bool = True if es_unisex.lower() == "s" else False

    prendas[codigo] = (nombre, categoria, talla_int, color, material, es_unisex_bool)
    bodega[codigo] = (precio_int, unidades_int)
    print("Prenda agregada")
    return True

def validar_codigo(codigo):
    
    if codigo.strip() != " ":
        return False
    
    return True
    
def validar_nombre(nombre):
    if nombre.strip() != "":
        return False
    else:
        return True
    
def validar_talla(talla):
    if talla.strip() != "":
        return False
    else:
        return True

def validar_color(color):
    if color.strip() != "":
        return False
    else:
        return True
    
def validar_color(material):
    if material.strip() != "":
        return False
    else:
        return True
    
def validar_es_unisex(es_unisex):
    if es_unisex == "s":
        return True
    elif es_unisex =="n":
        return False
    
def validar_precio(precio):
    try:
        if precio > 0:
            return True
        else:
            return False
    except ValueError:
        print("Debe ingresar numero entero")
    
def validar_unidades(unidades):
    try:
        if unidades >= 0:
            return True
        else:
            return False
    except ValueError:
        print("Debe ingresar numeros enteros")

def validar_categoria(categoria):
    if categoria.strip() != "":
        return False
    return True

def validar_material(material):
    if material.strip() != "":
        return False
    return True

def busqueda_precio(prendas,bodega,min_p,max_p):
    lista_final = []
    for codigo, datos in bodega.items():
        precio = datos[0]
        stock = datos[1]
        if min_p <= precio <=max_p and stock > 0:
            nombre_prenda = prendas[codigo][0]
            lista_final.append(f"{nombre_prenda}--{codigo}")
    if lista_final:
        lista_final.sort()
        print(f"Las prendas que hay en el rango de precio son: {lista_final}")
    else:
        print("No hay prendas en ese rango de precios")

def menu(prendas, bodega):
    while True:
        print("========== MENÚ PRINCIPAL ==========")
        print("1. Unidades por categoría")
        print("2. Búsqueda de prendas por rango de precio")
        print("3. Actualizar precio de prenda")
        print("4. Agregar prenda")
        print("5. Eliminar prenda")
        print("6. Salir")
        print("=====================================")

        opc = leer_opcion()

        if opc == 1:
            categoria = input("Ingrese categoría a consultar: ")
            unidades_categoria(prendas, bodega, categoria)
        elif opc == 2:
            while True:
                try:
                    min_p = int(input("Ingrese el precio minimo: "))
                    max_p = int(input("Ingrese el precio maximo: "))
                    if min_p >= 0 and max_p >= min_p:
                        busqueda_precio(prendas, bodega, min_p, max_p)
                        break
                    else:
                        print("Los valores deben ser positivos")
                except ValueError:
                    print("Debe ingresar valores enteros")
        elif opc == 3:
            codigo = input("Ingrese el codigo de la prenda: ").lower()
            try:
                nuevo_precio = int(input("Ingrese el precio nuevo: "))
                if nuevo_precio > 0:
                    actualizar_precio(codigo, nuevo_precio, prendas, bodega)
                else:
                    print("El valor debe ser superior a 0")
            except ValueError:
                print("Ingrese un valor entero ")
        elif opc == 4:
            codigo = input("Ingrese el codigo: ")
            nombre = input("Ingrese el nombre: ")
            categoria = input("Ingrese la categoria: ")
            talla = input("Ingrese la talla: ")
            color = input("Ingrese el color: ")
            material = input("Ingrese el material: ")
            es_unisex = input("Ingrese si es unisex (s/n): ")
            precio = input("Ingrese el precio: ")
            unidades = input("Ingrese las unidades: ")

            if not validar_codigo(codigo):
                print("El codigo contiene espacios")
            elif not validar_nombre(nombre):
                print("El Nombre contiene espacios")
            elif not validar_categoria(categoria):
                print("La categoria contiene espacios")
            elif not validar_talla(talla):
                print("Ponga un numero positivo")
            elif not validar_color(color):
                print("El Color contiene espacios")
            elif not validar_material(material):
                print("El Material contiene espacios")
            elif not validar_es_unisex(es_unisex):
                print("No es unisex la ropa")
            elif not validar_precio(precio):
                print("El precio debe de ser un numero positivo")
            elif not validar_unidades(unidades):
                print("El precio debe de ser un numero positivo mayor o igual a 0")
            else:
                agregar_prenda(codigo, nombre, categoria, talla, color, material, es_unisex, precio, unidades)

        elif opc == 5:
            codigo = input("Ingrese el codigo: ")
            eliminar_hechizos(bodega, prendas, codigo)

        elif opc == 6:
            print("Programa finalizado.")
            break






if __name__=="__main__":
    main()