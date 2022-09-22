import time
import unicodedata
def countdown(t): 
	while t: 
		mins, secs = divmod(t, 60) 
		timer = '{:02d}:{:02d}'.format(mins, secs) 
		print(timer, end="\r") 
		time.sleep(1) 
		t -= 1
h=int(input("enter the number of hours if any otherwise enter 0: "))
m=int(input("enter the number of minutes if any otherwise enter 0: "))
s=int(input("enter the number of seconds if any otherwise enter 0: "))
t=(h*60*60)+(m*60)+s
countdown(int(t))
print("TIME UP!!!","\U0001F55B")