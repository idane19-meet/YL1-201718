class person(object):
    def __init__(self,name,age,city,gender,breakfast):
        self.name = name
        self.age = age
        self.city = city
        self.gender = gender
        self.breakfast = breakfast
    def breakfast2(self,bf):
        print(self.name + " is eating his favorite breakfast! it is: " + bf)
    def sports(self,sp):
        print(self.name + " favorties sport is: " + sp)
        
        
i = person("idan",15,"adi","male","cornflakes")
i.breakfast2("cornflakes")
i.sports("basketball")
