#可以输出字符串
print("hello world")

#含有运算符的表达式
print(3+1)

#将数据输出到文件中，注意点，1，所指定的盘符存在 2，使用file=fp
fp=open('D:/text.txt','a+')#如果文件不存在就创建，存在就在文件内容后面追加 a+的含义
print('hello world',file=fp)
fp.close()

#不进行换行输出（输出内容在在一行中）
print('hello','world','Python')