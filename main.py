from authentication import signup,login
from customer import withdraw,deposit,check_Bal,request
from Adminmenu import search_customer,search_admin,fetchUsers,delete_customer,viewReqs
print("1.signup")
print("2.login")
print("3.Exit")

choose=input("choose above options:----")
if choose == "1": 
    signup()
elif choose == "2": 
    abc=login()
    user_id,user_name,user_pswd,user_role=abc
    if user_role=="customer":
        print("---customer menu----")
        print("1.withdraw")
        print("2.deposit")
        print("3.check_balance")
        print("4.(request(atm/loan/checkbook:--))")
        chooseopt=int(input("enter option here:--"))
        if chooseopt==1:
            withdraw(user_id)
        if chooseopt == 2:
            deposit(user_id)
        if chooseopt == 3:
            check_Bal(user_id)   

        if chooseopt  == 4:
            request(user_id)  
    if user_role =="admin":
       


        while True:
            print("--------admin features----------") 
            print("1.search for customer")
            print("2.search for admin")
            print("3.fetch all users")
            print("4.delete  customer")
            print("5.view requests for customer")

            choose =int(input("enter yr option here :----    "))
            if choose == 1:
                search_customer()
            elif choose ==2:
                search_admin()  
            elif choose == 3:
                fetchUsers()   
            elif choose == 4:
                delete_customer()  
            else:
                viewReqs()      
            
  