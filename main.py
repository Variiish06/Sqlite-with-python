def main():
    def PrintPrompt():
         print("db>",end=" ")
    while(True):
         UserInput = input("db> ")
         if UserInput.startswith("."):
            if UserInput.strip().lower() == ".exit":
               print("Exiting")
               break
            else:
               print("Umrecognised intput type again")
         else:
            print("Umrecognised input type again")
         

if __name__ == "__main__":

 main()    
