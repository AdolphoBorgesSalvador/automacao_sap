import pygetwindow as gw
import pyautogui

# Suponha que você queira ativar a janela com o título "Mapa PSI - por centro"
target_window_title = "Mapa PSI - por centro"

# Obtenha a lista de janelas com o título desejado
target_windows = gw.getWindowsWithTitle(target_window_title)

# Se houver pelo menos uma janela com o título desejado, ative-a e mova para uma posição visível
if target_windows:
    target_window = target_windows[0]
    
    # Mova a janela para uma posição visível (0, 0)
    target_window.moveTo(0, 0)

    # Ative a janela
    target_window.activate()

    print(f"Janela '{target_window_title}' ativada.")
else:
    print(f"Janela '{target_window_title}' não encontrada.")
