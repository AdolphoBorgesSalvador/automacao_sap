import pyautogui as p
import time as t
import pygetwindow as gw

print("iniciou")

def wait(seconds):
    t.sleep(seconds)

def type_with_interval(text, interval=0.25):
    p.write(text, interval=interval)

def press_keys(*keys, interval=0.25):
    p.hotkey(*keys, interval=interval)

def geral():
    print("entrou no geral")
    press_keys('shift', 'f5')
    wait(4)
    p.press('down', presses=1, interval=0.25)
    press_keys('f2')
    wait(4)
    press_keys('f8')
    wait(45)
    press_keys("alt")
    wait(5)
    press_keys("x")
    wait(5)
    press_keys("a")
    wait(5)
    press_keys('alt','s')
    wait(5)
    p.press("down")
    type_with_interval('r')
    wait(5)
    press_keys('alt', 'n')
    type_with_interval('GERAL.XLSX')
    p.press("enter")
    press_keys('alt', 's')
    wait(5)
    press_keys('alt', 'P')
    wait(5)
    press_keys('alt', 'P')
    target_window_title = "Mapa PSI - por centro"

    target_windows = gw.getWindowsWithTitle(target_window_title)

    if target_windows:
        target_window = target_windows[0]
    
        target_window.moveTo(0, 0)

        target_window.activate()

    wait(5)
    press_keys('shift', 'f3')

    print("saiu do geral")

if __name__ == "__main__":
    geral()