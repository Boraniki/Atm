from Atm_project_admin import *

from Atm_project_client import *

control_client = Process_of_client()

control_admin = Process_of_admin()

print("""   ************************ 
                    
                   WELCOME TO Boran's Atm 
                   
                   
                1.Administration Access
            
            
                2.Customer Access
            
                    FOR QUIT PRESS 'Q'
                    
                    
            ************************        """)

while True:
    operation1 = input("Choose willing access :")

    if(operation1 == "q"):

        print("We want to see you again...")
        break

    elif(operation1 == "1"):
        print("Enter ")
        admin_no = int(input("No :"))
        admin_password = int(input("Password :"))

        true_password1 = control_admin.admin_enter(admin_no)

        if(admin_password == true_password1):
            print("WELCOME OLD FRIEND ")
            print(""" *******************
            
            
                        Choose what you want
                        1.Adding Customer
                        2.Deleting Customer
                        3.Searching Customer
                        
                        PRESS 'Q' FOR QUİT
                        
                        *******************
                        """)
            while True:
                operation3 = input("Willing option :")

                if(operation3 == "q"):
                    break
                elif(operation3 == "1"):

                    customer_name = input("Name :")
                    customer_surname = input("Surname :")
                    customer_password = int(input("Password :"))
                    customer_no = int(input("No :"))
                    new_customer = Client(customer_name,customer_surname,customer_no,customer_password,0)
                    control_admin.adding_client(new_customer)
                    print("New customer added")

                    

                elif(operation3 == "2"):

                    deleted_customer = input("Write customer no")

                    sure = input("ARE YOU SURE ? YES/NO")

                    if(sure == "yes"):
                        control_admin.deleting_client(deleted_customer)

                    else:
                        print("YOUR CHOICE")
                elif(operation3 == "3"):
                    customer_name = input("Write searching customer name :")
                    control_admin.searching_client(customer_name)

                else:
                    print("PLEAS SELECT CORRECT NUMBER")

        else :
            print("Wrong password pls try again")

    elif(operation1 == "2"):

        print("Enter ")
        client_no = int(input("No :"))
        client_password = int(input("Password :"))

        true_password2 = control_admin.client_enter(client_no)
        if (client_password == true_password2):
            print("WELCOME OLD FRIEND DO WHAT YOU WANT,BUT PAY BACK")
            print(""" *******************


                                    Choose what you want my dear
                                    1.Imbursing
                                    2.Withderaw
                                    3.Balance inquiry

                                    PRESS 'Q' FOR QUİT

                                    *******************
                                    """)

            while True:
                operation2 = input("SELECT OPTION :")
                if(operation2 == "q"):
                    print("WE WANT TO SEE YOU AGAIN")
                    break
                elif(operation2 == "1"):
                    amount = int(input("Input money amount :"))
                    control_client.imbursing(client_no,amount)
                    control_client.balance_inquiry(client_no)
                elif(operation2 == "2"):
                    withdrawing_amount = int(input("Input willing amount of money :"))
                    control_client.withdrawing(client_no,withdrawing_amount)
                    control_client.balance_inquiry(client_no)
                elif(operation2 == "3"):
                    control_client.balance_inquiry(client_no)
                else:
                    print("PLEAS SELECT CORRECT NUMBER")

        else:
            print("Wrong password please try again")

    else :
        print("You enter, please try again")





















