from db_connection import get_connection
dbc=get_connection()
cur=dbc.cursor()
def search_customer():
    user_Name=input("enter customer name:---")
    user_role=input("enter user role")
    cur.execute("select * from user where user_name =%s and user_role=%s",(user_Name,user_role))
    customerData=cur.fetchone()
    print(customerData,"c   data")    


def search_admin():
    user_Name=input("enter customer name:---")
    user_role=input("enter user role")
    cur.execute("select * from user where user_name =%s and user_role=%s",(user_Name,user_role))
    customerData=cur.fetchone()
    print(customerData,"cdata")
    

def fetchUsers():
    cur.execeute ("select * from user ")
    customerData=cur.fetchall()
    print(customerData,"cdata")

def delete_Customer():
    user_Name=input("enter username you want to delete:----")
    cur.execute("select * from user where user_Name =%s",(user_Name,))
    user_id=cur.fetchone()[0]
    
    cur.execute("delete from user where user_id=%s,"(user_id,))
    dbc.commit()
    cur.execute ("delete  from accounts where user_id=%s",(user_id,))
    cur.execute ("delete  from requests where user_id=%s",(user_id,))
    cur.execute("delete from customers where user_id=%s,"(user_id,))
    dbc.commit()
    print("customer deleted successfully:-----")
    

def viewReqs():
    option=input("choose: 1) loan  2) atm_card 3) checkbook:----")
    if option=="1":
        cur.execute("""
        select user.user_name,accounts.account_balance,requests.req_type,requests.req_amount
        from user
        left join accounts 
        using (user_id)
        left join requests
        using (user_id)
        where requests.req_type = %s
        """,("loan",))
        reqData=cur.fetchall()
        for i in reqData:
            # print(i)
            user_name,user_main_bal,user_req_type,user_quoteamt=i
            print(f"{user_name},,{int(user_main_bal)},{user_req_type},{int(user_quoteamt)}")
        
    elif option=="2":
        cur.execute ("select * from  requests where req_type =%s",("atm_card",))
        reqData=cur.fetchall()
        print(reqData,"rdata")
    elif option=="3":
        cur.execute ("select * from  requests where req_type =%s",("checkbook",))
        reqData=cur.fetchall()
        print(reqData,"rdata")
    else:
        return "inavid"
        
   