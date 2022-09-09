#single level inheritance
class mani:
    def nani(self,name,age,):
        self.name = name
        self.age = age
        print("NAME    : ", name)
        print("AGE     : ", age )
class babu(mani):
    def mani1(self,rolln0,branch):
        self.rolln0 = rolln0
        self.branch = branch
        print("ROLL N0 : ",rolln0)
        print("BRANCH  : ",branch)
    def run(self):
        print("studing in riet college.....")
obj=babu()
obj.nani("manikanta babu",26)
obj.mani1(302,"mech")
obj.run()
# multi level inheritance
