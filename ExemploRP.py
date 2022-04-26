from time import sleep

while True:
    x = int(input('Digite a hora: '))
    y = int(input('Digite o minuto: '))
    z = int(input('Digite o segundo: '))
    hh = 0
    while hh < 24:
        mm = 0
        if hh == x + 1:
            break
        while mm < 60:
            ss = 0
            if  mm == y + 1:
                break
            while ss < 60:
                ss += 1
                print(f'{hh:02}:{mm:02}:{ss:02}')
                if (hh == x and mm == y and ss == z):
                    break
            mm += 1
        hh += 1 
        print('Alarme')
    d = str(input('quer executar o codigo de novo: '))
    if d == 's':
        continue
    else:
        break
    