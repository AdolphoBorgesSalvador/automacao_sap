import pyautogui as p
import time as t

def wait(seconds):
    t.sleep(seconds)

def type_with_interval(text, interval=0.35):
    p.write(text, interval=interval)

def press_keys(*keys, interval=0.4):
    p.hotkey(*keys, interval=interval)

def press_key_with_repeats(key, repeats=1):
    p.press(key, presses=repeats)

transacao = "ZYCIR075A"
tipo_material = "PCCC"
mes_inicial = "01112022"
mes_final = "01102023"
caminho = "C:\\Users\\fsp_adolpho.salvador\\Desktop\\RELATORIOS\\"

wait(5)
def fup():
    print("entrou no fup")
    type_with_interval(transacao)
    press_keys('enter')
    press_keys('shift', 'f5')
    press_keys('right')
    press_keys('f2')
    press_key_with_repeats("down", repeats=7)
    type_with_interval(mes_inicial)
    press_keys('tab')
    type_with_interval(mes_final)
    press_keys('f8')
    wait(8)
    press_keys('ctrl','shift','f6')
    wait(5)
    press_keys('down')
    wait(2)
    press_keys('enter')
    wait(3)
    press_keys('up')
    press_keys('ctrl','a')
    type_with_interval(caminho)
    press_keys('down')
    press_keys('ctrl','a')
    type_with_interval("fup.xls")
    wait(10)
    press_keys('enter')
    wait(5)
    press_keys('enter')
    wait(5)
    press_keys('alt','p')
    wait(5)
    press_keys('alt','p')
    wait(5)
    press_keys('alt','p')
    wait(5)
    press_key_with_repeats("esc", repeats=2)
    wait(5)
    press_key_with_repeats("enter", repeats=2)
    wait(5)
    press_key_with_repeats("esc", repeats=2)

if __name__ == "__main__":
    fup()
