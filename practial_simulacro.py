inventario = [
    

]
# HOLA

def mostrar_menu():
    '''
    funcion que sirve para mostrar el menu 
    dependiendo la opcion llama distintas funciones
    si se elige una opcion incorrecta repite el bucle
    
    no recibe parametros ni retorna valores
    '''
    opcion = ""

    while opcion != "6":   
        print('''
1• Cargar producto/s.
2• Buscar producto.
3• Ordenar inventario.
4• Mostrar producto más caro y más barato.
5• Mostrar productos con precio mayor a 15000.
6• Salir

        ''')
            

        opcion = input("Ingrese la opcion deseada: ")

        match opcion:

            case "1":
                cargar_producto()
        

            case "2":
                realizar_busqueda()

            case "3":
                organizar_inventario()

            case "4":
                    
                mostrar_mas_caro_y_barato()

            case "5":
                mostrar_productos_15000()

            case "6":
                print("Siga utilizando Empire inventory")
                return
            
            case _:
                print("Opcion erronea, ingrese nuevamente")



def cargar_producto():
    '''
    funcion que sirve para cargar un producto en el inventario

    se puede utilziar hasta que el usuario lo desee
    
    no recibe parametros ni retorna valores
    '''
    
    respuesta = "s"
    while respuesta.lower() == "s":
    
        nombre_producto = input("Ingrese el nombre del producto que carga: ")        
        stock_producto = -1
                    
        while stock_producto < 1:
            
            stock_producto = input("Ingrese el stock del producto que carga: ")

            if stock_producto.isdigit():
                
                stock_producto = int(stock_producto)
                        
            else:
                stock_producto = -1 

        precio_producto = -1
                    
        while precio_producto < 1:
            
            precio_producto = input("Ingrese el precio del producto que carga: ")

            if precio_producto.isdigit():

                precio_producto = float(precio_producto)

            else:
                precio_producto = -1

                        
                    
                    
                    

        inventario.append([nombre_producto, precio_producto, stock_producto])
        
        print("Producto cargado con exito")
        
        respuesta = input("¿Desea cargar más productos (s/n)?: ").lower()
        
        while respuesta not in ["s", "n"]:
            
            respuesta = input("Respuesta no valida. Ingrese 's' para continuar o 'n' para salir: ").lower()
def realizar_busqueda():
    '''
    Realiza la búsqueda de un producto en el inventario.

    Esta función permite al usuario buscar un producto en el
    inventario. Si el producto se encuentra, se muestra su precio y la
    cantidad disponible en stock. Si no se encuentra, se notifica al
    usuario. Si el inventario está vacío, se informa al usuario.

    No recibe parámetros ni retorna valores.
    '''
    
    if len(inventario) > 0:
        producto_busqueda = input(f"¿Cual producto desea buscar?: ")
        
        for i in range(len(inventario)):
                
            if inventario[i][0].lower() == producto_busqueda.lower():
                    
                stock_disponible = inventario[i][2]
                precio_producto = inventario[i][1]

                print(f"El producto {producto_busqueda} vale actualmente {precio_producto} y tenemos {stock_disponible} unidades en stock")
                return
                    
        print(f"No se encontro el producto {producto_busqueda}")
                

            
    else:
        print(f"No hay objetos en el inventario aun")
                    


def organizar_inventario():
    '''
    Organiza el inventario por precio de productos en orden ascendente.

    Esta función verifica si hay productos en el inventario. Si hay productos,
    los organiza, ordenando los productos de menor a mayor. Luego, imprime los detalles de
    cada producto en el inventario.

    No recibe parámetros ni retorna valores.
    '''


    if len(inventario) > 0:

        n = len(inventario)
        
        for i in range(n):
            for j in range(0, n-i-1):
                if inventario[j][1] > inventario[j+1][1]:
                    inventario[j], inventario[j+1] = inventario[j+1], inventario[j]

    else:
        print(f"No hay objetos en el inventario aun") 

    for i in range(len(inventario)):
        
        nombre = inventario[i][0]
        precio = inventario[i][1]
        stock = inventario[i][2]
        
        print(f"producto: {nombre}, precio: {precio} y stock: {stock}  ")   
    
def mostrar_mas_caro_y_barato():
    '''
    Muestra el producto mas caro y el mas barato del inventario.

    si existen productos en el inventario, realiza una busqueda 
    de los productos mas caros y mas baratos , luego los muestra

    No recibe parámetros ni retorna valores.
    '''
    if len(inventario) > 0:

        producto_mas_caro = inventario[0]
        producto_mas_barato = inventario[0]

        for item in inventario:
            if item[1] > producto_mas_caro[1]:

                producto_mas_caro = item
            if item[1] < producto_mas_barato[1]:

                producto_mas_barato = item
            
        print(f"El producto más caro es: {producto_mas_caro[0]} con un precio de {producto_mas_caro[1]}")

        print(f"el producto más barato es: {producto_mas_barato[0]} con un precio de {producto_mas_barato[1]}.")

        
       




    else:
        print(f"No hay objetos en el inventario aun") 

def mostrar_productos_15000():
    '''
    Muestra los productos del inventario con un precio superior a 15,000.

    si hay productos en el inventario. 
    busca aquellos cuyo precio es mayor a 15,000 y los muestra, incluyendo su
    nombre, precio y stock. Si no se encuentran productos que cumplan con esto se notifica al usuario. 
    Si el inventario está vacío, tambien se informa al usuario.

    No recibe parametros ni retorna valores.
    
    '''

    if len(inventario) > 0:

        productos_mas_15000 = []

        for i in range(len(inventario)):  
            
            if inventario[i][1] > 15000:  
                
                productos_mas_15000.append(inventario[i])

        if len(productos_mas_15000) > 0:
            
            for i in range(len(productos_mas_15000)):
                
                print(f"Nombre: {productos_mas_15000[i][0]}, Precio: {productos_mas_15000[i][1]}, Stock: {productos_mas_15000[i][2]}")

        else:

            print(f"No hay productos que valgan mas que 15 mil pesos")

                
            


    else:
        print(f"No hay objetos en el inventario aun")





mostrar_menu()