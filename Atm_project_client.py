import sqlite3

class Client():


    def __init__(self, Name, Surname, No, Password, Balance ):
        self.Name = Name
        self.Surname = Surname
        self.No = No
        self.Password = Password
        self.Balance = Balance

    def __str__(self):
        return "Name :{}\nSurname :{}\nClient No :{}\nCurrent Remainder : {}\n".format(self.Name, self.Surname,self.No,self.Balance)


class Process_of_client():


    def __init__(self):
        self.connection()

    def connection(self):
        self.connect = sqlite3.connect("Atm_project.db")
        self.cursor = self.connect.cursor()
        request = "Create table if not exists client (Name TEXT,Surname TEXT,No INT,Password INT,Balance INT)"
        self.cursor.execute(request)
        self.connect.commit()

    def imbursing(self,no,amount):
        request1 = "Select * from client where No = ?"
        self.cursor.execute(request1,(no,))
        data = self.cursor.fetchall()
        for i in data:
            balance = i[4]
            new_balance = balance + amount
            request2 = "Update client set Balance = ? where No = ?"
            self.cursor.execute(request2,(new_balance,no))
            self.connect.commit()

    def withdrawing(self,no,amount):
        request1 = "Select * from client where no = ?"
        self.cursor.execute(request1,(no,))
        data = self.cursor.fetchall()
        for i in data:
            balance = i[4]
            current_balance = balance - amount
            if (current_balance < 0):
                print("There is no enough money in your account...")
            else:
                request2 = "Update client set Balance = ? where no = ?"
                self.cursor.execute(request2,(current_balance,no))
                self.connect.commit()



    def balance_inquiry(self,no):
        request = "SELECT * from client where no = ?"
        self.cursor.execute(request,(no,))
        data = self.cursor.fetchall()
        for i in data:
            print("Current balance :",i[4])
































