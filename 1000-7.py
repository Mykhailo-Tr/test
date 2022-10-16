                                #1000-7
import time
a = 1000
time.sleep(0.5)
while a > 0:
    time.sleep(0.02)
    print(str(a)+'-'+'7'+'='+str(a-7))
    a-=7
