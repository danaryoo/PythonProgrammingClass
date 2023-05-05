#2 classes: A, B
#class A can only see function 1 and 2, class B can see 3 and 4

class A:
    def one(self):
        print('1')
    def two(self):
        print('2')

class B:
    def three(self):
        print('3')
    def four(self):
        print('4')

#only sees objects in A
a1 = A()
a1.one()
a1.two()

#only sees objects in B
b1 = B()
b1.three()
b1.four()

b1.one()
b1.two()
b1.three()
b1.four()
