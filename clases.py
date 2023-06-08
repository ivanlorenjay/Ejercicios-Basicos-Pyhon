# Clase con 3 parámetros de entrada 

class ObjetoMinecraft:
    def __init__(self, nombre, material, durabilidad):
        self.nombre = nombre
        self.material = material
        self.durabilidad = durabilidad
        
# ========================================== # 

# Clase utilizando herencia:

class ObjetoMinecraft:
    def __init__(self, nombre, material, durabilidad):
        self.nombre = nombre
        self.material = material
        self.durabilidad = durabilidad

class CuboMinecraft(ObjetoMinecraft):
    def __init__(self, nombre, material, durabilidad, lado):
        super().__init__(nombre, material, durabilidad)
        self.lado = lado

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Material: {self.material}")
        print(f"Durabilidad: {self.durabilidad}")
        print(f"Lado: {self.lado}")

# Crear una instancia de la clase CuboMinecraft y mostrar su información
cubo = CuboMinecraft("Cubo de piedra", "piedra", 100, 1)
cubo.mostrar_informacion()

# ========================================== # 

# Clase utilizando polimorfismo:

class ObjetoMinecraft:
    def __init__(self, nombre, material, durabilidad):
        self.nombre = nombre
        self.material = material
        self.durabilidad = durabilidad

    def usar(self):
        raise NotImplementedError("Método no implementado")

class EspadaMinecraft(ObjetoMinecraft):
    def __init__(self, nombre, material, durabilidad, dano):
        super().__init__(nombre, material, durabilidad)
        self.dano = dano

    def usar(self):
        print(f"La espada '{self.nombre}' hace un daño de {self.dano}")

class CuboMinecraft(ObjetoMinecraft):
    def __init__(self, nombre, material, durabilidad, lado):
        super().__init__(nombre, material, durabilidad)
        self.lado = lado

    def usar(self):
        print(f"El cubo '{self.nombre}' puede ser utilizado para construir")

# Crear instancias de las clases y utilizar el polimorfismo
espada = EspadaMinecraft("Espada de diamante", "diamante", 100, 10)
cubo = CuboMinecraft("Cubo de piedra", "piedra", 100, 1)

objetos = [espada, cubo]

for objeto in objetos:
    objeto.usar()

# Comentarios finales 

# En Python, la palabra clave raise se utiliza para generar una excepción 
# de forma explícita. Permite al lanzar manualmente una excepción
# en una determinada situación cuando se cumple una condición específica.
# El método super() se utiliza en Python para acceder y llamar métodos de una
# clase base (superclase) desde una clase derivada (subclase). Proporciona una
# forma 'acortada' de invocar la implementación de un método en la clase padre,
# permitiendo extender y personalizar la funcionalidad heredada.
