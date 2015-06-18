#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)

def media(v):
    return sum(v)/len(v)

def arranjo(n, p):
    return fatorial(n) / fatorial(n-p)

def arranjo_rep(n, p):
    return pow(n, p)

def combinacao(n, p):
    return arranjo(n, p) / fatorial(p)

def combinacao_rep(n, p):
    return combinacao(n+p-1,p)

def permutacao(n):
    return fatorial(n)

def permutacao_rep(n, r):
    #Variavel r como um array
    n = fatorial(n)
    for i in r:
        n /= fatorial(i)
    return n

def permutacao_circular(n):
    return fatorial(n-1)

def desvio_medio(v):
    return media([abs(i - media(v)) for i in v])

def variancia(v):
    return media([pow(i - media(v), 2) for i in v])

def desvio_padrao(v):
    return pow(variancia(v), .5)
