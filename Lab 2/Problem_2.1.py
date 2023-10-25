# Problem 2.1: Writing lyrics

def we_wish_you(x):
    for number in range(x):
        print("We wish you a Merry Christmas")
    print ("We wish you a Merry Christmas and a Happy New Year\n")

def good_tiding(x):
    for i in range(x):
        print("Good tidings we bring to you and your kin")
    print("We wish you a Merry Christmas and a Happy New Year\n")

def figgy_wont_go(figgy,figgy_extended,wont_go,wont_go_extended):
    
    for number in range(figgy):
        print("Now bring us some figgy pudding")
    for number in range(figgy_extended):
        print("Now bring us some figgy pudding, now bring some out here\n")
    for number in range(wont_go):
        print("We won't go until we get some")
    for number in range(wont_go_extended):
        print("We won't go until we get some, so bring some out here\n")


we_wish_you(2)
good_tiding(1)
figgy_wont_go(2,1,0,0)
good_tiding(1)
figgy_wont_go(0,0,2,1)
good_tiding(1)
we_wish_you(2)

