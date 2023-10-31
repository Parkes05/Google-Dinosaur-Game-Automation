import pyautogui, time, PIL


# screenwidth, screenheight = pyautogui.size()
# # print(screenwidth, screenheight)

# currentMouseX, currentMouseY = pyautogui.position()
# # print(currentMouseX, currentMouseY)

pyautogui.hotkey('alt', 'tab')

time.sleep(2)
pyautogui.click(200, 70)
pyautogui.write('https://elgoog.im/dinosaur-game/', interval=0.1)
pyautogui.press('enter')

time.sleep(6)
pyautogui.press('space')

pyautogui.moveTo(455, 735)
time.sleep(3)
while True:
    for i in pyautogui.screenshot().crop((400, 635, 550, 785)).getcolors():
        if i[1] == (83, 83, 83):
            pyautogui.press('space')


