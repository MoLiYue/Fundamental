#------------------------------------------------------
import random
import this
a = []
for i in range(29):
    a.append(i*7)
    #a[i] = i*7
#print(a)
b = a.copy()
#print(len(b))
del b[0:(int)(len(a)/2)]
#print(b)
c = a.copy()
del c[(int)(len(a)/2):]
#print(c[::-1])
d = c[::-1]+b
print(d)
#----------------------------------------------------------
room = [(),(),(),()]
people = [("A",),("B",),("C",),("D",),("E",),("F",),("G",),("H",),("I",)]
for i in people:
    #print(i)
    tem = int(random.random()*10)
    #print(tem)
    if(tem % 4 == 0):
        room[0] += i
    elif(tem % 4 == 1):
        room[1]+= i
    elif(tem % 4 == 2):
        room[2] += i
    else:
        room[3] += i
print(tuple(room))
#--------------------------------------------------------------------------------
lib = ["1","2","3","4","5","6","7","8","9","0"]
def random_str(length):
    tempString = ""
    for i in range(length):
        randTem = random.randint(0,2)
        if(randTem == 0):
            randTemStr = chr(random.randint(48,57))
        elif(randTem == 1):
            randTemStr = chr(random.randint(65, 90))
        else:
            randTemStr = chr(random.randint(97, 122))
        #print(randTemStr)
        tempString += randTemStr
    print(tempString)
    print(list(set(tempString)))

random_str(200)
#-------------------------------------------------------------------------------------
class Circle:
    def __init__(self,r):
        self.r = r
    def s(self):
        return 3.14 * self.r*self.r
    def C(self):
        return 3.14 * self.r * 2

circle1 = Circle(9)
print(circle1.s())
print(circle1.C())

circle2 = Circle(16)
print(circle2.s())
print(circle2.C())
#---------------------------------------------------------------------------------------------
old = open("../hamlet.txt", 'r')
l = []
txtTemp = old.read()
#print(txtTemp)
for line in txtTemp:
        for letter in line:
            l.append(letter.lower())
l3=''.join(l)
print(l3.count("hamlet"))
#print(l3)s
old.close()
new = open("../hamlet_sample.txt", "w")
new.write(l3)
new.close()