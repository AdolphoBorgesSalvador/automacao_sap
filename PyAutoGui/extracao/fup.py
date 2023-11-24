import pyautogui as p
import time as t

def wait(seconds):
    t.sleep(seconds)

def type_with_interval(text, interval=0.25):
    p.write(text, interval=interval)

def press_keys(*keys, interval=0.2):
    p.hotkey(*keys, interval=interval)

def press_key_with_repeats(key, repeats=1):
    p.press(key, presses=repeats)

transacao = "ZYCIR075A"
tipo_material = "PCCC"
mes_inicial = "11.2022"
mes_final = "10.2023"
caminho = "C:\\Users\\fsp_adolpho.salvador\\Desktop\\RELATORIOS\\"


def fup():
    print("entrou no fup")
    type_with_interval(transacao)
    press_keys('enter')
    





if __name__ == "__main__":
    fup()
