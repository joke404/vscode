#组成
#标识：表示对象所存储的内存地址，使用内置函数id（obj）来获取
#类型：表示的是对象的数据类型，使用内置函数type（obj）来获取
#值：表示对象所存储的具体数据，使用print（obj可以）可以将值进行打印输出
name='玛利亚'
print('标识',id(name))
print('类型',type(name))
print('值',name)