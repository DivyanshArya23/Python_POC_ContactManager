#created on 3 June 2015;8:34:50 PM
#by Divyansh Arya
import string
 
print "*"*10,"CONTACT MANAGER","*"*10
print "~"*10,"\n1.Create Contacts\n2.View Contacts"
a=1
while a==1:
    print "\n","~"*10
    choice=input("Enter Your Choice:")
    print "-"*10
    if choice==2:                   #Viewing Contacts 
        f=open('Contacts.txt','r')
        content=f.read()
        print "\n",content,"\n"
    elif choice==1:                 #Creating Contact
        print "To Quit Leave Any of The Field Blank\n","*"*10
        n=1
        while n>0:
            print "CONTACT",n 
            fname=raw_input("Enter First Name:")
            fname=str.capitalize(fname)
            if fname=='':
                break
            lname=raw_input("Enter Last Name:")
            lname=str.capitalize(lname)
            if lname=='':
                break
                print "CREATING CONTACTS ENDED\n","*"*10
            mob=input("Enter Contact Number:")
            mob=str(mob)
            info='\n\n'+'--x--'*7+'\n'+'NAME:'+fname+' '+lname+'\nCONTACT No.'+mob
            f=open('Contacts.txt','r')
            content=f.read()
            f=open('Contacts.txt','w')
            f.write(content+info)
            f.close()
            print "*"*10,"\n"
            n+=1
