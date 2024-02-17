from keyboard import Keyboard
from phone import Phone

class Device:
    def __init__(self, keyboard, phone):
        self.keyboard = keyboard
        self.phone = phone

    def type(self, text):
        self.keyboard.type(text)

    def call(self, number):
        self.phone.call(number)
