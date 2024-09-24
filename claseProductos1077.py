#creacion de la clase Productos
class Productos:
    #atributos
    id_producto = 0
    nombre = ""
    precio = 0
    stock = 0
    categoria = ""
    descripcion = ""
    fecha = ""
    
    #funciones
    def mostrarDatos(self):
        self.id_producto = 1
        self.nombre = "Calzon"
        self.stock = 200
        self.precio = 40
        self.categoria = "hombre"
        self.descripcion = "Calzon para hombre de color negro con azul"
        self.fecha = "12/Agosto/2024"
        
        print("---Valores asignados a calzon---")
        print(self.id_producto)
        print(self.nombre)
        print(self.stock)
        print(self.precio)
        print(self.categoria)
        print(self.descripcion)
        print(self.fecha)
    
    def listaProductos(self):
        productos = ["calcetines", "shores", "calzones", "calzones hombre", "calzones mujer"]
        for producto in productos:
            print(producto)
        
    def tupla_Productos_Categoria(self):
        productoss = ("nino", "nina", "hombre", "mujer", "enano")
        for producto in productoss:
            print(producto)
            
    def diccionario_producto_precio(self):
        productos = {
            "Calcetin" : 78,
            "short" : 100,
            "calzon mujer": 40,
            "calzon hombre": 45,
            "faldas": 100
        }
        
        for key, value in productos.items():
            print(f"El producto {key} cuesta: {value}")
            
    
    def productoAlta(self):
        print("El producto ya está disponible")
        
    def productosBaja(self):
        print("El producto ya no está disponible")
        
        


#Creando objeto
calzon = Productos()


#imprimiendo valores asignadas a calzon
calzon.mostrarDatos()

#imprimiendo funciones
print("\n--Llamando a las funciones--")
print("**Lista de productos**")
calzon.listaProductos()
print("\n**Tupla de la categoria de los productos**")
calzon.tupla_Productos_Categoria()
print("\n**Diccionario de productos y su precio**")
calzon.diccionario_producto_precio()
print("\n**Productos en alta**")
calzon.productoAlta()
print("\n**Productos en baja**")
calzon.productosBaja()
