class Relogio:

	def __init__(self, hora=0, min=0, seg=0):
		self.hora = hora
		self.min = min
		self.seg = seg

	def ajustar_hora(self, hora, min, seg=0):
		self.hora = hora
		self.min = min
		self.seg = seg

	def __str__(self):
		return "{0:02d}:{1:02d}:{2:02d}".format(self.hora,
												self.min, 
												self.seg)

	def tick(self):
		if self.seg == 59:
			self.seg = 0
			if self.min == 59:
				if self.hora == 23:
					self.hora = 9
				else:
					self.hora += 1
			else:
				self.min +=1
		else:
			self.seg += 1

"""rel = Relogio(10, 3, 59)
print(rel)
rel.tick()
print(rel)"""

class Calendario:

	meses = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

	def __init__(self, dia, mes, ano):
		self.dia = dia
		self.mes = mes
		self.ano = ano

	def ajustar_data(self, dia, mes, ano):
		self.dia = dia
		self.mes = mes
		self.ano =ano

	def __str__(self):
		return "{0:02d}/{1:02d}/{2:04d}".format(self.dia, 
												self.mes,
												self.ano)

	def avancar(self):
		dia_max = Calendario.meses[self.mes - 1]

		if self.dia == dia_max:
			self.dia = 1
			if self.mes == 12:
				self.mes = 1
				self.ano += 1
			else:
				self.mes += 1
		else:
			self.dia += 1

"""cal = Calendario(31, 1, 2016)
print(cal)
cal.avancar()
print(cal)"""

class CalendarioRelogio(Relogio, Calendario):
	
	def __init__(self, hora, min, seg, dia, mes, ano):
		Relogio.__init__(self, hora, min, seg)
		Calendario.__init__(self, dia, mes, ano)

	def __str__(self):
		return Relogio.__str__(self) + ', ' + Calendario.__str__(self)


cal_rel = CalendarioRelogio(30,1,10,1,2,2010)
print(cal_rel)

