# -*- coding: utf-8 -*-
import pickle
from user import User
from tkt_bk import TICKET_BOOK
import qrcode
from random import *
from pathlib import Path

class Train_Ticket():

    Admin_list = []
    Cust_list = []
    Tc_list = []
    ticket_list = []
    loc_list=[]
    pnr=[]

    def __init__(self, user = None, tkt_bk = None ): 
        if isinstance(user, User) and isinstance(tkt_bk, TICKET_BOOK):
            Train_Ticket.user_list.append(user)
            Train_Ticket.ticket_list.append(tkt_bk)

    def Admin_SignUp(self):
        print'+-----------------------+'
        print'   ENTER USER DETAILS    '
        print'+-----------------------+'

        name=raw_input("Enter your Name      : ")
        mo_no=raw_input("Enter your Phone no. : ")
        add=raw_input("Enter your Address   : ")
        email=raw_input("Enter your Email     : ")
        print''
        newkey=raw_input('Enter Username       : ')
        newvalue=raw_input('Enter Password       : ')
        admin[newkey]=newvalue

        Train_Ticket.Admin_list.append(User(name, add,mo_no,email))
        pickle_out = open("AdminInfoList.pickle","wb")
        pickle.dump(Train_Ticket.Admin_list, pickle_out)
        pickle_out.close()
        
        pickle_out = open("Admindict.pickle","wb")
        pickle.dump(admin, pickle_out)
        pickle_out.close()

    def Cust_SignUp(self):
        print'+-----------------------+'
        print'   ENTER USER DETAILS    '
        print'+-----------------------+'

        name=raw_input("Enter your Name      : ")
        mo_no=raw_input("Enter your Phone no. : ")
        add=raw_input("Enter your Address   : ")
        email=raw_input("Enter your Email     : ")
        print''
        newkey=raw_input('Enter Username       : ')
        newvalue=raw_input('Enter Password       : ')
        cust[newkey]=newvalue

        Train_Ticket.Cust_list.append(User(name, add,mo_no,email))
        pickle_out = open("CustInfoList.pickle","wb")
        pickle.dump(Train_Ticket.Cust_list, pickle_out)
        pickle_out.close()

        pickle_out = open("custdict.pickle","wb")
        pickle.dump(cust, pickle_out)
        pickle_out.close()

    def Tc_SignUp(self):
        print'+-----------------------+'
        print'   ENTER USER DETAILS    '
        print'+-----------------------+'
        name=raw_input("Enter your Name      : ")
        mo_no=raw_input("Enter your Phone no. : ")
        add=raw_input("Enter your Address   : ")
        email=raw_input("Enter your Email     : ")
        print''
        newkey=raw_input('Enter Username       : ')
        newvalue=raw_input('Enter Password       : ')
        tc[newkey]=newvalue

        Train_Ticket.Tc_list.append(User(name, add,mo_no,email))
        pickle_out = open("TcInfoList.pickle","wb")
        pickle.dump(Train_Ticket.Tc_list, pickle_out)
        pickle_out.close()

        pickle_out = open("tcdict.pickle","wb")
        pickle.dump(tc, pickle_out)
        pickle_out.close()
        

    def ADlogin(self):#ADMIN LOG IN
        my_file = Path("admindict.pickle")
        if my_file.is_file():#it will check whether file is exists or not 
            pickle_in = open("admindict.pickle","rb")
            admin = pickle.load(pickle_in)
            login_username=raw_input('Enter Username       : ')
            login_password=raw_input('Enter Username       : ')
            if admin.has_key(login_username):
                if admin[login_username]==login_password:
                    while True:
                        print'╔═[ADMIN]══════════════╗'
                        print" 1.Add new Location."
                        print" 2.Add new Route."
                        print" 3.Manage Route."
                        print" 0.Back."
                        print'╚══════════════════════╝'

                        choice=input('Enter Your Choice    : ')
                        
                        if choice==1:
                            print'+-----------------------+'
                            print"  CREATE NEW LOCATION    "
                            print'+-----------------------+'
                            #pickle_out = open("locations.pickle","wb")
                            #pickle.dump(Train_Ticket.loc_list, pickle_out)
                            #pickle_out.close()
                            loc=raw_input('Enter Your Choice    : ')
                            Train_Ticket.loc_list.append(loc)
                        elif choice==2:
                            #pickle_in = open("locations.pickle","rb")
                            #Train_Ticket.loc_list = pickle.load(pickle_in)
                            From=raw_input("Enter Source         : ")
                            to=raw_input("Enter Destination    : ")
                            if From in Train_Ticket.loc_list:
                                if to in Train_Ticket.loc_list:
                                    train[From]=to
                                    pickle_out = open("Route.pickle","wb")
                                    pickle.dump(train, pickle_out)
                                    pickle_out.close()
                                    print"Route is added!!!"
                                else:
                                    print'Invalid Destination!!!'
                            else:
                                print 'Invalid Source!!!'
                                
                                
                        elif choice==3:
                            print"Manage Route"
                            while True:
                                print'╔═[ADMIN]══════════════╗'
                                print" 1.Delete Route."
                                print" 2.Change Route."
                                print" 0.Back."
                                print'╚══════════════════════╝'
                                choice=input('Enter Your Choice    : ')

                                if choice==1:
                                    From=raw_input("Enter Source         : ")
                                    to=raw_input("Enter Destination    : ")
                                    if train.has_key(From):
                                        if train[From]==to:
                                            del train[From]
                                            print"Successfully Removed!!!!"
                                        else:
                                            print"Invalid Destination!!!"
                                    else:
                                        print"Invalid Source!!!"
                                elif choice==2:
                                    print'╔═[ADMIN]══════════════╗'
                                    print' 1.Update Source.'
                                    print' 2.Update Destination.'
                                    print' 0.Back.'
                                    print'╚══════════════════════╝'
                                    choice=input('Enter Your Choice    : ')

                                    if choice==1:
                                        From=raw_input("Enter Source         : ")
                                        to=raw_input("Enter Destination    : ")
                                        if train.has_key(From):
                                            if train[From]==to:
                                                new_key=raw_input('Enter New Source :')
                                                train[new_key] = myDict.pop(From)
                                                print"Successfully Update!!!!"
                                            else:
                                                print"Invalid Destination!!!"
                                        else:
                                            print"Invalid Source!!!"
                                        
                                    elif choice==2:
                                        From=raw_input("Enter Source         : ")
                                        to=raw_input("  Enter Destination    : ")
                                        
                                        if train.has_key(From):
                                            if train[From]==to:
                                                new_value=raw_input('Enter New Destination :')
                                                train[From] = new_value
                                                print"Successfully Update!!!!"
                                            else:
                                                print"Invalid Destination!!!"
                                        else:
                                            print"Invalid Source!!!"
                                    elif choice==0:
                                        break
                                    
                                elif choice==0:
                                    break
                        elif choice==0:
                            break
            else:
                print('Invalid username or password')
            
        else:
            print"Signup first!!!"
        

            
    def CUSlogin(self):#CUSTOMER LOG IN
        my_file = Path("custdict.pickle")
        if my_file.is_file():#it will check whether file is exists or not 
            pickle_in = open("custdict.pickle","rb")
            cust = pickle.load(pickle_in)
            login_username=raw_input('Enter Username       : ')
            login_password=raw_input('Enter Username       : ')
            if cust.has_key(login_username):
                if cust[login_username]==login_password:

                    while True:
                        print'╔═[CUSTOMER]═══════════╗'
                        print" 1.Book Ticket."
                        print" 2.View History."
                        print" 0.Back."
                        print'╚══════════════════════╝'

                        print''
                        choice=input('Enter Your Choice    : ')
                        print''
                    
                        if choice==1:
                            pickle_in = open("Route.pickle","rb")
                            train = pickle.load(pickle_in)
                            From=raw_input("Enter Source         : ")
                            to=raw_input("Enter Destination    : ")
                            if train.has_key(From):
                                if train[From]==to:
                                    print('Train is available for given route')
                                    t.ticket_book()
                                else:
                                    print('user entered the wrong input')
                            else:
                                print('train is not available for given route')
                            
                        elif choice==2:
                            print'+-----------------------+'
                            print"     RECENT HISTORY     "
                            print'+-----------------------+'
                            print t.ticket_list
                        elif choice==0:
                            break

            else:
                print('Invalid username or password')
        
        else:
            print"signup first!!!"
        
        

        
    def TClogin(self):#TICKET CHECKER LOG IN
        my_file = Path("tcdict.pickle")
        if my_file.is_file():#it will check whether file is exists or not 
            pickle_in = open("tcdict.pickle","rb")
            tc = pickle.load(pickle_in)
            login_username=raw_input('Enter Username       : ')
            login_password=raw_input('Enter Username       : ')
            if tc.has_key(login_username):
                if tc[login_username]==login_password:

                    while True:
                        print'╔═[TC]═════════════════╗'
                        print' 1.Check In Database.'
                        print' 0.Back.'
                        print'╚══════════════════════╝'

                        print''
                        choice=input('Enter Your Choice    : ')
                        print''

                        if choice==1:
                            print'+-----------------------+'
                            print'   CHECK IN DATABASE     '
                            print'+-----------------------+'
                            print''
                            pickle_in = open("pnr.pickle","rb")
                            Train_Ticket.pnr = pickle.load(pickle_in)
                            a=input('Enter PNR NO.        : ')
                            if a in Train_Ticket.pnr:
                                print'+-----------------------+'
                                print"      TICKET DETAILS     "
                                print'+-----------------------+'
                                pickle_in = open("ticket_list.pickle","rb")
                                Train_Ticket.ticket_list = pickle.load(pickle_in)
                                print Train_Ticket.ticket_list[0]
                            else:
                                print "Invalid PNR!!!"
                        elif choice==0:
                            break

            else:
                print('Invalid username or password')
            
        else:
            print"Signup first!!!"
        

        
    def ticket_book(self):
        print'+-----------------------+'
        print'   RESERVATION FORM      '
        print'+-----------------------+'
        Class=raw_input('Enter Class          : ')
        bdg_pt=raw_input('Enter Bording point  : ')
        quota=raw_input('Enter Quota          : ')
        
        Train_Ticket.ticket_list.append(TICKET_BOOK(Class, bdg_pt, quota))
        pickle_out = open("ticket_list.pickle","wb")
        pickle.dump(Train_Ticket.ticket_list, pickle_out)
        pickle_out.close()
        

        qr = qrcode.QRCode(
            version = 1,
            error_correction = qrcode.constants.ERROR_CORRECT_H,
            box_size = 10,
            border = 4,
        )
        x = randint(1000000000,10000000000)#random number
        Train_Ticket.pnr.append(x)
        pickle_out = open("pnr.pickle","wb")
        pickle.dump(Train_Ticket.pnr, pickle_out)
        pickle_out.close()
        # The data that you want to store
        data = ("PNR NO             :: "+str(x)+"\t\n"+"CLASS               :: "+Class+"\t\n"+"BOARDING PT :: "+bdg_pt+"\t\n"+"QUOTA              :: "+quota)
        # Add data
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image()
        # Create an image from the QR Code instance
        name_img=raw_input("Name the file        : ")#e.g. file.jpg
        img.save(name_img)

        

       
