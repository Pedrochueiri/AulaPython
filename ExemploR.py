hh = 0
while hh < 24:
    mm = 0
    if hh == 24:
        break
    while mm < 60:
        ss = 0
        if  mm == 56:
            break
        while ss < 60:
            print(f'{hh:02}:{mm:02}:{ss:02}')
            ss += 1
            if (hh == 23 and mm == 55 and ss == 1):
                break
        mm += 1
    hh += 1 
    print('Alarme')
    
    