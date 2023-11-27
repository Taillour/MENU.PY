#| __    __ |
#|  |    |  |
#|    \/    |
#|          |
# \________/
import time
while True:
    
    print("\n                           ----------Menu----------")
    time.sleep(0.8)
    print("                         - [1] New")
    time.sleep(0.8)
    print("                         - [2] Edit")
    time.sleep(0.8)
    print("                         - [3] Open")
    time.sleep(0.8)
    print("                           ------------------------")

    mmchoice = input("                           = ")

    if mmchoice == "1":
        print ("\n                             ('New' Option Chosen)")
        break
    
    elif mmchoice == "2":
        print ("\n                            ('Edit' Option Chosen)")
        break
    
    elif mmchoice == "3":
        print ("\n                            ('Open' Option Chosen)")
        exec(open('2page.py').read())
        break
        

    
#this is gonna get VERY cluttered
