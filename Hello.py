class hello1:
    @staticmethod
    def say_hello():
        print("say Hello")

    def greet(self):
        self.say_hello()

class Hello2(hello1):
    @staticmethod
    def say_hello():
        print("Say Salam'")


Hello1 = hello1()
hello2 = Hello2()

Hello1.greet()
hello2.greet()







