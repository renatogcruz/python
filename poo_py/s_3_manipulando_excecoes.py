def algo():
	raise Exception('excecao')
	print('depois do raise')


try:
	algo()
except:
	print('Eu peguei uma excecao')
	print('executado apos a excecao')

	#except BaseException