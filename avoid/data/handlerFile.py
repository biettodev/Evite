def fileExists(name):
	try:
		a = open(name, 'rt')
		a.close()
	except FileNotFoundError:
		return False
	else:
		return True

def createFile(name):
	try:
		a = open(name, 'wt+')
		a.close()
	except:
		print('O arquivo não pôde ser criado')
	else:
		print(f'Arquivo com name {name} criado com sucesso!')
