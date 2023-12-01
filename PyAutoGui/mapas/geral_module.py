import pyautogui as p
import time as t
import pygetwindow as gw

caminho = "C:\\Users\\fsp_adolpho.salvador\\Desktop\\RELATORIOS\\"

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
    wait(60)
    press_keys("alt")
    wait(5)
    press_keys("x")
    wait(5)
    press_keys("a")
    wait(5)
    type_with_interval('GERAL.XLSX')
    p.press('tab', presses=6, interval=0.25)
    wait(5)
    p.press("space")
    wait(5)
    type_with_interval(caminho)
    wait(5)
    press_keys('alt', 'l')
    wait(3)
    press_keys('alt', 's')
    wait(3)
    press_keys('alt', 'p')
    wait(3)
    press_keys('alt', 'p')
    wait(20)

    target_window_title = "Mapa PSI - por centro"

    target_windows = gw.getWindowsWithTitle(target_window_title)

    if target_windows:
        target_window = target_windows[0]
    
        target_window.moveTo(0, 0)

        target_window.activate()

    wait(5)
    press_keys('shift', 'f3')
    wait(3)
    press_keys('shift', 'f3')
    print("saiu do geral")

if __name__ == "__main__":
    geral()