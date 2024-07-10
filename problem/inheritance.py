# in opps inheritance cospect 

class men:
    name = 'abhishek'
    age = 24
    mobile_no = 8273814047
    address = "nagla jhamman line par tundla(frizobad) 283204"

    
    
class work(men):
    domain = "backend developer"
    experience = "1 year"


    def get_info(self):
        print (f"hi i am {self.name} and i am working as {self.domain} ")

information = work()
information.get_info()
print(information.name,information.age,information.domain)

    