# Symbol Review
# import os
# from os import path
x = 5; y = 4
# if x == 5 and y == 4:
#     print "Now you understand and symbol."
#
# with open('test.txt') as f:
#     print f.read()
#
# assert x > 0, 'actually x >=0'
# print "something"
#
# while x >0:
#     print x
#     if (x == 2):
#         break
#     x -= 1
# for i in range(5):
#     print i
#     if i == 3:
#         break
# class A:
#     i = '12345'
#     def pr(self):
#         print self.i
#
# a = A()
# a.pr()

# while x >0:
#     print x
#     if (x == 2):
#         continue
#     x -= 1
# def pr():
#     print "x = %d, y = %d" % (x, y)
# pr()
# a = ['a','b','c','d']
# b = 'abcd'
# del a[0]
# del b
# print a, "and "
# if x > 5:
#     print 'x > 5'
# elif x < 5:
#     print 'x < 5'
# else:
#     print 'x == 5'
# try:
#     a = 1/0
# except Exception as e:
#     print e
# exec 'print "bac"'
# try:
#     a = 1/0
# except Exception as e:
#     print  e
# finally:
#     print "finally goes here."
# for i in range(4):
#     print i
# def fun():
#     global x
#     print 'x = ',x
#     x = 80
#     print 'x = ',x
# fun()
# if x == 5:
#     print 'x = %r' % x
# if 1 in [1,2]:
#     print "yes"
# z = 5
# obj1 = {'a':'b'}
# obj2 = obj1.copy()
# if obj1 == obj2:
#     print "x == z"
# if obj1 is obj2:
#     print "x is z"
# if obj1 is obj1:
#     print "x is x"
# g = lambda x:x+2
# print g(2)

# if not x == 4:
#     print 'x != 4'

# if x == 5 or y == 10:
#     print "True"

# def func(): pass
# func()

# print "nothing at all."

# try:
#     if(x == 5):
#         raise TypeError
#     print "x is 5"
# except Exception as e:
#     print e
# def add(a, b):
#     return a + b
# print add(x, y)
# try:
#     x/0
# except Exception as e:
#     print e

# while x > 0:
#     print x
#     x -= 1

# with open('test.txt') as f:
#     print f.read()
# def fab(max):
#     a, b = 0, 1
#     while a < max:
#         yield a
#         a, b = b, a + b
# for i in fab(20):
#     print i,

# a = True
# b = False
# c = None
# d = "abc"
# e = 1
# f = 1.4
# h = ['a','b']
# i = {'1':'a'}
# print a,b,c,d,e,f,h,i

# str = "abc\rdef"
# print str
# print "%d" % 45 == '45'
# print "%i" % 34 == '34'
# print "%o" % 1000 == '1750'
# print "%u" % -1000 == "-1000"
# print "%x" % 1000 == '3e8'
# print "%X" % 1000 == '3E8'
# print "%e" % 1000 == '1.000000e+03'
# print "%E" % 1000 == '1.000000E+03'
# print "%f" % 10.34 == '10.340000'
# print "%F" % 10.34 == '10.340000'
# print "%g" % 10.34 == '10.34'
# print "%G" % 10.34 == '10.34'
# print "%c" % 34 == '"'
# print "%r" % int == "<type 'int'>"
# print "%s there" % 'hi' == 'hi there'
# print "%g%%" % 10.34 == '10.34%'

# print 1 + 2 == 3
# print 3 - 2 == 1
# print 3 * 2 == 6
# print 2 ** 3 == 8
# print 2 / 4.0 == 0.5
# print 2 // 4.0 == 0.0
# print 1 % 3 == 1
# print 3 < 5
# print 4 > 1
# print 2 <= 2
# print 3 >= 3
# print 4 == 4
# print 2 != 4
# print 2 <> 5
# print len('hi') == 2
# print [1,2,3]
# print {'x':5}
# print range(1,5)
def fun(f):
    print "func"
    f()

@fun
def abc():
    print "abc"
