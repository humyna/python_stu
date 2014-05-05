#encoding:utf-8

#第一种:for...in循环
names = ['zhangsan','lisi','wangwu']
#for (name in  names) # error
for name in names:
    print name

#Python提供一个range()函数，可以生成一个整数序列，比如range(5)生成的序列是从0开始不大于5的整数[0,1,2,3,4]
#计算1-100的整数之和
sum = 0
for x in range(101):
    sum = sum + x
print sum

#第二种:while循环
#计算100以内所有奇数之和
sum = 0
n =99
while n > 0: # 千万不要忘记这个冒号
    sum = sum + n
    n = n - 2
print sum

#infinite loop u  can enter 'ctrl+c'
while(1):
    print 'infinite loop'
