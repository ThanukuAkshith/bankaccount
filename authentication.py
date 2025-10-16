from db_connection import get_connection
conn=get_connection() 
cur=conn.cursor()
def signup():
    u_name=input("enetr user name :---  ")
    u_pswd=input("enetr user pswd :---  ")
    u_role=input("enetr user role (admin/customer) :---  ")
    cur.execute("insert into user(user_name,user_password,user_role) values (%s,%s,%s)",(u_name,u_pswd,u_role))
    conn.commit()
    print(f"{u_name} is registred as {u_role} successfully")
   


    cur.execute("select * from user where user_name=%s",(u_name,))
    data=cur.fetchone()
    print(data,"data")
    ac_type=input("enetr type of account (savings/current) :--- ")
    cur.execute("insert into accounts(user_id,account_type,account_balance) values (%s,%s,%s)",(data[0],ac_type,15000))
    print(f"account created  successfully to {u_name}")
    conn.commit()
    conn.close()

def login():
    while True:
        u_name=input("enter user name to login  :--- ")
        u_pswd=input("enetr pswd to login :- ------")
        cur.execute("select * from user where user_name =%s and user_password =%s",(u_name,u_pswd))
        data=cur.fetchone() 
        if data:
            return data
        else:
            print("no user found with that credentials. Try again.")
  