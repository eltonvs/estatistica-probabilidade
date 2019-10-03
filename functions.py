#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#Medidas de Tendência Central
def media(v):
    return sum(v) / len(v)

def moda(v):
    b, modas = 2, []
    for i in v:
        a = v.count(i)
        if a > b:
            b, modas = a, [i]
        elif a == b and i not in modas:
            modas.append(i)
    modas.sort()
    return modas

def mediana(v):
    v.sort()
    if len(v) % 2 == 0:
        return media([v[int(len(v) / 2) - 1], v[int(len(v) / 2)]])
    else:
        return v[int(len(v) / 2)]

#Medidas de Dispersão
def amplitude(v):
    return max(v) - min(v)

def desvio_medio(v):
    return media([abs(i - media(v)) for i in v])

def variancia(v):
    return media([pow(i - media(v), 2) for i in v])

def desvio_padrao(v):
    return pow(variancia(v), .5)

#Análise Combinatória
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

def arranjo(n, p):
    return fatorial(n) / fatorial(n-p)

def arranjo_rep(n, p):
    return pow(n, p)

def combinacao(n, p):
    return arranjo(n, p) / fatorial(p)

def combinacao_rep(n, p):
    return combinacao(n + p - 1, p)

def permutacao(n):
    return fatorial(n)

def permutacao_rep(n, r):
    n = fatorial(n)
    for i in r:
        n /= fatorial(i)
    return n

def permutacao_circular(n):
    return permutacao(n - 1)
