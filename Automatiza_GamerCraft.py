"""
# Este código automatiza a atividade de entrar no site https://gamercraft.com/ e solicitar os créditos
diários.
# Deve ser utilizado com o agendador de tarefas do windows
# pip install pyautogui
"""
import pyautogui
import time
import webbrowser


def coleta_creditos():
    website_url = "https://gamercraft.com/me/ladders"  # Site que se deseja abrir
    webbrowser.open(website_url)  # Abre o site com o navegador padrão
    time.sleep(5)
    for i in range(2):
        pyautogui.press('tab')

    pyautogui.press("enter")

    time.sleep(5)
    for i in range(7):
        pyautogui.press("tab")

    pyautogui.press("enter")

    time.sleep(2)
    pyautogui.press("tab")
    pyautogui.press("enter")


coleta_creditos()
