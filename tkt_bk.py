class TICKET_BOOK (object):
    """docstring for User"""
    def __init__(self, Class=None, bdg_pt=None, quota=None):
        super(TICKET_BOOK, self).__init__()
        self.Class = Class
        self.bdg_pt = bdg_pt
        self.quota=quota

    def __str__(self):
        return "============================="+\
               "\nClass : " + self.Class+\
               "\nbdg_pt: "+ str(self.bdg_pt)+\
               "\nquota : "+ str(self.quota)+\
               "\n============================="+\
               " "

    def display(self):
        print "============================="
        print " CLASS       : ",self.Class
        print " BOARDING PT.: ",self.bdg_pt
        print " QUOTA       : ",self.quota
        print "============================="
        print " "
