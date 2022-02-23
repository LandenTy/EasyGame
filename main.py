"""
Main

Description:
"""
from EasyGame import Button
from EasyGame import AudioSource
from EasyGame import Switch

# Program
one = Button(150, 150, 500, 100, (9, 132, 227), "Hello!")
two = Switch(150, 130, 500, 100, (116, 185, 255), "Hello!")
source = AudioSource("Bubbles", False, True)

while True:
    running = True
