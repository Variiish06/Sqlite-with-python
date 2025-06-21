class table:
    def __init__(self):
        self.rows=[]

    def addrow(self,id,username,email):
        self.rows.append((id,username,email))

UserInput = input("db> ")
print(UserInput)

def insert_row(command_line, table1):
    words = command_line.strip().split()


    if UserInput.strip().startswith("insert"): #to add to a single row to the table
        if len(words) != 4:
            print("synatax error invalid numbers")
        else:
            id = words[1]
            username = words[2]
            email = words[3]
            table1.addrow(id,username,email)
    else:
        print("sytax error type again")



table1 = table()
print(table1.rows)

def main():

    def PrintPrompt():
         print("db>",end=" ")
         
    while(True):
         UserInput = input( )
         if UserInput.startswith("."):
            if UserInput.strip().lower() == ".exit":
               print("Exiting")
               break
            else:
               print("Umrecognised intput type again")
         elif UserInput.startswith("insert"):
             insert_row(UserInput,table1)
         else:
            print("Umrecognised input type again")

     
         

if __name__ == "__main__":

 main()    
