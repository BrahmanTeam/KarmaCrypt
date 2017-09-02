from pyDes import des



def encriptaFichero(user_pass, fichero):
    '''
    @funcionamiento: Encripta un fichero en el mismo directorio.
    @argumentos: la clave de encriptacion, el nombre del fichero
    @return: devuelve True
    '''
#    abro el fichero lo copio en memoria y lo cierro
    f = open(fichero, 'rb+')
    d = f.read()
    f.close()

#    convierto la clave string en objeto clave
    k = des(user_pass)

#    encripto el fichero-objeto en memoria con el
#    objeto clave y lo grabo con el mismo nombre
    d = k.encrypt(d, ' ')
    f = open(fichero, 'wb+')
    f.write(d)
    f.close()
    return True


def desencriptaFichero(user_pass, fichero):
    '''
    @funcionamiento: Desencripta un fichero en el mismo directorio.
    @argumentos: la clave de encriptacion, el nombre del fichero
    @return: devuelve True
    '''

#    abro el fichero lo copio en memoria y lo cierro
    f = open(fichero, 'rb+')
    d = f.read()
    f.close()

#    convierto la clave string en objeto clave
    k = des(user_pass)

#    desencripto el fichero-objeto en memoria con el objeto
#    clave y lo grabo con el mismo nombre
    d = k.decrypt(d, ' ')
    f = open(fichero, 'wb+')
    f.write(d)
    f.close()
    return True




