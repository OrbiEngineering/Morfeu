listx = [825,823.1,817.5,808.25,795.75,780.35,762.5,742.75,721.7,702.2,678.3,657.25,637.5,619.65,604.25,591.75,582.52,577,575]
listy = [300,278.3,257.24,237.5,219.66,204.25,191.75,182.55,177,174,174,177,182.55,191.75,204.25,219.66,237.5,257.24,278.3,300]
radiouslist = [0,0,0,0,0,0]
for i in listx:
    radiouslist[0] = 700
    radiouslist[1] = (((i-700)/5)*1)+700
    radiouslist[2] = (((i-700)/5)*2)+700
    radiouslist[3] = (((i-700)/5)*3)+700
    radiouslist[4] = (((i-700)/5)*4)+700
    radiouslist[5] = (((i-700)/5)*5)+700
    print("--------{}------".format(i))
    print(radiouslist)
    radiouslist.reverse()
    print(radiouslist)
for i in listy:
    radiouslist[0] = 300
    radiouslist[1] = (((i-300)/5)*1)+300
    radiouslist[2] = (((i-300)/5)*2)+300
    radiouslist[3] = (((i-300)/5)*3)+300
    radiouslist[4] = (((i-300)/5)*4)+300
    radiouslist[5] = (((i-300)/5)*5)+300
    print("--------{}------".format(i))
    print(radiouslist)
    radiouslist.reverse()
    print(radiouslist)
