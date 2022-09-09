class manikanta:
    def __init__(self,name,age,):
        self.name = name
        self.age = age
    def run(self):
        print("running")
    def walk(self):
        print("walking")
obj=manikanta("bandreddy",26)
print("NAME : ", obj.name,)
print("AGE : ", obj.age)
obj.run()
obj.walk()
obj1=manikanta("babu",26)
print("NAME : ", obj1.name,)
print("AGE : ", obj1.age)
obj.run()
obj.walk()