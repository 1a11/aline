import sp_recog as sp
import comand_editor as editor
import os

while True:
    print('Choose interface:')
    print('1. Speech recognition')
    print('2. Comand editor')
    print('3. EXIT')
    n = int(input())
    os.system('cls')
    if n == 1:
        sp.repeat()
    elif n == 2:
        print('EDIT:')
        print('1. Object list')
        print('2. Comand list')
        n = int(input())
        os.system('cls')
        if n == 1:
            editor.edit_obj_list('objects.txt')
        elif n == 2:
            editor.edit_obj_list('comands.txt')
    elif n == 3:
        break
