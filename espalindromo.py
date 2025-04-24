palabra = ""
print("Ingrese su palabra")
palabra = input ()
nuevapalabra = ""

for i in range( len(palabra) ):
    print(palabra[len(palabra) -1-i] )
    nuevapalabra += palabra[len(palabra) -1-i] 
    print("La nueva palabra es:" + nuevapalabra)

    if palabra == nuevapalabra:
        print("La palabra : " + palabra + " es igual a la palabra " + nuevapalabra)
    else:
        print("La palabra :" + palabra + " es dintinto a la palabra " + nuevapalabra)
 
