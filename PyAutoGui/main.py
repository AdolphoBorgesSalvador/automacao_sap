import pyautogui as p
import time as t
import keyboard
from modulo.vix_module import vix
from modulo.mao_module import mao
from modulo.ambiente_module import ambiente
from modulo.geral_module import geral

def check_for_interrupt():
    return keyboard.is_pressed('Esc')

def main():
    print("Entrou no main2")
    ambiente()
    vix()
    mao()
    geral()

    p.alert(text='Código finalizado com sucesso.', title='Fim', button='OK')
    
if __name__ == "__main__":
    print("Pressione 'Esc' para interromper o código.")
    main()
    p.alert(text='Código finalizado com sucesso.', title='Fim', button='OK')
