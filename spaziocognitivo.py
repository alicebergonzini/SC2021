import sys
import re
import math
import nltk


def leggifiles(file0):
    fileInput=open(file0, mode="r", encoding="utf-8")
    raw=fileInput.read()
    return raw

def listaLuoghi(el):
    listaLuoghi=[]
    for elemento in el:
        m = re.match(r'[A-Z]?[a-z]+', elemento) #attenzione questa regex non riconosce parole con caratteri speciali 
        if m:
            luogo=elemento
            listaLuoghi.append(luogo)
    return listaLuoghi

def listaCompleta(x, luoghi): 
    lista=[]
    i=0
    for luogo in luoghi:
        nomeL=luogo
        occ=x[i+1]
        lat=x[i+2]
        longit=x[i+3]
        elemento=[nomeL, occ, lat, longit]
        lista.append(elemento)
        i=i+4
    return lista

def calcolapeso(nOcc, card):
    peso=nOcc/card
    return peso

def totOcc(listaElem):
    count=0
    for oggetto in listaElem:
        occ=oggetto[1]
        occorrenze=float(occ)
        count=count+occorrenze
    return count

def listaPesi(listaElem, totale):
    listaPesi=[]
    for oggetto in listaElem:
        occStr=oggetto[1]
        occorrenze=int(occStr)
        peso=calcolapeso(occorrenze, totale)
        listaPesi.append(peso)
    return listaPesi

def coordinatePesate(listaElem, listapesi):
    i=0
    X=0
    Y=0
    Z=0
    for oggetto in listaElem:
        latitudineStr=oggetto[2]
        longitudineStr=oggetto[3]
        lat=float(latitudineStr)
        longit=float(longitudineStr)
        peso=listapesi[i]
        senoLat=math.sin(math.radians(lat))
        cosenoLat=math.cos(math.radians(lat))
        senoLong=math.sin(math.radians(longit))
        cosenoLong=math.cos(math.radians(longit))
        calcoloX=peso*cosenoLat*cosenoLong
        calcoloY=peso*cosenoLat*senoLong
        calcoloZ=peso*senoLat
        X=X+calcoloX
        Y=Y+calcoloY
        Z=Z+calcoloZ
        i=i+1
    return X,Y,Z

def centrodiP(x, y, z):
    Arad=math.atan(z/(math.sqrt(pow(x,2)+pow(y,2))))
    Brad=math.atan(y/x)
    A=math.degrees(Arad)
    B=math.degrees(Brad)
    return A,B


def distanza(A, B, oggetto):
    lat=float(oggetto[2])
    longit=float(oggetto[3])
    T=6372.797
    x=math.cos(math.radians(lat))
    y=math.cos(math.radians(A))
    z=math.cos(math.radians(longit-B))
    h=math.sin(math.radians(lat))
    j=math.sin(math.radians(A))
    calcolo=T*(math.acos((x*y*z)+(h*j)))
    return calcolo

def listaDistanze(A, B, listaogg):
    d=0
    listaDist=[]
    for oggetto in listaogg:
        d=distanza(A, B, oggetto)
        listaDist.append(d)
    return listaDist

def raggiodiP(listapesi, listadistanze):
    i=0
    media=0
    for oggetto in listapesi:
        peso=oggetto
        distanza=listadistanze[i]
        calcolo=peso*distanza
        media=media+calcolo
        i=i+1
    return media
        

def main(testo):
    corpus=leggifiles(testo)
    singolielementi=nltk.word_tokenize(corpus)
    listaL=listaLuoghi(singolielementi)
    listaC=listaCompleta(singolielementi, listaL)
    totaleL=totOcc(listaC)
    listapesi=listaPesi(listaC, len(listaC))
    X,Y,Z=coordinatePesate(listaC, listapesi)
    A,B=centrodiP(X, Y, Z)
    listadistanze=listaDistanze(A,B, listaC)
    raggioDiPercezione=raggiodiP(listapesi, listadistanze)
    print(A,B)    
    print(raggioDiPercezione)
    
main(sys.argv[1])
