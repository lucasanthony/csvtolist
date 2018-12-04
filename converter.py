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
