#encoding:utf-8

#要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：

L = [ x * x for x in range(10)]
print L

g = (x * x for x in range(10))

for n in g:
    print n

#著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到:1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易

def fab(max):
    n, a, b = 0, 0 ,1
    while n < max:
	print b
	a, b =b, a+b
	n = n + 1
print fab(6)


#函数和generator仅一步之遥。要把fab函数变成generator，只需要把print b改为yield b就可以了
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
	yield b
	a, b = b, a+b
	n = n + 1
print fab(6)

#generator和函数的执行流程不一样——函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。


def odd():
    print 'step 1'
    yield 1
    print 'step 3'
    yield 3
    print 'step 5'
    yield 5

o = odd()
print o.next()
print o.next()
print o.next()
#print o.next() #error

#把函数改成generator后，我们基本上从来不会用next()来调用它，而是直接使用for循环来迭代


#===================总结========================
#generator的工作原理，它是在for循环的过程中不断计算出下一个元素，并在适当的条件结束for循环。对于函数改成的generator来说，遇到return语句或者执行到函数体最后一行语句，就是结束generator的指令，for循环随之结束。

