#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Gerenciador de senhas by: Juvenal Cullyno
from time import sleep
from random import choice
import os

# Funções de Banners e cores

def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')



def banner():

    #clr()
    logo="""
  ___                           _           _             
 / __| ___  _ _  ___  _ _   __ (_) __ _  __| | ___  _ _ 
| (_ |/ -_)| '_|/ -_)| ' \ / _|| |/ _` |/ _` |/ _ \| '_|
 \___|\___||_|  \___||_||_|\__||_|\__,_|\__,_|\___/|_|                                                                
                                         """
    print()
    print(choice(cores),'By: Juvenal Cullyno', W)
    print(choice(cores) + logo + W)



cores = ['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m']
W = '\033[0m'


def imprimir():
    print('\033[1;m','=='*28,'\033[0m')
    print(choice(cores))
    print('''
    [ 1 ] Mostrar todas as senhas
    [ 2 ] Buscar site
    [ 3 ] Incluir Site
    [ 4 ] Editar Site
    [ 5 ] Excluir site
    [ 6 ] Exportar sites
    [ 7 ] Importar sites para csv
    [ 0 ] Fechar Gerenciador''')
    print()
    print('\033[1;m','=='*28,'\033[0m')
#-----------------------------------------------------------------
gerenciador = {}

# Funções

def mostrar_site():
    clr()
    banner()
    if len(gerenciador) > 0:
        for sites in gerenciador:
            buscar_site(sites)
        print(f'Total: {len(gerenciador)}')
    else:
        print('Lista vazia...')



def buscar_site(sites):

    try:
        print('site:'.rjust(6), sites)
        print('email:', gerenciador[sites]['email'])
        print('senha:', gerenciador[sites]['senha'])

       #Aqui tem a opção de mostrar as senhas criptografadas em base64
       #Só precisa comentar o codigo acima e descomentar o código abaixo.
       #sen = 'senha:', gerenciador[sites]['senha']
       #sen1 = sen[1]
       #men_bytes = sen1.encode('ascii')
       #b64_bytes = base64.b64encode(men_bytes)
       #base64_men = b64_bytes.decode('ascii')
       # print('senha:',base64_men)

        print('url:'.rjust(6), gerenciador[sites]['url'])
        print('~'*25)
    except KeyError:
        print('Site Inexistente')
    except Exception as erro:
        print('>>> Erro Inesperado <<<')
        print(erro)



def ler_detalhes_site():
    email = input('Digite o email/usuário: ')
    senha = input('Digite a senha: ')
    url = input('Digite a url do site: ')
    return  email, senha, url



def incluir_editar_site(sites, email, senha, url):
    gerenciador[sites] = {
        'email': email,
        'senha': senha,
        'url': url
    }
    salvar()
    print()
    print(f'Site {sites} Adicionado...')
    print()

    

def excluir_site(sites):
    try:
        gerenciador.pop(sites)
        print()
        print(f'Contato {sites} excluido com sucesso...')
    except KeyError:
        print('Site Inexistente...')
    except Exception as erro:
        print('Ocorreu algum erro')
        print(erro)



def exportar_site(nome_arquivo):
    try:
        with open(nome_arquivo, 'w') as arquivo:
            for sites in gerenciador:
                email = gerenciador[sites]['email']
                senha = gerenciador[sites]['senha']
                url = gerenciador[sites]['url']
                arquivo.write('{},{},{},{}\n'.format(sites, email, senha, url))
        print('Sites Exportados com sucesso')

    except Exception as erro:
        print('Erro ocorrido...')
        print(erro)



def importar_site(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')
                nome = detalhes[0]
                email = detalhes[1]
                senha = detalhes[2]
                url = detalhes[3]

                incluir_editar_site(nome, email, senha, url)
        print('Sites importados com sucesso...')
    except FileNotFoundError:
        print('>>> Site não encontrado...')
    except Exception as erro:
        print('Algum Erro ocorreu')
        print(erro)



def salvar():
    exportar_site('senhas.csv')



def carregar():
    try:
        with open('senhas.csv', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')

                nome = detalhes[0]
                email = detalhes[1]
                senha = detalhes[2]
                url = detalhes[3]

                gerenciador[nome] = {
                    'email': email,
                    'senha': senha,
                    'url': url
                }
        print(choice(cores),'>>>> Database carregado com sucesso...')
        print(f' >>>> {len(gerenciador)} Sites carregados...', W)

    except FileNotFoundError:
        print('Site não encontrado...')
    except Exception as erro:
        print('Ocorreu um erro...')
        print(erro)



# INICIO DO PROGRAMA
carregar()
while True:
    banner()
    imprimir()

    opcao = input('\033[1;105m''Digite uma opção: ''\033[0m')

    if opcao == '1' or opcao == '01':
        mostrar_site()
    elif opcao == '2' or opcao == '02':
        sites = input('Digite o nome do site: ')
        buscar_site(sites)
    elif opcao == '3' or opcao == '03':
        sites = input('Digite o nome do site: ')
        if len(sites) <= 2:
            print('ERRO! Nenhum site foi adicionado.')
        else:
            try:
                rr = gerenciador[sites]
                print('Site já existente...')
            except KeyError:
                email, senha, url = ler_detalhes_site()
                incluir_editar_site(sites, email, senha, url)
    elif opcao == '4' or opcao == '04':
        sites = input('Digite o nome do site: ')
        try:
            rr2 = gerenciador[sites]
            print('>>> Editando sites:', sites)
            email, senha, url = ler_detalhes_site()
            incluir_editar_site(sites, email, senha, url)
        except KeyError:
            print('>>> Site Inexistente')
    elif opcao == '5' or opcao == '05':
        sites = input('Digite o nome do site a excluir: ')
        if len(sites) == 0:
            print('ERRO! digite o nome do site')
        else:
            excluir_site(sites)
    elif opcao == '6' or opcao == '06':
        nome_arquivo = input('Digite o nome do arquivo para ser exportado: ')
        exportar_site(nome_arquivo)
    elif opcao == '7' or opcao == '07':
        nome_arquivo = input('Digite o nome do arquivo a ser importado: ')
        importar_site(nome_arquivo)

    elif opcao == '0' or opcao == '00':
        print('Saindo...')
        sleep(3)
        break
    else:
        print('Opção Inválida...')
