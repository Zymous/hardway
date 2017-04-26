# implements of ex19
from sys import argv

argv1,argv2,argv3 = argv

def output(numbers,name):
    print "the eggs we have are %d" % numbers
    print "the chicken name is %s" % name

n1 = raw_input("input a number: ")
n2 = raw_input("input a name: ")
output(12,"amy")
output(12+13,"amy"+"dom")
num = 10; name = "ddaa"
output(num,name)
output(num+10,name+"aa")
output(int(argv2),argv3)
output(int(argv2)+1,argv3+"aaa")
output(int(n1), n2)
