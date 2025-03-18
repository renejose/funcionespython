import funcionregular

filas = 790 
topelectura = 100

funcionregular.saludar()

funcionregular.calculartiempdelecturadeexcel(filas,topelectura)

def saludar2():
    print("hola a todos")


def invertirordenclaves(clave):
    z = 0  # Inicializamos z en 0 para almacenar el número invertido
    x = clave
    
    while x > 0:
        k = x % 10  # Obtiene el último dígito de x
        z = z * 10 + k  # Agrega el dígito a z
        x = x // 10  # Elimina el último dígito de x
    
    print(z)    