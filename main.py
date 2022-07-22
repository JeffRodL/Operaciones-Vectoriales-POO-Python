# Vector es una clase que toma valores de x, y & z para realizar operaciones vectoriales cartesianas.
#Se importa math para las operaciones matemáticas.
import math

class vector:
    #Constructor
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    #Representación matemática i+j+k
    def __str__(self):
        return '{:g}i+{:g}j+{:g}k'.format(self.x, self.y, self.z)
    
    #Representación de lista (i,j,k)
    def __repr__(self):
        return repr((self.x, self.y, self.z))

    #El método __add__ es el que se utiliza para el operador '+'
    #Denota la suma de dos vectores u+v 
    def __add__(self, other):
        return vector(self.x + other.x, self.y + other.y, self.z + other.z)
    
    #El método __sub__ es el que se utiliza para el operador '-'
    #Denota la resta de dos vectores u-v
    def __sub__(self, other):
        return vector(self.x - other.x, self.y - other.y, self.z - other.z)
    
    #El producto punto, multiplicación entre dos vectoes. Su producto es un escalar
    #Para este producto no existe un método tal como __dot__
    def dot(self, other):
        #Debemos asegurarnos que los valores ingresados sean válidos, es decir, vectores.
        #Si other no es del tipo vector, entonces muestra el error.
        if not isinstance(other, vector):
            raise TypeError('Solamente puede tomar como valores 3 vectores.')
        return self.x*other.x+self.y*other.y+self.z*other.z
    
    #Producto escalar, donde a, un número real, es un escalara y V un vector.
    def __mul__(self, scalar):
        #Para este caso es necesario que el escalar sea del tipo int o float
        if isinstance(scalar, int) or isinstance(scalar, float):
            return vector(self.x*scalar, self.y*scalar, self.z*scalar)
        raise NotImplementedError('Es necesario que sea un número')
            
    #La multiplicacioń reflejada también funciona, es decir vector * escalar
    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    #Negación de un vector, se invierte. (-)*V=(-V)
    def __neg__(self): 
        return vector(-self.x,-self.y,-self.z)
    
    #División de un vector dentro de un escalar.
    def __truediv__(self,scalar):
        #Es necesario que el escalar sea un número válido.
        if isinstance(scalar, int) or isinstance(scalar, float):
            return vector(self.x/scalar,self.y/scalar,self.z/scalar)
        raise TypeError('El escalar debe ser un número')
    
    #La norma de un vector. Definida como |x^2+y^2+z^3|^1/2
    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    #La distancia entre dos vectores, definida como |v-u|
    def distance(self, other):
        return abs(self - other)
    
if __name__ == '__main__':
    print('-'*40,'\nBienvenido a la calculadora vectorial.\n','-'*39)
    #Dos listas vacías para guardar los datos del usuario.
    v1 = []
    v2 = []
    #Ciclo for para ingresar los datos del usuario en una lista
    for i in range(3):
        numero = float(input('ingresar valores para el primer vector en x,y,z respectivamente: '))
        v1.append(numero)
    
    x1,y1,z1 = v1[0], v1[1], v1[2]
    vector1 = vector(x1,y1,z1)

    for i in range(3):
        numero2 = float(input('ingresar valores para el segundo vector en x,y,z respectivamente: '))
        v2.append(numero2)
        
    x2,y2,z2 = v2[0], v2[1], v2[2]
    vector2 = vector(x2,y2,z2)
    print('-'*20,'Vectores','-'*20)
    print(f'v1 = {vector1} \t \t v2 = {vector2}')
    print(f'v1 = {repr(vector1)} \t v2 = {repr(vector2)}')
    print('-'*22,'Suma','-'*22)
    print('v1 + v2 =', vector1 + vector2, '\t' ,'v1 + v2 =', repr(vector1 + vector2))
    print('-'*22,'resta','-'*22)
    print('v1 - v2 =', vector1 - vector2, '\t', 'v1 - v2 =', repr(vector1 - vector2))
    print('v2 - v1 =', vector2 - vector1, '\t', 'v2 - v1 =', repr(vector2 - vector1))
    print('-'*17,'Producto Punto','-'*17)
    print('v1·v2 = ', vector1.dot(vector2))
    print('-'*16,'Producto Escalar','-'*16)
    var = float(input('Ingrese un valor escalar para multiplicar por un vector'))
    print('¿Por cuál vector quisiera multiplicarlo?')
    var2 = input('¿v1 o v2?')
    if var2 == 'v1':
        print(var, '* v1 = ', var*vector1)
    elif var2 == 'v2':
        print(var,'* v2 = ', var*vector2)
    else:
        print('Ingrese un valor válido')
    print('-'*21,'Negación','-'*21)
    print(f'v1 = {-vector1} \t \t v2 = {-vector2}')
    print(f'v1 = {repr(-vector1)} \t v2 = {repr(-vector2)}') 
    print('-'*19,'División','-'*19)
    var = float(input('Ingrese un valor escalar para dividirlo por un vector'))
    print('¿Por cuál vector quisiera dividirlo?')
    var2 = input('¿v1 o v2?')
    if var2 == 'v1':
        print('v1 /',var,'=',vector1/var)
    elif var2 == 'v2':
        print('v2 /',var,'=',vector2/var)
    else:
        print('Ingrese un valor válido') 
    print('-'*21,'Norma','-'*21)
    print('|x1²+y1²+z1²|^1/2 =',abs(vector1))
    print('|x2²+y2²+z2²|^1/2 =',abs(vector2))
    print('-'*19,'Distancia','-'*19)
    print('Distancia de v1 a v2 = ',vector1.distance(vector2))
    