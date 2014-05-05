# print string demo
# -*- coding: utf-8 -*-

print 'hello ,world!'
print "I'm ok!"
print 'i\'m \"ok\"!'

print '\\\n\\'

print '\\\t\\'
print r'\\\t\\'

print '''line1
line2
line3'''

print '中文' # 打印出来时乱码
print '中文'.decode('UTF-8')
