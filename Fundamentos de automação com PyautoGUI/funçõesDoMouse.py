from turtle import left, right
import pyautogui
import time

#Dá ao arquivo python tempo antes de iniciar 
time.sleep(3)

#|--------------- Funções do Mouse ---------------|
print(pyautogui.size()) #Printa a resolução da sua tela
print(pyautogui.position())
#Detalhe: Só nesses códigos já é calculado o Size(width=1920, height=1080) e o valor da posição X e Y do mouse (x=676, y=204), exemplo. 

pyautogui.moveTo(100, 100, 1) #Mover o cursor para X, Y em 1 segundo(velocidade. SHOW DE BOLA!!! 
pyautogui.moveRel(1700,-50,1) #Move-se a distância relativa da atual, "calculado para Run Python File" :)

#|--------------- Funções de Clicar ---------------|
pyautogui.click(500, 500, 1, 3, button="left")#X, Y, Numero de cliques, Velocidade, Botão.
#Temos outras funções como: pyautogui.leftClick / pyautogui.rightClick / pyautogui.doubleClick...

#|--------------- Função Scroll / Rolar rodinha do mouse  ---------------|
pyautogui.scroll(-800)#-X negativo, rolando para baixo, depois de 3 seg.

#|--------------- Automatizando o mouse: Movimentando e Clicando ---------------|
#Você pode abrir o paint, e observar como funciona esta função
pyautogui.mouseDown(300, 400, button= "Left")
pyautogui.moveTo(800, 400, 3)
pyautogui.mouseUp()
pyautogui.moveTo(1000, 400, 3)
