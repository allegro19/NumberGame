#!/usr/bin/python
import time
print('type in your name please')
name=raw_input()
print('hello '+name)
time.sleep(0.25)
print('do you want to play my game')
yes='0'
while yes!='no' and yes!='yes':
    #time.sleep(0.25)
    print('please type yes/no')
    yes=raw_input()
if yes=='no':
	print('ok then '+name)
	time.sleep(0.5)
	print('see you soon*****************')
else:
    print('what theme do you want')
    print('christmas or christmas lunch')
    time.sleep(1)
    print('type in wich you want')
    theme=raw_input()
    if theme=='christmas':
        print('type in a letter')
        time.sleep(0.5)
        print('type in a letter folowing')
        print('F,S,E,R,P,FA,')
        print('warning....please type it in in LOWERCASE')
        letter=raw_input()
        if letter=='f':
            print('FARTHER CHRISTMAS IS COMING TO TOWN***')
            print('YOUV BETTER WATCH OUT BECAUSE HES COMING TO ')
            time.sleep(1)
            print('TOWN YEHHH*************&&&&&&****************')
        elif letter=='s':
            print('SNOW MAN')
            time.sleep(0.25)
            print('you can have fun ****in the snow')
            print('you can even build a SNOWMAN!!!!!!!!!!!******')
        elif letter=='e':
            print('they help farther christmas can you giues what it is before')
            print('the answer apears on the screen????')
            time.sleep(8)
            print('ELVES!!!!!!***************')
        elif letter=='r':
            print('RUDOLF THE RED NOSED RAINDEER ')
            print('youll go doun in HIST-OR-YYYYYYYYYYYYYYYY')
        elif letter=='p':
            print('presents')
            print('you normally get them from your family and friends************')
        elif letter=='fa':
            print('FAMILY')
            print('ON CHRISTMAS THE MOST IMPORTANT THING IS')
            print('FAMILY YOU SHOW HOW MUCH YOU LOVE THEM BY STUFF LIKE GIVING*****')
        else:
            print('write doun the thing you want most for christmas '+name)
            present=raw_input()
            print(present+' that is a very nice thing '+name)
    if theme=='christmas lunch':
         print('what do you normally have for your ')
         time.sleep(1)
         print('christmas lunch????***********')
         lunch=raw_input()
         print('wow! '+lunch)
         print('they are really nice!!!!')
         print('type in weather you have christmas pudding')
         pudding=raw_input()
         if pudding=='yes':
             print('you are so lucky i have only had it once')
         if pudding=='no':
            print('i havent eather:(')
         print('type in your favorite thing for christmas lunch')

         favorite=raw_input()
         if favorite=='brustle sprowts':
            print('eeeeewwwwww i hate them')
            time.sleep(0.25)
            print('pooooooy')
         else:
            print(favorite+' those are very nice')
            

print('thank you for playing_************')
