import fileinput
import hashlib
import math
import timeit
from Hash import transformacion

if __name__ == "__main__":
    #Iteraciones algoritmo creado
    StartTime_HashCreado_1 = timeit.default_timer()
    transformacion("123456")
    EndTime_HashCreado_1 = timeit.default_timer() - StartTime_HashCreado_1
    StartTime_HashCreado_10 = timeit.default_timer()
    for line in fileinput.input(files=("10.txt")):
       transformacion(line.rstrip())
    EndTime_HashCreado_10 = timeit.default_timer() - StartTime_HashCreado_10
    StartTime_HashCreado_20 = timeit.default_timer()
    for line in fileinput.input(files=("20.txt")):
        transformacion(line.rstrip())
    EndTime_HashCreado_20 = timeit.default_timer() - StartTime_HashCreado_20
    StartTime_HashCreado_50 = timeit.default_timer()
    for line in fileinput.input(files=("50.txt")):   
        transformacion(line.rstrip())
    EndTime_HashCreado_50 = timeit.default_timer() - StartTime_HashCreado_50
    hashCreado_entropia = 29*math.log(128,2)
    print("Valor entropia Creado:", hashCreado_entropia)
    print("T 1 Creado:",EndTime_HashCreado_1,"T 10 Creado:", EndTime_HashCreado_10,"T 20 Creado:",EndTime_HashCreado_20, "T 50 Creado:",EndTime_HashCreado_50)



    #Iteraciones SHA256
    StartTime_sha256_1 = timeit.default_timer()
    h=hashlib.new("sha256","123456".encode()) 
    EndTime_sha256_1 = timeit.default_timer() - StartTime_sha256_1
    StartTime_sha256_10 = timeit.default_timer()
    for line in fileinput.input(files=("10.txt")):
        h=hashlib.new("sha256",line.rstrip().encode()) 
    EndTime_sha256_10 = timeit.default_timer() - StartTime_sha256_10
    StartTime_sha256_20 = timeit.default_timer()
    for line in fileinput.input(files=("20.txt")):
        h=hashlib.new("sha256",line.rstrip().encode()) 
    EndTime_sha256_20 = timeit.default_timer() - StartTime_sha256_20
    StartTime_sha256_50 = timeit.default_timer()
    for line in fileinput.input(files=("50.txt")):  
        h=hashlib.new("sha256",line.rstrip().encode()) 
    EndTime_sha256_50 = timeit.default_timer() - StartTime_sha256_50

    h=hashlib.new("sha256",line.rstrip().encode()) 
    sha256_entropia=len(h.hexdigest())*math.log(36,2)
    print("Valor entropia SHA256:", sha256_entropia)
    print("T 1 SHA256:",EndTime_sha256_1,"T 10 SHA256:", EndTime_sha256_10,"T 20 SHA256:",EndTime_sha256_20, "T 50 SHA256:",EndTime_sha256_50)


    #Iteraciones sha1
    StartTime_sha1_1 = timeit.default_timer()
    h=hashlib.new("sha1","123456".encode()) 
    EndTime_sha1_1 = timeit.default_timer() - StartTime_sha1_1
    StartTime_sha1_10 = timeit.default_timer()
    for line in fileinput.input(files=("10.txt")):
        h=hashlib.new("sha1",line.rstrip().encode()) 
    EndTime_sha1_10 = timeit.default_timer() - StartTime_sha1_10
    StartTime_sha1_20 = timeit.default_timer()
    for line in fileinput.input(files=("20.txt")):
        h=hashlib.new("sha1",line.rstrip().encode()) 
    EndTime_sha1_20 = timeit.default_timer() - StartTime_sha1_20
    StartTime_sha1_50 = timeit.default_timer()
    for line in fileinput.input(files=("50.txt")):  
        h=hashlib.new("sha1",line.rstrip().encode()) 
    EndTime_sha1_50 = timeit.default_timer() - StartTime_sha1_50

    h=hashlib.new("sha1",line.rstrip().encode()) 
    sha1_entropia=len(h.hexdigest())*math.log(36,2)
    print("Valor entropia SHA1:", sha1_entropia)
    print("T 1 sha1:",EndTime_sha1_1,"T 10 sha1:", EndTime_sha1_10,"T 20 sha1:",EndTime_sha1_20, "T 50 sha1:",EndTime_sha1_50)


    #Iteraciones MD5
    StartTime_MD5_1 = timeit.default_timer()
    h=hashlib.new("MD5","123456".encode()) 
    EndTime_MD5_1 = timeit.default_timer() - StartTime_MD5_1
    StartTime_MD5_10 = timeit.default_timer()
    for line in fileinput.input(files=("10.txt")):
        h=hashlib.new("MD5",line.rstrip().encode()) 
    EndTime_MD5_10 = timeit.default_timer() - StartTime_MD5_10
    StartTime_MD5_20 = timeit.default_timer()
    for line in fileinput.input(files=("20.txt")):
        h=hashlib.new("MD5",line.rstrip().encode()) 
    EndTime_MD5_20 = timeit.default_timer() - StartTime_MD5_20
    StartTime_MD5_50 = timeit.default_timer()
    for line in fileinput.input(files=("50.txt")):  
        h=hashlib.new("MD5",line.rstrip().encode()) 
    EndTime_MD5_50 = timeit.default_timer() - StartTime_MD5_50
    h=hashlib.new("MD5",line.rstrip().encode()) 
    MD5_entropia=len(h.hexdigest())*math.log(36,2)
    print("Valor entropia MD5:", MD5_entropia)
    print("T 1 MD5:",EndTime_MD5_1,"T 10 MD5:", EndTime_MD5_10,"T 20 MD5:",EndTime_MD5_20, "T 50 MD5:",EndTime_MD5_50)

