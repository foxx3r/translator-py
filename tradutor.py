#!/usr/bin/python3
# coding: utf-8
from googletrans import Translator
import lista
from time import sleep
import os
import sys
from huepy import yellow

if 'linux' in sys.platform:
	pass
else:
	print('este script só é portado para Linux')
	exit()

resultado = None
DadosArray = []

func = (lambda x: x * '-=-')
translate = Translator(service_urls = [
	'translate.google.com'
])

print(yellow('''_       __
  _ _  __   _   _ _| | __ / | __  __
 / ` |/ _ \ / _ \ / _` | |/ _ \ | / _ \ \/ /
| (| | () | () | (| | |  _/  _| () >  <
 \_, |\_/ \_/ \, ||\__||  \__//\_\
 |_/             |_/
 # Telegram: @Foxxer_SA
 # Se inscreve lá @AcervoHackerBR!!!
 # GitHub: @foxx3r'''))
print(func(10))
print('\033[1;41mEvite utilizar acentos, ainda estamos trabalhando nisso!!!\033[0;0m')
sleep(1)
print(func(10))

while True:
	opcao = int(input('1) detectar idioma\n2) traduzir\n3) listar linguagens\n4) ler dados de um arquivo\n5) ler um conjunto\n6) sair\n-> '))
	print(func(10))
	
	if opcao == 1:
		detectar = str(input('digite algo -> '))
		print(translate.detect(detectar).lang)
		print(func(10))
		
	elif opcao == 2:
		try:
			traduzir = str(input('o que você deseja traduzir? -> '))
			linguagem = str(input('pra qual lingua você deseja traduzir? -> '))
			print('de: {}\t\tpara: {}'.format(translate.detect(traduzir).lang, linguagem))
			print('entrada: {}\nsaida: {}'.format(traduzir, translate.translate(traduzir, dest=linguagem).text))
			print(func(10))
		except ValueError:
			sleep(1)
			print('\033[1;41m\nDigite uma lingua válida!!!\n\033[0;0m')
			sleep(1)
			
	elif opcao == 3:
		print(lista.linguagens())
		print(func(10))
		sleep(1)
		
	elif opcao == 4:
		try:
			diretorio = str(input('digite o diretório do arquivo e o nome do arquivo > '))
			lingua = str(input('para qual lingua você deseja traduzir? -> '))
			with open(diretorio, 'r') as f:
				resultado = f.read()
				print('entrada: {}\nsaida: {}'.format(resultado, translate.translate(resultado, dest=lingua).text))
				print('de: {}\t\tpara: {}'.format(translate.detect(resultado).lang, lingua))
				f.close()
			print(func(10))
		except FileNotFoundError:
			print('Este arquivo não existe!!!')
			print(func(10))
		except ValueError:
			print('Digite uma lingua válida ou verifique sua conexão com a internet!!!')
			print('estamos tentando resolver erros de codificação, isso pode ter acontecido por conter caracteres especiais dentro do arquivo')
			print(func(10))
	elif opcao == 5:
		control = 7
		print('digite "quit" para parar a execução')
		while control != 'quit':
			control = str(input('> '))
			DadosArray.append(control)
		destino = str(input('Para qual linguagem você deseja traduzir? -> '))
		try:
			DadosArray.remove('quit')
		except:
			pass
		finally:
			os.system('clear')
			print(func(10))
		for c in DadosArray:
			print(translate.translate(c, dest=destino).text)
		DadosArray.clear()
		print(func(10))
	elif opcao == 6:
		exit()
		
	elif opcao >= 7 or opcao <= 0:
		print('digite apenas numeros entre 1 e 6!!!')
	else:
		print('digite apenas inteiros!!!')
