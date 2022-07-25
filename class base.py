class empoloyee:
   def __init__(self,name,fname,email):
       self.name = name
       self.fname = fname
       self.email = email



em1 = empoloyee("ali","abbai","m@gmail.com")

print(em1.name)

class cat :
   def __init__(self , name , color, sex):
       self.name = name
       self.color = color
       self.sex = sex



cat1 = cat("snowy","white","male")
cat2 = cat("tiny","brown","male")

print(cat1.name ,"\n",cat2.sex)