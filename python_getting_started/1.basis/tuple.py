#encoding:utf-8

#tuple和list非常类似，但是tuple一旦初始化就不能修改
classmates = ('zhangsan','lisi','wangwu')
print classmates[0],classmates[1],classmates[-1] 


#不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。

#tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
t = (1,2)
print t

#如果要定义一个空的tuple，可以写成()
t = ()
print ()

#只有1个元素的tuple定义时必须加一个逗号,，来消除(1)歧义
#Python在显示只有1个元素的tuple时，也会加一个逗号,，以免你误解成数学计算意义上的括号
t = (1,)
print t


#"可变的"tuple
#tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。
t = ('a','b',['A','B'])
print t[2][0]

t[2][0] = 'C'
print t
