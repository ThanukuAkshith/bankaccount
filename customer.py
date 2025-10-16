from db_connection import get_connection

connect_db=get_connection()
cur=connect_db.cursor()
def withdraw(user_iddd):
    amt=float(input("enetr amount to draw :---"))
    cur.execute("update accounts set account_balance=account_balance-%s where user_id =%s",(amt,user_iddd))
    connect_db.commit()
    print("amount withdrawn successfully....")
    

def deposit(user_iddd):
    amt=float(input("enetr amount to deposit :---"))
    cur.execute("update accounts set account_balance=account_balance+%s where user_id =%s",(amt,user_iddd))
    cur.execute("select * from accounts where user_id=%s",(user_iddd,))
    person=cur.fetchone()
    account_id,user_id,acc_type,bal=person
    connect_db.commit()

    print(f"{amt} credited to yr accrount successfully... and total bal :-- ",bal)
    


def check_Bal(user_iddd):
    cur.execute("select * from accounts where user_id=%s",(user_iddd,))
    person=cur.fetchone()
    account_id,user_id,acc_type,bal=person
    connect_db.commit()

    print(f"yr main bal {bal}")

def request(user_iddd):
    print("1)loan .. 2)atm_card.. 3)checkbook")
    ch=int(input("pick yr option in 1, 2, 3 :---- enter value "))
    if ch == 1:
        req_type="loan"
        amt=float(input("enter loan quoting amount :-- "))
    elif ch == 2:
        req_type="atm_card"
        amt=0
    elif ch == 3:
        req_type="checkbook"
        amt=0
    else:
        print("invalid req")
        return   
    cur.execute("insert into requests (user_id,req_type,req_amount) values (%s,%s,%s)",(user_iddd,req_type,amt))   
    connect_db.commit()

    print("req raised successfully....")  