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
        

