class Dog:

        def __test1(self):
                print("*"*10+"正在发送短信..."+"*"*10)
        def send_msg(self,money):
                if money<100000:
                        print("****余额不足****")
                else:
                        self.__test1()
dog = Dog()
dog.send_msg(1000000)
dog.send_msg(100)
