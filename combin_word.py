################################################
#                 MARLON SOUSA                 #
#                   CYBERBOT                   #
################################################
import itertools
from time import sleep

print("\033[32mDesenvolvido por  MARLON SOUSA\nCYBERBOT\033[m")

def func1():
    permuta = list(itertools.permutations(lista, 1))
    with open('wordlist.txt', 'w') as arquivos:
        for palavras in permuta:
            
            def listToString(s):  
                
                str1 = ""  
                

                for ele in s:  
                    str1 += ele   
                
                arquivos.write(f'{str1}\n')
                return str1  
        
            
            print(listToString(s=palavras)) 


def func2():
    permuta = list(itertools.permutations(lista, 2))
    with open('wordlist.txt', 'a') as arquivos:
        for palavras in permuta:
            
            def listToString(s):  
                
                str1 = ""  
                

                for ele in s:  
                    str1 += ele   
                
                arquivos.write(f'{str1}\n')
                return str1  
        
            
            print(listToString(s=palavras)) 


def func3():
    permuta = list(itertools.permutations(lista, 3))
    with open('wordlist.txt', 'a') as arquivos:
        for palavras in permuta:
            
            def listToString(s):  
                
                str1 = ""  
                

                for ele in s:  
                    str1 += ele   
                
                arquivos.write(f'{str1}\n')
                return str1  
        
            
            print(listToString(s=palavras)) 


def func4():
    permuta = list(itertools.permutations(lista, 4))
    with open('wordlist.txt', 'a') as arquivos:
        for palavras in permuta:
            
            def listToString(s):  
                
                str1 = ""  
                

                for ele in s:  
                    str1 += ele   
                
                arquivos.write(f'{str1}\n')
                return str1  
        
            
            print(listToString(s=palavras)) 

lista = []

def inserir():
    while True:
        print("\033[32m=-\033[m"*50)
        palavra = input("Digite [S] para sair\nPalavra Chave:")
        
        if palavra == 'S' or palavra == 's':
            break

        else:
            lista.append(palavra)
            continue 






inserir()
func1()
func2()
func3()
func4()


