# # -*- coding: utf-8 -*-
# # @Author: Zymous
# # @Date:   2017-04-28 10:41:44
# # @Last Modified by:   Zymous
# # @Last Modified time: 2017-04-28 11:06:28
# # Inheritance Versus Composition

# class Parent(object):

#     def implicit(self):
#         print "PARENT implicit()"

#     def override(self):
#         print "PARENT override()"

#     def altered(self):
#         print "PARENT altered()"

# class Child(Parent):
#     # override override function
#     def override(self):
#         print "CHILD override()"
#     # override altered function and call the parent altered function
#     def altered(self):
#         print "CHILD, BEFORE PARENT altered()"
#         super(Child, self).altered()
#         print "CHILD, AFTER PARENT altered()"

# dad = Parent()
# son = Child()

# dad.altered()
# son.altered()
class Other(object):

    def override(self):
        print "OTHER override()"


    def implicit(self):
        print "OTHER implicit()"

    def altered(self):
        print "OTHER altered"

class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE OTHER altered()"
        self.other.altered()
        print "CHILD, AFTER OTHER altered()"

son = Child()
son.implicit()
son.override()
son.altered()