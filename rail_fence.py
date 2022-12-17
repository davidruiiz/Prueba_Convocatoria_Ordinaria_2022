"""
El cifrado Rail Fence (también llamado cifrado en zigzag) es una forma de cifrado por transposición. Funciona escribiendo su mensaje en líneas alternas a lo largo de la página y luego leyendo cada línea por turno. Veamos el desglose paso a paso para cifrar un texto usando Rail Fence Cipher:
Para encriptar un mensaje usando Rail Fence Cipher, primero necesitamos tener una clave (lo mismo para encriptar y desencriptar), que es el número de filas que tendrá para este cifrado.
Luego comenzamos a escribir las letras del texto sin formato dado en diagonal hacia el lado derecho hasta alcanzar el número de filas especificado por la clave.
Luego rebotamos hacia arriba de manera similar en diagonal hasta que llegamos a la primera fila nuevamente. Así, los alfabetos del texto plano se escriben en zig-zag.
Este ciclo continúa hasta que se alcanza el final del texto sin formato. Luego se leen las filas individuales para obtener el texto cifrado.
Considerar un ejemplo nos aclararía las cosas. Tomemos un ejemplo donde: El texto sin formato se da como " defend the east wall " y el número de rieles (clave) = 3, luego el proceso de encriptación es como se muestra a continuación:
El cifrado Rail Fence con una clave de 3
Tenga en cuenta que al final del mensaje hemos insertado dos letras "X", que se llaman nulos y actúan como marcadores de posición. Esto se hace para asegurarse de que el mensaje encaje perfectamente en la cuadrícula, de modo que haya el mismo número de letras en la fila superior y en la fila inferior.
Ahora, leer la imagen fila por fila nos da el texto cifrado como "DNETLEEDHESWLXFTAAX".
Para descifrar un texto cifrado codificado con Rail Fence Cipher, tenemos que reconstruir la cuadrícula diagonal utilizada para cifrar el mensaje. Comenzamos escribiendo el mensaje, pero dejando una estrella en lugar de los espacios por ocupar (como se muestra en la siguiente figura). Gradualmente, puede reemplazar todas las estrellas con las letras correspondientes y leer el texto sin formato de la tabla de manera similar al cifrado
Colocación de estrellas en el lugar de los espacios a ocupar
Veamos el desglose por pasos:
Comenzamos haciendo una cuadrícula (matriz de rieles) con tantas filas como la clave dada (número de rieles) y tantas columnas como la longitud del texto cifrado.
Luego colocamos la primera letra en el cuadrado superior izquierdo y avanzamos en diagonal hacia abajo donde están presentes las letras.
Cuando volvemos a la fila superior, colocamos la siguiente letra en el texto cifrado. Continuamos este proceso a lo largo de la fila y comenzamos la siguiente fila cuando lleguemos al final.
Atravesamos la matriz en forma de zig-zag para obtener el texto plano original.
 Escriba una función/método que tome 2 argumentos, una cadena y el número de rieles, y devuelva la cadena CODIFICADA.
Escriba una segunda función/método que tome 2 argumentos, una cadena codificada y el número de rieles, y devuelva la cadena DECODIFICADA.
Tanto para la codificación como para la decodificación, asuma un número de rieles >= 2 y que pasar una cadena vacía devolverá una cadena vacía.
Tenga en cuenta que el ejemplo anterior excluye la puntuación y los espacios solo por simplicidad. Sin embargo, hay pruebas que incluyen puntuación. No filtre la puntuación, ya que son parte de la cadena.
"""

class Encriptado:
    
    def __init__(self, mensaje, clave):
        self.mensaje = mensaje
        self.clave = clave
        self.Matrix = [['' for cols in range(len(mensaje))] for rows in range(clave)]
        self.row = 0
        self.col = 0
        self.i = 1
    
    def __str__(self):
        return self.mensaje
    
    def encriptado(mensaje, clave):
        Matrix = [['' for cols in range(len(mensaje))] for rows in range(clave)]
        row = 0
        col = 0
        i = 1
        while col<len(mensaje):
            if row+i<0 or row + i >= clave:
                i *= -1
            Matrix[row][col] = mensaje[col]

            row += i
            col += 1
        Encryption = ''
        for j in Matrix:
            Encryption+=''.join(j)
            print(j)
        return Encryption


if __name__ == '__main__':
    print(Encriptado.encriptado('hola', 3))
    print(Encriptado.encriptado('holaquetal', 4))
        

