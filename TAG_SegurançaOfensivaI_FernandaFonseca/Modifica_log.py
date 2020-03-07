'''
PROCESSO SELETIVO - Grupo de Resposta a Incidentes de Segurança

Nome: Fernanda Veiga Gomes da Fonseca
TAG - Segurança Ofensiva - Entrega: 07/03/2020
'''

'''
Código secundário no malware.
Realiza a leitura do arquivo de log gerado pelo código principal susbtituindo alguns caracteres de maneira a facilitar a leitura.
Em virtude de dificuldades encontradas durante a escrita do código, 
apenas foram analisados os caracteres correspondentes às teclas de Caps Lock e Enter.
O código ainda pode ser incrementado (por exemplo, Ⓐ seguido de Ⓣ pode levar à escrita de "mudança de tela" no novo arquivo de log).
Observação: as teclas de captura de tecla e de espaço já haviam sido analisadas pelo código principal.
'''

import os

# Caminho do arquivo de log.
log = "/home/fernanda/Documentos/PS_GRIS_2020/Semana1/7_Segurança Ofensiva/TAG 1/log.txt"

# Caminho do novo arquivo de log.
log_modificado = "/home/fernanda/Documentos/PS_GRIS_2020/Semana1/7_Segurança Ofensiva/TAG 1/log_modificado.txt"

# Inicialização de variáveis necessárias para análise do caracter de Caps Lock.
caps_lock = 0
caps_lock_contador = 0

# O arquivo do novo log é aberto para escrita.
with open (log_modificado, "a") as fm:

	# O arquivo do log original é aberto para leitura.
	with open (log, "r") as f:

		# As linhas contidas no arquivo de log são salvas em uma lista.
		linhas = f.readlines ()

	# Um elemento da lista corresponde a uma linha do arquivo de log.
	for linha in linhas:

		# Um elemento da string (elemento da lista) corresponde a um caracter da linha.
		for indice, caracter in enumerate (linha):
			
			# Tecla pressionada: Caps Lock.
			if (caracter == "Ⓛ"):
				caps_lock_contador += 1

				# Analisa o caso de o Caps Lock ter sido desabilitado.
				if (caps_lock_contador % 2 != 0):
					caps_lock = 1

				else:
					caps_lock = 0

			# Tecla pressionada: Enter.
			elif (caracter == "↙"):
				fm.write ("\n")

			else:
				# Caso o Caps Lock não tenha sido desabilitado, o próximo caracter será escrito com letra maiúscula.
				if (caps_lock == 1):
					fm.write (caracter.upper ())

				# Os demais tipos de caracteres são escritos sem serem analisados.
				else:
					fm.write (caracter)