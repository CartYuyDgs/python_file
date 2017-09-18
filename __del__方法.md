class Dog:
        def __del__(self):
                print("*****OVER*****")

dog1 = Dog()
dog2 = dog1
del dog1
print("==============================")
del dog2
print("==============================")
~                                                                               
~                                                                               
~                                                                               
~              
