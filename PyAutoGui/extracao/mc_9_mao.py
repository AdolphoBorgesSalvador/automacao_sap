import pyautogui as p
import time as t

def wait(seconds):
    t.sleep(seconds)

def type_with_interval(text, interval=0.25):
    p.write(text, interval=interval)

def press_keys(*keys, interval=0.25):
    p.hotkey(*keys, interval=interval)

def press_key_with_repeats(key, repeats=1):
    p.press(key, presses=repeats)

transacao = "mc.9"
tipo_material = "PCCC"
mes_inicial = "11.2022"
mes_final = "10.2023"
caminho = "C:\\Users\\fsp_adolpho.salvador\\Desktop\\RELATORIOS\\"

wait(4)

def mc9_mao():
    print("entrou no mc.9")
    type_with_interval(transacao)
    press_keys('enter')
    wait(4)
    press_key_with_repeats("tab", repeats=2)
    wait(5)
    press_keys("enter")

    for ce_code in ["ce01", "ce02", "ce07"]:
        type_with_interval(ce_code)
        press_keys("enter")
        press_keys("down")
        wait(4)

    press_keys("f8")
    wait(4)

    press_key_with_repeats("down", repeats=3)
    press_key_with_repeats("tab", repeats=2)

    type_with_interval(tipo_material)

    press_key_with_repeats("down", repeats=3)

    press_keys('ctrl', 'a')
    type_with_interval(mes_inicial)
    press_keys('tab')
    type_with_interval(mes_final)
    press_keys("f8")
    wait(4)
    press_keys('ctrl', 'f')
    type_with_interval("QtdEst.avaliado")
    press_keys("down")
    press_keys("space")
    wait(2)
    press_keys("down")
    press_keys("space")
    wait(2)
    press_keys("enter")
    wait(4)
  

    press_keys('ctrl', 'g')
    wait(2)
    press_keys('f2')
    wait(4)
    press_keys('ctrl', 'shift', 'f4')
    wait(4)
    press_keys('shift', 'f8')
    press_keys("down")
    press_keys("enter")
    wait(5)
    press_keys("up")
    press_keys('ctrl', 'a')
    type_with_interval(caminho)
    press_keys('tab')
    type_with_interval("mc.9 MAO.xls")
    wait(3)
    press_keys("ctrl",'s')
    wait(10)
    press_keys('alt', 'p')
    wait(5)
    press_keys('alt', 'p')
    wait(5)
    press_keys('f12')
    press_keys('f12')
    press_keys('f12')
    press_keys('f12')
    press_keys('f12')
    press_keys('f12')
    press_keys('f12')
    press_keys('f12')
    press_keys('f12')

    print("saiu do mc.9")

if __name__ == "__main__":
    mc9_mao()