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
		retorno.append(b[i])

	return retorno
	
def retornaChaveValor(array):
	resultado = []
	for i in range(len(array)):
		chave = ''
		valor = []
		for e in range(len(array[i])):
			if (e == 7): 
				chave = array[i][e]	
			else:
				valor.append(array[i][e])
	
		resultado.append([chave, valor])
	return resultado
	
def dicionarios(a):
	retorno = []
	for i in a:
		inbuffer = i
		merged = merge(inbuffer)
 #		chaveValor = retornaChaveValor(merged)	
		dic = dict(merged[i:i+2] for i in range(0, len(merged), 2))
		retorno.append(dic)
	retorno.pop(0)
	return retorno


dados = csvtolist('dados',',')

lista = merge(dados)
print retornaChaveValor(lista)

lib = dicionarios(dados)

#print lib
