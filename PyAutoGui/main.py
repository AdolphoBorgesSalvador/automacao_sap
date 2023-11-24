import pyautogui as p
import time as t
import keyboard
from mapas.vix_module import vix
from mapas.mao_module import mao
from mapas.ambiente_module import ambiente
from mapas.geral_module import geral
from extracao.mc_9_vix import mc9_vix
from extracao.mc_9_mao import mc9_mao

def check_for_interrupt():
    return keyboard.is_pressed('Esc')

def main():
    print("Entrou no main2")
    #ambiente()
    #vix()
   # mao()
   # geral()
    mc9_vix()
    mc9_mao()

    p.alert(text='Código finalizado com sucesso.', title='Fim', button='OK')
    
if __name__ == "__main__":
    print("Pressione 'Esc' para interromper o código.")
    main()
    p.alert(text='Código finalizado com sucesso.', title='Fim', button='OK')
