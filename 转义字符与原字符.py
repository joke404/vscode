#转义字符
print('hello\nworld')#\ +转义功能的首字母 n--->newline的首字母表示换行

#\t占4个字符格子，占一个制表位，四个一组
print('hello\tworld')
print('hellooo\tworld')
print('hello\rworld')#\r是覆盖
print('hello\bworld')#\b是退格


#\是转义功能

print("http:\\www.baidu.com")

print('http:\\\\wwww.baidu.com')
#输出过程中遇到两个斜线最终会以一个斜线进行输出

#输出结果中想要包含单引号就这么写，表示单引号不是输出的边界，而是字符串要输出的内容
print('老师说：\'大家好\'')

#原字符，不希望字符串中的转义字符起作用，就使用原字符，就是在字符串之前加上r，或者R
print(r'hello\nworld')
#注意事项，最后一个字符不能是反斜杠
print(r'hello\nworld\\')
#但是可以是两个反斜杠航，因为会抵消