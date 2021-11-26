from datetime import datetime
import random 
import base64
import string 
def transformacion(texto): #Se realiza una función para que cada texto ingresado acabe con un largo de 25 caracteres.
    largo=len(texto)
    if(largo>25):
        i=0
        string_final=""
        string_add="".join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k = 13)) #Se genera un texto de 13 caracteres aleatorios para agregar.
        for caracter in texto: #Se ingresa un caracter del string ingresado y luego se genera un caracter aleatorio hasta tener 25 caracteres.
            if len(string_final)==24: #Al ingresar caracteres de 2 en 2, al acabar en 24 caracteres se agrega un ultimo caracter para terminar los 25 y salir del for.
                string_final=string_final+caracter
                break
            random.seed(datetime.now().minute)
            string_final=string_final+caracter
            string_final=string_final+string_add[i]
            i=i+1
        hash(string_final)
        
    elif(largo<25):
        #Se ocupa la hora para generar la semilla, despues de esto se calculan los caracteres faltantes para tener 25.
        random.seed(datetime.now().minute)
        largo_necesario = 25-len(texto)
        #Se añaden caracteres aleatorios, contando mayus, minus y numeros.
        string_add="".join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k = largo_necesario))
        string_final=texto+string_add
        hash(string_final)
    if(largo==25):
        hash(texto)
def hash(texto):   
    contador = 0
    hash_final = ""
    texto_1=""
    texto_3 = ""
    Reverse=""
    for caracter in texto: #Se itera sobre la lista y se separa en tres grupos diferentes.      
        contador=contador+1
        if contador<=12: #Se ocupa la libreria de base64 para realizar un cifrado en este lenguaje.
            texto_1=texto_1+caracter
            if contador==12: #Se ocupa esta condicional para ocupar solo los 12 primeros caracteres.
                Base64_Encoded=base64.b64encode(texto_1.encode())
                hash_final=hash_final+Base64_Encoded.decode()
        elif contador<=20: #Desde el caracter 12 al 20 se realizara un cifrado caesar con desplazamiento según el largo.
            #Se define la semilla, esta generara un numero dependiendo del largo del texto a hashear.
            #Este valor puede ser replicado solo conociendo el largo y usando la misma función.
            random.seed(datetime.now().minute)
            #Para ser utilizado en caesar se definira un numero entre 1 y 24
            desplazamiento=random.randint(1,24)
            if (caracter.isupper()):  #Implementación obtenida de https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_caesar_cipher.htm
                hash_final=hash_final+(chr((ord(caracter) + desplazamiento-65) % 26 + 65))
            else:
                hash_final=hash_final+(chr((ord(caracter) + desplazamiento-97) % 26 + 97))
        elif contador<=25: #Reverse
            texto_3=texto_3+caracter #Se agrupan los ultimos caracteres para aplicar el reverse
            if contador==25: 
                i = 4 #Se define el largo de los caracteres que se necesitan invertir (del caracter 20 al 25) 
                while i>=0: #Se realiza un while que va disminuyendo, ingresando los ultimos caracteres primero.
                    Reverse = Reverse + texto_3[i]
                    i = i - 1
                hash_final=hash_final+Reverse
    print("Texto:",texto,"| Hash:",hash_final)
