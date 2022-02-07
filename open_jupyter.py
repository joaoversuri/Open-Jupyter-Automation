import pyautogui as auto

auto.hotkey('win','r')
auto.sleep(0.5)
auto.typewrite('cmd')
auto.press('enter')
auto.sleep(0.5)
auto.typewrite('python -m notebook')
auto.press('enter')
auto.hotkey('win','r')
auto.sleep(0.5)
auto.typewrite('chrome')
auto.press('enter')
auto.sleep(0.5)
auto.typewrite('http://localhost:8888/tree')
auto.press('enter')





