import pyautogui as p
import time as t


print("iniciou")
def wait(seconds):
    t.sleep(seconds)

def type_with_interval(text, interval=0.25):
    p.write(text, interval=interval)
def press_keys(*keys, interval=0.25):
    p.hotkey(*keys, interval=interval)


def ambiente():
    print("entrou no ambiente")
    p.press('win', interval=0.25)
    wait(2)
    type_with_interval('SAP Logon')

    p.press('enter')
    wait(4)
    press_keys('alt', 'o')
    wait(4)

    user = "ASALVADOR"
    senha = "kmi2023"
    type_with_interval(user)
    press_keys('tab')
    type_with_interval(senha)
    press_keys('enter')
    press_keys('enter')
    wait(4)

    transacao = "ZTSD017"
    type_with_interval(transacao)
    press_keys('enter')
    wait(4)
    print("saiu no ambiente")

if __name__ == "__main__":
    ambiente()