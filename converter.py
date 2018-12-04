#coding: utf-8

def csvtolist(arquivo,separador):
	import csv
	lista = []
	arquivo = '%s.csv' %arquivo
	with open(arquivo) as csvfile:
   		dados = csv.reader(csvfile, delimiter=separador)
   		for linha in dados:
   			lista.append(linha)
	return lista

def merge(b):
	attributes = ['Price','Year','Mileage','City','State','Vin','Make','Model']
	retorno = []
	for i in range (len(attributes)):
		retorno.append(attributes[i])
		retorno.append(b[i])

	return retorno

def dicionarios(a):
	retorno = []
	for i in a:
		inbuffer = i
		merged = merge(inbuffer)
		dic = dict(merged[i:i+2] for i in range(0, len(merged), 2))
		retorno.append(dic)
	retorno.pop(0)
	return retorno


dados = csvtolist('dados',',')

lib = dicionarios(dados)

print lib
