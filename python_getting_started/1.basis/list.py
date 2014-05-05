#encoding:utf-8

classmates = ['zhangsan','lisi','wangwu']
print classmates
print len(classmates)

print classmates[0]
print classmates[1]
print classmates[2]
#print classmates[3] # error

#print classmates(len(classmates)-1) # error
print classmates[len(classmates)-1] 

print classmates[-1]
print classmates[-2]
print classmates[-3]

#list是一个可变的有序表，所以，可以往list中追加元素到末尾：
classmates.append('jinba')
print classmates

#可以把元素插入到指定的位置，比如索引号为1的位置
classmates.insert(1,'qian7')
print classmates

#要删除list末尾的元素，用pop()方法
del_element = classmates.pop()
print del_element
#要删除指定位置的元素，用pop(i)方法，其中i是索引位置
del_ind = classmates.pop(1)
print del_ind
print classmates

#要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
classmates[1] = 'sun8'
print classmates

#list里面的元素的数据类型也可以不同
typesList = ['123',True,1]
print typesList

#list元素也可以是另一个list
langList = ['python','java',['jsp','asp'],'scheme'] #可以看成是一个二维数组
print langList
print len(langList)
print langList[2]
print langList[2][1]


#如果一个list中一个元素也没有，就是一个空的list，它的长度为0
nullList = []
print len(nullList)
