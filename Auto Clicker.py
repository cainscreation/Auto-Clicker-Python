from pynput.mouse import Button , Controller
import random
import time
mouse = Controller()
timeout = time.time()+10 #seconds
i=time.time()
while i<timeout:
  a=random.random()*500
  b=random.random()*250
  mouse.move(-a,-b)
  mouse.move(a,b)
  print(mouse.position)
  mouse.click(Button.left, 2)
  i=time.time()
  
