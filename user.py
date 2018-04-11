class User(object):
    """docstring for User"""
    def __init__(self, name=None, mo_no=None, add=None, email=None):
        super(User, self).__init__()
        self.name = name
        self.mo_no = mo_no
        self.add = add
        self.email=email

    def __str__(self):
        return "\nName : " + self.name+\
               "\nAdd  : " + str(self.add)+\
               "\nMo No: "+ str(self.mo_no)+\
               "\nEmail: "+ str(self.email)

    def display(self):
        print "Name : ", self.name
        print "Add  : ", self.mo_no
        print "Mo No: ", self.add
        print "Email:",self.email
