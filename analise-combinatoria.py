#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def fatorial(n):
	if n == 0 or n == 1:
		return 1
	else:
		return n * fatorial(n-1)

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
	#r é um array
	n = fatorial(n)
	for i in r:
		n /= fatorial(i)
	return n

def permutacao_circular(n):
	return fatorial(n-1)

#Exemplos
print (arranjo(10,2))
print (arranjo_rep(10,2))
print (combinacao(10,2))
print (combinacao_rep(10,2))
print (permutacao(10))
print (permutacao_rep(10,[3,2]))
print (permutacao_circular(10))
