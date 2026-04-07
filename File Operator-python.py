import os
from datetime import datetime as d


class journalmanager:
    def __init__(self,filename="C://Users//MAYUR MAKVANA//OneDrive//Desktop//files//journal.txt"):
        self.fn = filename

    def add_entry(self):
        print("-*-"*30)
        entry=input("Enter your journal entry: ")
        print("-*-" * 30)
        time=d.now().strftime("[%Y-%m-%d %H:%M:%S]")
        try:
            with open(self.fn,"a") as file:
                file.write(f"{time}\n{entry}\n\n")
            print("Entry added to journal file")
        except Exception as e:
            print("-*-" * 30)
            print(f"error:-{e}")
            print("-*-" * 30)

    def view_entry(self):
        try:
            with open(self.fn,"r") as file:
                entry=file.read()
                if entry.strip() == "":
                    print("-*-" * 30)
                    print("Entry is empty")
                    print("-*-" * 30)
                else:
                    print("-*-" * 30)
                    print("Your Enteries......")
                    print("-*-" * 30)
                    print(entry)

        except FileNotFoundError as e:
            print(f"error:-{e}")

    def search_entry(self):
        print("-*-" * 30)
        kword=input("Enter your keyword to search: ")
        print("-*-" * 30)
        try:
            with open(self.fn,"r") as file:
                c=file.read()
                entry=c.strip().split("\n\n")
                found=0
                # print(entry)
                for i in entry:
                    if kword.lower() in i.lower():
                        print(i)
                        found = 1

                if found==0:
                    print("-*-" * 30)
                    print("File have not keyword like you Enter....")
                    print("-*-" * 30)
        except FileNotFoundError as e:
            print(f"error:-{e}")
    def delete_entry(self):
        while True:
            confirm = input("Do you want to delete the entry? y/n: ")
            if confirm == "y":
                try:
                    os.remove(self.fn)
                    print("-*-" * 30)
                    print("Entry deleted from journal file")
                    print("-*-" * 30)
                except FileNotFoundError as e:
                    print("-*-" * 30)
                    print(f"error:-{e}")
                    print("-*-" * 30)
                break
            elif confirm == "n":
                print("-*-" * 30)
                print("Deletion aborted ")
                print("-*-" * 30)
                break
            else:
                print("-*-" * 30)
                print("Enter the valid option")
                print("-*-" * 30)


j=journalmanager()
while True:
    try:
        print("-*-" * 30)
        print("Welcome to Personal Journal Manager")
        print("Select an option:")
        print("1. Add a new entry")
        print("2. View all entry")
        print("3. Search for an entry")
        print("4. Delete all entry")
        print("5. Exit")
        ch=int(input("Enter your choice: "))
        if ch==1:
            j.add_entry()
        elif ch==2:
            j.view_entry()
        elif ch==3:
            j.search_entry()
        elif ch==4:
            j.delete_entry()
        elif ch==5:
            print("-*-" * 30)
            print("Thank you for using this program")
            print("-*-" * 30)
            break
        else:
            print("-*-" * 30)
            print("Invalid choice")
            print("-*-" * 30)
    except ValueError as e:
        print(f"error:-{e}")