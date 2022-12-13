class Encriptado:
    
    def __init__(self, texto, clave):
        self.texto = texto
        self.clave = clave
        self.cifrado = ""
        self.descifrado = ""
    
    
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
        M=encriptado("SOMETHING", 3)

        print(M)



