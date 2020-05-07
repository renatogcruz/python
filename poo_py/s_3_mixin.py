"""
Quando utilizar?

Se vc desejar reutilizar uma determinada feature em várias classes
diferentes.
Para melhorar a modularidade.

Mixins é uma forma controlada de adicionar funcionalidades as classes.

Propriedades:

1 - não deve ser extendida
2 - não deve ser instanciada

Em python, o conceito de mixins é implementada utilizando herrança múltipla
"""

class Livro(object):

	def __init__(self, nome, conteudo):
		self.nome = nome
		self.conteudo = conteudo
		
class LivroHTMLMixin(object):
	def renderizar(self):
		return ('<html><xxxxxxxxxxxxxxxxxxxxxxxxxxxxx>') % (self.nome, self.conteudo)

class LivroHTML(Livro, LivroHTMLMixin):
	pass

livro_html = LivroHTML('Manifesto do Partido Comunista', 'Fogo nos racistas')
print(livro_html.renderizar())