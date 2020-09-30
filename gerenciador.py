#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Gerenciador de senhas by: Juvenal Cullyno
# Deixem os créditos:
# Juvenal Culino | Facebook: https://www.facebook.com/jose.juvenal.00
#                | Github: https://github.com/juvenalculino
import base64
import os
from time import sleep
from random import choice

gerenciador = {}
azul = '\033[1;34m'
verm = '\033[1;31m'
preto = '\033[1;30m'
cyanfun = '\033[1;106m'
reset = '\033[0;0m'
cores = ('\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;34m', '\033[1;35m', '\033[1;36m')


def banner():
    """
    Aqui é apenas o banner do script
    :return: Retorna o logo personalizado
    """
    logo = """
  ___                           _           _
 / __| ___  _ _  ___  _ _   __ (_) __ _  __| | ___  _ _
| (_ |/ -_)| '_|/ -_)| ' \ / _|| |/ _` |/ _` |/ _ \| '_|
 \___|\___||_|  \___||_||_|\__||_|\__,_|\__,_|\___/|_|
                                  """
    print()
    print(choice(cores), 'By: Juvenal Culino', reset)
    print(choice(cores) + logo + reset)


# Menu
banner()


def menu():
    """
    Função que retorna o menu de opções.
    :return: menu com as opções
    """
    print(f'{preto}=={reset}' * 28)
    print(f'{preto}Seja bem vindo(a){reset}'.rjust(34))
    print('''{}
    {}Escolha a opção:{}
    [1] Mostrar Dados
    [2] Buscar Site
    [3] Incluir site/senha
    [4] Excluir
    [5] Exportar para csv
    [6] Importar csv
    \n    [0] Sair{}'''.format(choice(cores), choice(cores), choice(cores), reset))
    print(f'{preto}=={reset}' * 28)
    option = input(f'{choice(cores)}\n=>> {reset}')
    executar_menu(option)
    return


