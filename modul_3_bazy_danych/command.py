import os, time


from pynput.keyboard import Key, Controller
from pynput import  keyboard
from pynput.mouse import Button, Controller as MouseController
import subprocess
import webbrowser
keyboard = Controller()
mouse = MouseController()

os.chdir('/usr/bin/')
webbrowser.get('/usr/bin/firefox').open_new_tab('https://www.youtube.com/')
mouse.position = (701, 152)
mouse.click(Button.left, 1)
keyboard.type('Kacper Sieradziński')
time.sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(1)
mouse.position = (1146, 479)
mouse.click(Button.left, 1)
time.sleep(1)

mouse.position = (945, 981)
mouse.click(Button.left, 1)
time.sleep(10)
keyboard.press(Key.alt)
keyboard.release(Key.alt)
keyboard.press(Key.f4)
keyboard.release(Key.f4)
'''  zamkniecie okna myszą'''
# mouse.position = (1904, 47)
# mouse.click(Button.left, 1)
# print('The current pointer position is {0}'.format(mouse.position))
# keyboard.press(Key.f11)
# keyboard.release(Key.f11)

