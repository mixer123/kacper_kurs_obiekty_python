import os, time
from screeninfo import get_monitors

from pynput.keyboard import Key, Controller
from pynput import  keyboard, mouse
from pynput.mouse import Button, Controller as MouseController
import subprocess
import webbrowser

class Controler:
    def __init__(self):
        self.keyboard = keyboard.Controller()
        self.mouse = mouse.Controller()
    def click_button_keyboard(self, key):
        self.keyboard.press(key)
        self.keyboard.release(key)

    def click_buttons_keyboard(self, key1, key2):
        self.keyboard.press(key1)
        self.keyboard.press(key2)
        self.keyboard.release(key1)
        self.keyboard.release(key2)
    def position(self, x,y):
        self.mouse.position = (x,y)
    def click_button_mouse(self, key, code):
        self.mouse.click(key, code)
    def type(self, text):
        self.keyboard.type(text)


controller = Controler()


os.chdir('/usr/bin/')
webbrowser.get('/usr/bin/firefox').open_new_tab('https://www.youtube.com/')
controller.position(int(get_monitors()[0].width*0.36), 136)
# print('mouse position', controller.position())
controller.click_button_mouse(Button.left, 1)
controller.type('Kacper Sieradziński')
time.sleep(5)
controller.click_button_keyboard(Key.enter)
time.sleep(5)
# controller.click_button_mouse(Button.left,1)
controller.position(1087, 534)
controller.click_button_mouse(Button.left, 1)
time.sleep(1)
# # Kliknięcie łapki w górę
controller.position(945, 981)
controller.click_button_mouse(Button.left, 1)
time.sleep(5)
# '''Zamkniecie okna z klawiatury alt+f4'''
controller.click_buttons_keyboard(Key.alt, Key.f4)

# keyboard.release(Key.alt)
# keyboard.release(Key.f4)
# '''  zamkniecie okna myszą'''
# # mouse.position = (1904, 47)
# # mouse.click(Button.left, 1)
# # print('The current pointer position is {0}'.format(mouse.position))
# # keyboard.press(Key.f11)
# # keyboard.release(Key.f11)
