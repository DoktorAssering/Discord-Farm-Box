import pyautogui
import time
import keyboard

def click_at_position(x, y, delay=0):
    pyautogui.moveTo(x, y, duration=0.2)
    time.sleep(delay)
    pyautogui.click()

running = True

def stop_loop():
    global running
    running = False

keyboard.add_hotkey('ctrl+shift+x', stop_loop)

while running:
    x_coord = 1175
    y_coord = 120
    click_at_position(x_coord, y_coord)
    x_coord = 1020
    y_coord = 500
    click_at_position(x_coord, y_coord)
    #time.sleep(0.1)
    x_coord = 1175
    y_coord = 120
    click_at_position(x_coord, y_coord)
    #time.sleep(0.1)