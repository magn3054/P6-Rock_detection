import time

timeNOW = time.localtime()
timeNOW = time.strftime("%d-%m_%H;%M", timeNOW)

print(timeNOW)