class Animals :
    def __init__(self , name , age , sex , **kwargs):

        self.name = name
        self.age = age
        self.sex = sex 
class Cat (Animals):
    def __init__(self, name, age, sex, breed , color , **kwargs):
        super().__init__(name, age, sex, **kwargs)
        self.color = color
        self.breed = breed
         
cat1 = Cat("lee",2,"male","persian","white")
print(cat1.name)
print(cat1.age)
print(cat1.sex)
print(cat1.breed)
