import mouse
import keyboard
import time
# import only system from os
from os import system, name, remove, path


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')




run = True
f = open('data_K', 'r')
key = f.readline()
f.close()
f = open('data_I', 'r')
intervals = f.readline()
f.close()
autoclicker = False
keyholder = False
Macro_Menu = False
standby = False
clicks = 0
while run:
    print('######################\nAutoClicker\nBy ultraflame42\n######################')
    time.sleep(0.5)
    print('\nHot Key > %s\nIntervals > %s \n' % (key, intervals))
    time.sleep(0.5)
    print('----------------------\nOptions\n----------------------')
    print('-a > Change Unievrsal Hotkey  -b > Change Auto Clicker Interval\n\n-c > AutoClicker                  -d > Key Holder \n\n-e > Macro Menu')
    print('\n[==========================================]')
    options = input('->')
    if options == '-a':
        print('\n\n\n\n')
        clear()
        print('######################\nAutoClicker\nBy ultraflame42\n######################')
        print('[][][][][][][][][][]\nKey > %s\nCurrent Interval > %s \n[][][][][][][][][][]' % (key, intervals))
        key = input('New Hot key ->')
        f = open('data_K', 'w+')
        f.write(key)
        f.close()
    elif options == '-b':
        print('\n\n\n\n')
        clear()
        print('\nCurrent Key > %s\nInterval > %s \n' % (key, intervals))
        intervals = input('New Interval (INTEGERS ONLY) ->')
        f = open('data_I', 'w+')
        f.write(str(intervals))
        f.close()
    elif options == '-c':
        time.sleep(1)
        print('Auto Clicker On Standby \nPress Hotkey [%s] To Start' % (key))
        standby = True
    elif options == '-d':
        print('\n\nKey To Hold\nUse "+" In Between Characters Without space To Hold Multiple Keys')
        holdkey = input('INPUT >').lower()
        standby = True
    elif options == '-e':
        Macro_Menu = True


    while Macro_Menu:
        clear()
        print('######################\nAutoClicker\nBy ultraflame42\n######################')
        print('Macro Menu\n*********************\nDisclaimer:\nThe Macros Are Not Really Macros\nThey Are More Like Stored Keystrokes\n*********************')
        print('\n-a > View \ Activate Macros    -b > Create New Macro')
        macromenu_user_input = input('->')

        if macromenu_user_input == '-a':
            clear()
            print('######################\nAutoClicker\nBy ultraflame42\n######################')
            print('Macro Menu\n*********************\nDisclaimer:\nThe Macros Are Not Really Macros\nThey Are More Like Stored Keystrokes\n*********************')
            print('Macro List:\n********************************************')
            f = open('data_macro', 'r')
            f.readline()
            macrolist = f.read()
            print(macrolist)
            f.close()
            print('********************************************')
            print('-a > Select Macro -b > Delete Macro')
            print('============================================')
            macrolist_input = input('>')
            if macrolist_input == '-b':
                macro_del = input('Enter Macro Name ->')
                new_macrolist = macrolist.replace(str('\n' + macro_del), '')
                f = open('data_macro', 'w')
                f.write('0\n' + new_macrolist)
                f.close()
                if path.exists('Macros/' + macro_del):
                    remove('Macros/' + macro_del)
            elif macrolist_input == '-a':
                macro_activate = input('Enter Macro Name ->')
                f = open(('Macros/' + macro_activate), 'r')
                play_macro = f.read()
                f.close()
                
                macro_play = True
                while macro_play:
                    clear()
                    print(play_macro)
                    print('[PRESS HOTKEY (%s) TO ACTIVATE SELECTED MACRO]' % (key))
                    if keyboard.is_pressed(key):
                        keyboard.play(str(play_macro), 0)
                        macro_play = False

        elif macromenu_user_input == '-b':
            new_macro_name = input('New Macro Name ->')
            new_macro = keyboard.record(until='escape')
            f = open(('Macros/' + new_macro_name), 'w+')
            f.write(str(new_macro))
            f.close()
            f = open('data_macro', 'a')
            f.write('\n' + new_macro_name)
            f.close()
            pass


    while standby:
        if keyboard.is_pressed(key):
            time.sleep(1)
            standby = False
            if options == '-c':
                print('[AUTO CLICKER STARTED]')
                autoclicker = True
            elif options == '-d':
                keyholder = True
                print('\n\n\n\n')
                clear()
    while keyholder:
        print('Holding [%s] key' % (holdkey))
        keyboard.press(hotkey=holdkey)
        if keyboard.is_pressed(key):
            keyholder = False
    while autoclicker:
        print('\n\n\n\n')
        clear()
        print('######################\nAutoClicker\nBy ultraflame42\n######################')
        print('[AUTO CLICKER ENABLED]\n[Clicks] %s \n ######################' % (clicks))
        if keyboard.is_pressed(key):
            autoclicker = False
        clicks += 1
        time.sleep(float(intervals))
        mouse.click(button='left')
    if clicks != 0:
        print('Clicked ' + str(clicks) + ' Times')
        time.sleep(0.5)

    print('\n\n\n\n')
    clear()
