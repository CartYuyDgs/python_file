class Tool(object):#类对象
        #类属性
        num = 0
        #方法
        def __init__(self,name):
                self.name = name#实例属性
                Tool.num+=1

tool1 = Tool('ABC')#实例对象
tool2 = Tool('BCD')
tool3 = Tool('DEF')
print(Tool.num)
print(tool3.num)
#实例属性和具体某个实例对象有关系
#实例对象之间不能共享实例属性
#类属性属于类对象
#实例对象共享类对象
