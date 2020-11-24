"""
#recrusão infinita

def regressiva(i):
	print(i)
	regressiva(i-1)
"""


#recursão caso-base e caso recursivo
def regressiva(i):
	print (i)
	if i <= 1: #caso-base
		return
	else:      #caso recursivo
		regressiva (i-1)

regressiva(10)