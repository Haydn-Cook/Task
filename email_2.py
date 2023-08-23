### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.
class Email(object):
    
    # Initialise class variables for emails.
    def __init__ (self , email_address , subject_line , email_contents):
         self.email_address = email_address
         self.subject_line = subject_line
         self.email_contents = email_contents
    
    
 
    # Initialise instance variables for emails
         self.has_been_read = False
         self.is_spam = False

    
    
    # Method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):
        self.has_been_read = True
    
    # Method to change 'is_spam' emails from False to True.
    def mark_as_spam(self):
        self.is_spam = True
    

# --- Lists --- #
# Initialise empty lists to store the email objects.
Inbox = []
Outbox = []

# --- Functions --- #
# Create and build out the required functions for your program.

def populate_inbox():
    
    # Create 3 sample emails and add it to the inbox list.
    email_1 = Email("john11@gmail.com" , "This is a test email hope it works" , "If you are getting this email then the test is succesful welldone bro!")
    email_2 = Email("Bro123@gmail.com" , "Yo bro" , "Yo bro hope that you are getting this email!")
    email_3 = Email("GigaBro@giga.com" , "Giaga email" , "Giga bro here with the giga email")
    Inbox.extend([email_1, email_2, email_3])

def send_email():

    # Create an email to 'send'/add to the outbox list.
    sent_email_1 = Email("KimCook99@gmail.com" , "Hello There" , "Hello there")
    Outbox.extend(sent_email_1)

def list_emails():

    # Create a function which prints the email’s subject_line, along with a corresponding number.

    email_number = 0
    for e in Inbox:
        email_number += 1
        print(f"{email_number}: {e.subject_line}")


def read_email():

    # Create a function which displays a selected email and then sets its has_been_read instance variable to True.
   
    number_1 = 0
    number = 0
    for a in Inbox:
        if a.has_been_read == False:
            number_1 += 1
            print(f"""Email Index {number_1} : {a.subject_line}""")
        
    email_index = int(input("Please provide the index number of the email you would like to read: "))
    for e in Inbox:
            if e.has_been_read == False:
                number += 1
                print(email_index)
                if number == email_index:
                    print(f"""{number}: 
                    {e.email_address}
                    {e.subject_line}
                    {e.email_contents}""")
                    e.mark_as_read()
                    break
    else:
        print("There is no emial under the given interger: ")


def mark_spam():
    number = 0
    number_1 = 0
    for a in Inbox:
        number_1 += 1
        if a.is_spam == False:
            print(f"Email {number_1} - {a.email_address}: {a.subject_line}  ")
    spam_index = int(input("Which email index would you like to mark as spam?: "))
    for e in Inbox:
        number += 1
        if number == spam_index:
            e.mark_as_spam()
        else:
            print("There is no email under this index.")
        
    # Create a function which sets the selected email's mark_as_spam instance variable to True.

def delete_email():
    number_1 = 0
    for a in Inbox:
        number_1 += 1  
        print(f"Email {number_1} - {a.email_address}: {a.subject_line}")  
    delete_index = int(input("Which email index would you like to delete?: "))
    number = 0
    for e in Inbox:
        number += 1
        if number == delete_index:
            print(f"emial number: {number}")
            print(f"{e.subject_line}")
            Inbox.pop(number-1)
    
    # Create a function which deletes an email from the inbox.

# --- Email Program --- #
populate_inbox()

# Populate the inbox with 3 sample emails for use in your program

# Fill in the logic for the various menu operations.
menu = True

while True:
    user_choice = int(input('''\nWould you like to:

    Choose a number based on the action you would like to perform:
    eg: If you want to read a email type 1 and follow further instructions.                                               

    1. Read an email
    2. Mark an email as spam
    3. Delete an email
    4. View unread emails
    5. View spam emails
    6. Send an email
    7. Quit application

    Enter selection: '''))
       
    # Read an email
    if user_choice == 1:
        # add logic here
        read_email()
        
    # Mark an email as spam
    elif user_choice == 2:
        # add logic here
        mark_spam()

    # Delete an email
    elif user_choice == 3:
        # add logic here
        delete_email()
    
    # View unread emails
    elif user_choice == 4:
        # add logic here
        number = 0
        for e in Inbox:
            number += 1
            if e.has_been_read == False:
                print(f" {number} - {e.email_address}: {e.subject_line}")
            
    # View spam emails
    elif user_choice == 5:
        # add logic here
        for e in Inbox:
            if e.is_spam == True:
                print(f"{e.email_address}: {e.subject_line}")
            else:
                print("There is no  more spam emails to view: ")
                break
    # Send an email
    elif user_choice == 6:
        # add logic here
        send_email()

    # Quit appplication
    elif user_choice == 7:
        # add logic here
        break

    else:
        print("Oops - incorrect input.")