admin = {}
cust = {}
tc = {}
train = {}
t=Train_Ticket()

while True:
    
    print'╔═[Main Menu]══════════╗'
    print' 1.Admin Account.'
    print' 2.Customer Account.'
    print' 3.Ticket Checker.'
    print' 0.Exit.'
    print'╚══════════════════════╝'
    

    choice=input('Enter Your Choice    : ')
    print''
    
    if choice==1:
        while True:
            print'╔═[ADMIN]══════════════╗'
            print' 1.Log In.'
            print' 2.Sign up.'
            print' 0.Back.'
            print'╚══════════════════════╝'

            choice=input('Enter Your Choice    : ')
            print''
            if choice==1:
                t.ADlogin()
            elif choice==2:
                t.Admin_SignUp()
            elif choice==0:
                break
        
    elif choice==2:
        while True:
            print'╔═[CUSTOMER]═══════════╗'
            print' 1.Log In.'
            print' 2.Sign up.'
            print' 0.Back.'
            print'╚══════════════════════╝'

            choice=input('Enter Your Choice    : ')
            print''
            if choice==1:
                t.CUSlogin()
            elif choice==2:
                t.Cust_SignUp()
            elif choice==0:
                break
    
    elif choice==3:
        while True:
            print'╔═[TC]═════════════════╗'
            print' 1.Log In.'
            print' 2.Sign up.'
            print' 0.Back.'
            print'╚══════════════════════╝'

            choice=input('Enter Your Choice    : ')
            print''
            if choice==1:
                t.TClogin()
            elif choice==2:
                t.Tc_SignUp()
            elif choice==0:
                break

    elif choice==0:
        break

    
