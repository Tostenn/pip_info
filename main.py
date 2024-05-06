from dependance import *
effter()

info = f'''{"info sur vos package":-^40}
| {"1 - lister tout mes packages": <37}|
| {"2 - rechercher un de mes package": <37}|
| {"3 - supprimer un package": <37}|
| {"0 - quitter": <37}|
{"T_xOx_T":-^40}
-> '''
print('chargements de la liste des packages ...')
package = [i.split('==')  for i in cmds('pip freeze').split('\n')]

choix = ''
while choix != 0:
    effter()
    choix = verch(info,erro=f'valeur innatendu!\n{barre}',fin=4)

    if choix == 1:
        for i in range(len(package)):
            print(f'{i+1} - package: {package[i][0]} | version={package[i][1]}')
        c = verch(
            info='entrer le numero d\'un package pour plus d\'information sur celui-ci (q pour quitter) : ',
            erro=f'valeur innatendu!\n{barre}',deb=1, fin=i+1,exp=['q']
        )
        if c != 'q':
            show_package(package[c-1][0])

    elif choix == 2:
        c = choice('entrer le nom du package a rechercher : ')
        data = search(c,package)
        if len(data):
            print('package trouver')
            if len(data) == 1:
                show_package(data[0][0])
                continue
            for i in range(len(data)):
                print(f'{i + 1} - {data[i][0]}')
            
            c = verch(
                info='entrer le numero d\'un package pour plus d\'information sur celui-ci (q pour quitter) : ',
                erro=f'valeur innatendu!\n{barre}',deb=1, fin=i+1,exp=['q']
            )
            if c != 'q':
                show_package(data[c-1][0])
            else : continue
            
        else : print(f'aucun package trouver avec ce nom dans votre systéme\n{barre}')
        input()
    
    elif choix == 3:
        effter()
        c = choice('entrer le nom du package a supprimer : ')
        data = search(c,package)

        if len(data):
            if len(data) >= 2:
                print('nous avons trouver plusieur packages')
                for i in range(len(data)):
                    print(f'{i + 1} - {data[i][0]}')
                c = choice('entrer les numéro des packages a supprimer (ex: 1,2,5 ) : ').split(',')
                for i in c:
                    try:
                        del_package(data[int(i) - 1][0])
                        package.pop(data[int(i) - 1][1])
                    except: pass
            else :
                del_package(data[0][0])
                package.pop(data[0][1])
            print(package)

        else : 
            print(f'aucun package trouver avec ce nom dans votre systéme\n{barre}')
        input()