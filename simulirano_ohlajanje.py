import random
import math

def simulirano_ohlajanje(G):
    n = len(G)
    for a in range(0, n): #spremenimo diagonalo da ima same 0
        if G[a][a] == 1:
            G[a][a] = 0
    d1 = int(n / 2)
    X = list(range(0, d1)) #vektorja indeksov vozlišč
    Y = list(range(d1, n))
    A = list(range(0, d1))  #vektorja indeksov vozlišč
    B = list(range(d1, n))
    k = 2
    (najboljsi_seznam_stevila_sosedov, najboljse_stevilo_povezav) = seznam_stevila_sosedov(G,X,Y)
    while k < 3000:
        (trenutni_seznam_stevila_sosedov, trenutno_stevilo_povezav) = (najboljsi_seznam_stevila_sosedov, najboljse_stevilo_povezav)
        t = (500/math.log(k))
        a = random.randint(0, d1-1)
        b = random.randint(d1, n)
        trenutno_stevilo_povezav += trenutni_seznam_stevila_sosedov[a][0]
        trenutno_stevilo_povezav -= trenutni_seznam_stevila_sosedov[a][1]
        trenutno_stevilo_povezav += trenutni_seznam_stevila_sosedov[b][0]
        trenutno_stevilo_povezav -= trenutni_seznam_stevila_sosedov[b][1]
        if trenutno_stevilo_povezav > najboljse_stevilo_povezav or random.uniform(0, 1)<math.exp((trenutno_stevilo_povezav-najboljse_stevilo_povezav)/t):
            najboljse_stevilo_povezav = trenutno_stevilo_povezav
            vmesni = A[a]
            A[a] = B[b]
            B[b] = vmesni
            vmesni = trenutni_seznam_stevila_sosedov[a][0]
            trenutni_seznam_stevila_sosedov[a][0] = trenutni_seznam_stevila_sosedov[a][1]
            trenutni_seznam_stevila_sosedov[a][1] = vmesni
            vmesni = trenutni_seznam_stevila_sosedov[b][0]
            trenutni_seznam_stevila_sosedov[b][1] = trenutni_seznam_stevila_sosedov[a][1]
            trenutni_seznam_stevila_sosedov[b][0] = vmesni
            vmesni = trenutni_seznam_stevila_sosedov[a]
            trenutni_seznam_stevila_sosedov[a] = trenutni_seznam_stevila_sosedov[b]
            trenutni_seznam_stevila_sosedov[b] = vmesni

        k+=1

    return najboljsi

def seznam_stevila_sosedov(I,C,D):    #izracuna zacetno stevilo sosedov za vsako vozlisce in stevilo povezav med razdelitvama grafa
    n = len(I)
    seznam_stevila_sosedov =[(0,0)]*len(I)
    for i in C:
        for j in D:
            Ix = 0
            Ox = 0
            Iy = 0
            Oy = 0
            for k in range(0, len(C)):
                if I[i][k] == 1:
                    Ix += 1
                if I[j][k] == 1:
                    Oy += 1
            for l in range(len(C), n):
                if I[j][l] == 1:
                    Iy += 1
                if I[i][l] == 1:
                    Ox += 1
            seznam_stevila_sosedov[i] = [Ix, Ox]
            seznam_stevila_sosedov[j] = [Iy,Oy]
            stevilo_povezav = Ox  + Oy - I[i][j]
    return seznam_stevila_sosedov, stevilo_povezav


A = [[]]