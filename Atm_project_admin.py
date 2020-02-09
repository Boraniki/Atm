import sqlite3
from Atm_project_client import *

class Admin ():
    def __init__(self,name,surname,no,password):
        self.name = name
        self.surname = surname
        self.no = no
        self.password = password


    def __str__(self):
        return "Name :{}\nSurname :{}\nAdmin No :{}\n".format(self.name, self.surname,self.no)


class Process_of_admin():
    def __init__(self):
        self.connection()


    def connection(self):
        self.connect = sqlite3.connect("Atm_project.db")
        self.cursor = self.connect.cursor()
        request = "Create table if not exists admin (Name TEXT,Surname TEXT,No INT,Password INT)"
        self.cursor.execute(request)
        self.connect.commit()


    def adding_client(self,client):
        request = "INSERT INTO client VALUES (?,?,?,?,?)"
        self.cursor.execute(request,(client.name,client.surname,client.no,client.password,client.balance))
        self.connect.commit()

    def deleting_client(self,no):
        request = "Delete From client Where No = ?"
        self.cursor.execute(request,(no,))
        self.connect.commit()


    def searching_client(self,name):
        request =  "SELECT * FROM client where Name = ?"
        self.cursor.execute(request,(name,))
        info = self.cursor.fetchall()
        for i in info:
            if(len(info) == 0):
                print("There is no client with that name")
            else :
                client = Client(i[0],i[1],i[2],i[3],i[4])
                return print(client)


    def admin_enter(self,no):
        request = "Select * From admin Where No = ?"
        self.cursor.execute(request,(no,))
        person = self.cursor.fetchall()
        for i in person:
            if (len(person) == 0):
                print("Wrong password or account number please, try again")
            else :
                return i[3]


    def client_enter(self,no):
        request = "Select * From client Where No = ?"
        self.cursor.execute(request,(no,))
        person = self.cursor.fetchall()
        for i in person:
            if (len(person) == 0):
                print("Wrong password or account number please, try again")
            else :
                return i[3]























