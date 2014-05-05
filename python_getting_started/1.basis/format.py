# format 
#vim set:fileencoding=utf-8 #或者#encoding:utf-8

a = 'hello %s ' % 'world'
print a

b = 'Hi, %s, you have $%d.' % ('Michael',10000)
print b

print '%2d~%02d \n' % (3,1) 

print '%.2f' % 3.1415926

print 'Age: %s. Gender %s' % (23, True)

print u'Hi, %s' % u'Michael'

print 'growth rate: %d %%' % 7 #输出%，需要转义，用%%来表示一个%
