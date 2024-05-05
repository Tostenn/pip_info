from os import system
from sys import platform
from subprocess import run

def effter() -> None:
    '''efface le terminal'''
    system("cls") if platform == "win32" else system("clear")

def cmds(cmd:str, code:bool=False) -> str:
    '''exercuter des commande shell'''
    cmd = run(cmd,capture_output=True,text=True,shell=True)
    if code: return cmd.returncode
    return cmd.stdout.strip()

def ver_t(t1,t2):
    '''fonction vérifie si deux variable on le même type'''
    return type(t1) == type(t2)

def verch(info,erro = 'valeur innatendu!', deb = 0,fin = 3,arret=True,exp=[]):
    '''verifier l'entrer de l'utilisateur'''
    l= list(range(deb,fin+1)) if str(fin).isdigit() else []
    veri = True
    arret = arret if str(arret).isdigit() == True else True
    choix = ''
    while veri and arret:
        choix = input(info)
        if choix.isdigit():
            choix = int(choix)
            if ver_t(exp,[]):
                try:
                    el = exp.index(choix)
                    return exp[el]
                except: pass
            if choix in l: 
                veri = False
                break

            if fin == True:
                veri = False
                break
            else: print(erro)
        else:
            if ver_t(exp,[]):
                try:
                    el = exp.index(choix)
                    return exp[el]
                except: pass
            print(erro)
        if not ver_t(arret,True):
            arret -= 1
            if arret <= 0:veri = False 
    return choix

barre = f"{'-':-^50}"

def show(_):
    '''afficher personnaliser avec des --'''
    print(f'{barre}\n{_}\n{barre}')

def search(_:str, item:list):
    '''recherche dans une liste un element'''
    data = []
    for i in item:
        if _ in i[0]:
            data.append(i[0])
    return data

def show_package(_):
    '''affichache d'un package'''
    effter()
    cmd = cmds(f'pip show {_}')
    show(cmd)
    input()

def choice(info:str, error:str = f'valeur innatendu!\n{barre}') -> str:
    """force l'utilisateur a entrer uns valeur"""
    c = ''
    while not c:
        c = input(info)
        if not c: print(error)
    return c
