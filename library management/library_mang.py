from mq_sql_library import *  # your MySQL setup (mydb, my_cursor, sqlformula)
from library_file import get_book  # function that fetches book info
import bcrypt
from tabulate import tabulate
import re
import webbrowser

class Book:

    def __init__(self):
        self.query = None
        self.title = None
        self.author = None
        self.year = None
        self.edition_count = None
        self.ebook_access = None
        self.email = None
        self.password = None
        self.user = None
        self.passw = None
        self.first_name = None
        self.last_name = None
        self.phone_no = None
        self.link = None
        self.work = None
        self.real_password = None
        self.salt = bcrypt.gensalt()
        self.harsh_password = None
        self.customer_id = None
        self.my_books = []
        self.move = None
        self.reset_psw = None

    def fresh_ui(self):
        new = [
            ['Welcome to our Library service'],
            ['ENTER 1:➕ To Create Account'],
            ['ENTER 2:👤 To login'],
            ['ENTER 3:♻️ Forgotten password']
        ]
        print(tabulate(new))
        while True:
            self.move = input("enter here: ")
            if self.move == "1":
                self.create_account()
            elif self.move == "2":
                self.login()
            elif self.move == "3":
                self.password_reset()
            else:
                print("INVALID INPUT")

    def dashboard(self):
        data = [
            ['Welcome to our Library Service '],
            ['ENTER 1: ➕ Get New Book'],
            ['ENTER 2: 👤 Register New Member'],
            ['ENTER 3: 🔍 Search / Borrow / Return Book'],
            ['ENTER 4: 📅 View Borrowing History'],
            ['ENTER 5: 🧾 Generate Reports'],
            ['ENTER 0: 🧾 Main Menu']
        ]
        print(tabulate(data))
        while True:
            self.move = input("enter here: ")
            self.pointer()

    def get_my_book(self):
        self.query = input("ENTER YOUR DESIRED BOOK: ")
        self.title, self.author, self.year, self.edition_count, self.ebook_access, self.link, self.work = get_book(self.query)
        self.book = (self.title, 100, self.author, self.year, self.edition_count, self.ebook_access,self.link)
        if self.ebook_access == "borrowable" or "public_domain" or "full_access":
            self.adding_to_database()
            self.show_book()
        else:
             print("This book it not available")

    def show_book(self):
        if self.link != None:
            print(f"TO GET YOUR BOOK, CLICK HERE: https://openlibrary.org{self.work}")
            webbrowser.open(f"https://openlibrary.org/links/{self.link}")
            #if work_key else "N/A"
            # print(f"https://openlibrary.org/books/{self.link}") #if lending_edition else "N/A"
        else:
            print('SOMETHING WENT WRONG')

    def adding_to_database(self):
        my_cursor.execute('SELECT title FROM books WHERE title = %s',(self.title,))
        temp_book = my_cursor.fetchone()
        if temp_book == None:
            my_cursor.execute(sqlformula, self.book)
            mydb.commit()
            print(f"✅ '{self.title}' has been successfully added to the database!")
        else:
            print("already in the system")

    def create_account(self):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        self.first_name = input('ENTER YOUR FIRST NAME: ')
        self.last_name = input('ENTER YOUR LAST NAME: ')
        self.phone_no = input('ENTER YOUR PHONE NUMBER: ')
        self.user = input('ENTER YOUR EMAIL HERE : ')
        if re.match(pattern,self.user) is not None:
            self.passw = input('ENTER YOUR PASSWORD HERE : ')
            if len(self.passw) <= 8 :
                print("password have to be greater than or equal to 8 characters")
            else:
                self.harsh_password = bcrypt.hashpw(self.passw.encode("utf-8"), self.salt)
                self.new_details = (self.user, self.harsh_password)
                self.customers = (self.first_name, self.last_name, self.phone_no, self.user)
                my_cursor.execute(sqlformula_1,self.new_details)
                my_cursor.execute(sqlformular_3,self.customers)
                mydb.commit()
                print('Account Created Successfully ✅')

    def login_authentication(self):
        my_cursor.execute("SELECT passwords FROM the_library_logins WHERE customer_id = %s", (self.customer_id,))
        stored_data = my_cursor.fetchone()

        if not stored_data:
            print("❌ Password not found. Please create an account.")
            return

        stored_hash = stored_data[0].encode("utf-8")

        if bcrypt.checkpw(self.harsh_password, stored_hash):
            print("✅ Login Successful! Welcome back.")
        else:
            print("❌ Incorrect password. Try again.")


    def login(self):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        self.email = input('Enter your email here: ')
        if re.match(pattern, self.email) is not None:
            self.password = input('Enter your password here: ')
            self.harsh_password = self.password.encode("utf-8")
            my_cursor.execute("SELECT usernames, customer_id FROM the_library_logins WHERE usernames = %s", (self.email,))
            stored_data = my_cursor.fetchall()
            self.customer_id = stored_data[0][1]
            if not stored_data:
                print("❌ Email not found. Please create an account.")
        return self.login_authentication()

    def password_reset(self):
        self.email = input('Enter your email here: ')
        my_cursor.execute("SELECT usernames FROM the_library_logins WHERE usernames = %s", (self.email,))
        result = my_cursor.fetchall()
        if result != None:
            self.reset_psw=input("Enter your new password: ")
            self.harsh_password = bcrypt.hashpw(self.reset_psw.encode("utf-8"), self.salt)
            my_cursor.execute(
                "UPDATE the_library_logins SET passwords = %s WHERE usernames = %s",
                (self.harsh_password, self.email)
            )
            mydb.commit()

        else:
            print("YOU DO NOT HAVE AN ACCOUNT WITH US")

    def show_all_books(self):
        headers = ['SERIAL NUMBER','NAME','QUANTITY','AUTHOR','YEAR','EDITION COUNT','AVAILABILITY','LINK']
        my_cursor.execute("SELECT * FROM books ")
        result = my_cursor.fetchall()
        for i in result :
            self.my_books.append(i)
        print(tabulate(self.my_books, headers= headers, tablefmt="fancy_grid"))
    def pointer(self):
        if self.move == "1":
            self.get_my_book()
        elif self.move == "2":
            self.create_account()
        elif self.move == "3":
            self.get_my_book()
        elif self.move == "4":
            self.show_book()
        elif self.move == "5":
            pass
        elif self.move == "6":
            self.dashboard()
        else :
            print("INVALID INPUT ❌")

    def menu(self):
        print('Navigation panel : \n'
              'ENTER 1 TO CREATE AN ACCOUNT \n'
              'ENTER 2 TO LOGIN IN \n')
        temp = input('ENTER YOUR ANSWER HERE : ')
        if temp == '1' :
            print('THANKS FOR CHOOSING USE \n'
              'ENTER YOUR DETAILS HERE 🔽')
            self.create_account()
        elif temp == '2':
            self.login()
        else :
            print('BYE👋🙋‍♂️')




m_1 = Book()
# m_1.fresh_ui()
# m_1.dashboard()
# m_1.password_reset()
# m_1.create_account()
# m_1.login()
# m_1.login_verification()
m_1.get_my_book()
# m_1.menu()
# m_1.show_all_books()













