
class Person():

    def __int__(self,name,email,password):
        self.name = name,
        self.email = email
        self.password = password

    def save(self):
        with open('test.txt', 'w', encoding='utf-8') as file:
            x = file.write(self.name + self.email + self.password)
            file.close()
