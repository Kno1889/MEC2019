from Restuarants import *
from Students import *

def creationX():
    print(glblRests.lst[0].menu)

def restMenu():
    restSelection = input("Pick the Restaurant you would like to order from\n 1. CreationX\n 2. Eggcetra\n 3. Global Delights\n 4. HammerTown\n 5. PizzaPizza\n 6. Other\n Press exit to exit: ")
    if(restSelection == 'exit'):
        print("\n")
        main()
    elif (restSelection == '1'):
        creationX()
    elif (restSelection == '2'):
        eggcetra()
    elif (restSelection == '3'):
        globDel()
    elif (restSelection == '4'):
        hamTown()
    elif (restSelection == '5'):
        pizzaPizza()
    elif (restSelection == '6'):
        otherStuff()
    else:
        print("Invalid Response")
        restMenu()
        
def main():
    selection = 0
    print("Welcome to La Piazza\n")
    while(selection == 0):
        stdNum = input("Please enter your student number. If you do not have a student number press 0      ")
        if(stdNum == '0'):
            restMenu()
        elif(stdNum == 'exit'):
            break
        #else:
        
main()
    