def executar_menu(option):
    """
    Funcionalidade para o menu de opções
    :param option: limpeza da tela em sistemas posix e so
    :return: Retorna o loop do menu e limpeza da tela cls em sist. win e clear em linux.
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    ch = option.lower()
    if ch == '':
        menu_action['menu']()
    else:
        try:
            menu_action[ch]()
        except KeyError:
            print(f'{verm}Opção inválida, Tente novamente{reset}')
            menu_action['menu']()
    return


# Funções
def mostrar_site():
    """
    Retorna todos os sites.
    :return: Retorna os dados salvos no gerenciador or no arquivo salvo 'senhas.csv'
    """
    if len(gerenciador) > 0:
        try:
            sim = input(f"{verm}Deseja ver as senhas criptografadas em base64?{reset} [s|n]: ")
            for sites in gerenciador:
                if sim == 's'.lower():
                    print(f'{choice(cores)}--------------------------------')
                    print('site:'.rjust(6), sites)
                    print('email:', gerenciador[sites]['email'])
                    sen = 'senha:', gerenciador[sites]['senha']
                    sen1 = sen[1]
                    men_bytes = sen1.encode('ascii')
                    b64_bytes = base64.b64encode(men_bytes)
                    base64_men = b64_bytes.decode('ascii')
                    print('senha:', base64_men)
                    print('url:'.rjust(6), gerenciador[sites]['url'])
                    print(f'--------------------------------{reset}')
                else:
                    print(f'{choice(cores)}--------------------------------')
                    print('site:'.rjust(6), sites)
                    print('email:', gerenciador[sites]['email'])
                    print('senha:', gerenciador[sites]['senha'])
                    print('url:'.rjust(6), gerenciador[sites]['url'])
                    print(f'--------------------------------{reset}')
        except KeyError:
            print(f'{verm}Lista vazia...{reset}')
    menu()


def buscar_site():
    """
    Busca com nome específico do site salvo no arquivo 'senhas.csv'.
    :return: Retorna o nome específico caso contrário retorna o KeyError.
    Temos a opção de visualizar os arquivos criptografados em base64, basta comentar a linha 85 -> senha,
    e descomentar as linhas 88 à 93.
    """
    sites = input(f'{cyanfun}Digite o nome do site:{reset} ')
    print()
    try:
        sim = input(f"{verm}Deseja ver as senhas criptografadas em base64?{reset} [s|n]: ")
        if sim == 's':
            print(f'{choice(cores)}--------------------------------')
            sen = 'senha:', gerenciador[sites]['senha']
            sen1 = sen[1]
            men_bytes = sen1.encode('ascii')
            b64_bytes = base64.b64encode(men_bytes)
            base64_men = b64_bytes.decode('ascii')
            print('site:'.rjust(6), sites)
            print('email:', gerenciador[sites]['email'])
            print('url:'.rjust(6), gerenciador[sites]['url'])
            print('senha:', base64_men)
            print(f'--------------------------------{reset}')
        else:
            print(f'{choice(cores)}--------------------------------')
            print('site:'.rjust(6), sites)
            print('email:', gerenciador[sites]['email'])
            print('senha:', gerenciador[sites]['senha'])
            print('url:'.rjust(6), gerenciador[sites]['url'])
            print(f'--------------------------------{reset}')

    except KeyError:
        print(f'{verm}Nome não encontrado...{reset}')

    except Exception as erro:
        print(f'{verm}>>> Erro: {erro} <<<{reset}')
    menu()


def incluir_editar_site():
    """
    Está função tem como funcionalidade inserir site, email, senha e url.
    :return: Recebe entrada de dados em conjunto com a função exportar, no qual tem a opção de salvar os dados.
    """
    sites = input(f'{cyanfun}Informe o nome do site: {reset}')
    if len(sites) < 3:
        print(f'{verm}\nErro. Informe o nome do site.{reset}\n')
    if sites in gerenciador is not True:
        print(f'{azul}Site existe...{reset}')
    else:
        email = input(f'{cyanfun}Digite o email:{reset} ')
        senha = input(f'{cyanfun}Digite a senha:{reset} ')
        url = input(f'{cyanfun}Digite a url: {reset}')
        gerenciador[sites] = {'email': email, 'senha': senha, 'url': url}
        salvar()
        print()
        print(f'{azul}Site {sites} Adicionado...{reset}')
        print()
    menu()


def excluir_site():
    """
    Exclui o site caso exista se não existir retorna erro.
    :return: Retorna o input para o utilizador digitar o nome do site a ser excluido.
    """
    try:
        sites = input(f'{verm}Digite o nome do site a excluir:{reset} ')
        gerenciador.pop(sites)
        if len(sites) == 0:
            print(f'{verm}ERRO! digite o nome do site{reset}')
        else:
            print(f'{azul}Site {sites} Removido..{reset}')

    except Exception as erro:
        print(f'{verm}erro: {erro} {reset}')
    menu()


def exportar_site():
    """
    Funcionalidade para exportar os dados para um arquivo csv.
    :return: Retorna um input para o utilizador digitar o nome desejado da saída do arquivo .csv
    """
    try:
        a = input(f'{cyanfun}Deseja salvar {reset}[s|n]').lower()
        if a == 's':
            b = input(f'{cyanfun}Digite o nome do arquivo: Padrão {reset}[senhas.csv] > ')
        else:
            return
        with open(b, 'w') as arq:
            for sites in gerenciador:
                email = gerenciador[sites]['email']
                senha = gerenciador[sites]['senha']
                url = gerenciador[sites]['url']
                arq.write(f'{sites},{email},{senha},{url}\n')
        print(f'{azul}Sites Exportados com o nome: >>> {b} <<<{reset}')
    except Exception as erro:
        print(f'{verm}Erro {erro}...{reset}')
    menu()


def importar_site():
    """
    Faz importação de arquivo csv salvo no formato desejado
    :return: Retorna o input para o utilizador informar o arquivo csv a ser importado.
    """
    try:
        arquivo = input(f'{cyanfun}Digite o nome do arquivo a ser importado:{reset} ')
        with open(arquivo, 'r') as arq:
            linhas = arq.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')
                nome = detalhes[0]
                email = detalhes[1]
                senha = detalhes[2]
                url = detalhes[3]
                gerenciador[nome] = {'email': email, 'senha': senha, 'url': url}
                # print('>>>> Database carregado com sucesso')
                print(f'{choice(cores)}>>>> {len(gerenciador)} contatos carregados{reset}')

    except FileNotFoundError:
        print(f'{verm}>>> Arquivo encontrado...{reset}')

    except Exception as erro:
        print(f'{verm}Erro: {erro} {reset}')
    menu()


def salvar():
    exportar_site()
    menu()


def carregar():
    """
    Caso o arquivo esteja na pasta, ao rodar o script ele automaticamente carrega.
    :return: Retorna todos os dados salvos no arquivo 'senhas.csv'.
    """
    try:
        with open('senhas.csv', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')
                sites = detalhes[0]
                email = detalhes[1]
                senha = detalhes[2]
                url = detalhes[3]
                gerenciador[sites] = {'email': email, 'senha': senha, 'url': url}
        print(f'{choice(cores)}>>>> {len(gerenciador)} Sites carregados <<<<{reset}')

    except FileNotFoundError:
        print(f'{verm}Arquivo encontrado...{reset}')

    except Exception as erro:
        print(f'{verm}Ocorreu um erro...{verm}')
        print(erro)
    menu()


def exiting():
    print(f'{choice(cores)} Saindo...\n\n Deixem os créditos:\n '
          f'FACEBOOK: https://www.facebook.com/jose.juvenal.00\n GITHUB: https://github.com/juvenalculino\n{reset}')
    sleep(3)
    print(f'{choice(cores)} Volte sempre!{reset}')
    quit()


# def back():
# menu_action['menu']()


# Lista do menu
menu_action = {
    'menu': menu,
    '1': mostrar_site,
    '2': buscar_site,
    '3': incluir_editar_site,
    '4': excluir_site,
    '5': exportar_site,
    '6': importar_site,
    '0': exiting}
carregar()
menu()
