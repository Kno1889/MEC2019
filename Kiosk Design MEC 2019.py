from Restuarants import *
from Students import *

# displays menu and selection options for the 
# restuarant Creation X
def creationX():
    orderlst = []
    total = 0
    print(glblRests.lst[0].menu)
    
    select = 0
    while(select == 0):
        selection = input("Select the order that you want excatly how its spelled: ")
        if(selection not in glblRests.lst[0].menu):
            print("Type it again correctly")
        else:
            orderlst.append(selection)
            total += glblRests.lst[0].menu[selection]
            
            print("Successfully added: ", selection)
            print("With a total price of: ", total)
            select = int(input("Would you like to add anything? If yes, press 0, if not press 1"))
    print("Your Order is: ", orderlst)
    print("Your total is: ", total)
            
# displays menu and selection options for the 
# restuarant Eggcetera
def eggcetra():
    orderlst = []
    total = 0
    print(glblRests.lst[1].menu)
    
    select = 0
    while(select == 0):
        selection = input("Select the order that you want excatly how its spelled: ")
        if(selection not in glblRests.lst[1].menu):
            print("Type it again correctly")
        else:
            orderlst.append(selection)
            total += glblRests.lst[1].menu[selection]
            
            print("Successfully added: ", selection)
            print("With a total price of: ", total)
            select = int(input("Would you like to add anything? If yes, press 0, if not press 1"))
    print("Your Order is: ", orderlst)
    print("Your total is: ", total)
    
# displays menu and selection options for the 
# restuarant Global Delights
def globDel():
    orderlst = []
    total = 0
    print(glblRests.lst[2].menu)
    
    select = 0
    while(select == 0):
        selection = input("Select the order that you want excatly how its spelled: ")
        if(selection not in glblRests.lst[2].menu):
            print("Type it again correctly")
        else:
            orderlst.append(selection)
            total += glblRests.lst[2].menu[selection]
            
            print("Successfully added: ", selection)
            print("With a total price of: ", total)
            select = int(input("Would you like to add anything? If yes, press 0, if not press 1"))
    print("Your Order is: ", orderlst)
    print("Your total is: ", total)

# displays menu and selection options for the 
# restuarant HammerTown
def hamTown():
    orderlst = []
    total = 0
    print(glblRests.lst[3].menu)
    
    select = 0
    while(select == 0):
        selection = input("Select the order that you want excatly how its spelled: ")
        if(selection not in glblRests.lst[3].menu):
            print("Type it again correctly")
        else:
            orderlst.append(selection)
            total += glblRests.lst[3].menu[selection]
            
            print("Successfully added: ", selection)
            print("With a total price of: ", total)
            select = int(input("Would you like to add anything? If yes, press 0, if not press 1"))
    print("Your Order is: ", orderlst)
    print("Your total is: ", total)

# displays menu and selection options for the 
# restuarant Pizza Pizza   
def pizzaPizza():
    orderlst = []
    total = 0
    print(glblRests.lst[4].menu)
    
    select = 0
    while(select == 0):
        selection = input("Select the order that you want excatly how its spelled: ")
        if(selection not in glblRests.lst[4].menu):
            print("Type it again correctly")
        else:
            orderlst.append(selection)
            total += glblRests.lst[4].menu[selection]
            
            print("Successfully added: ", selection)
            print("With a total price of: ", total)
            select = int(input("Would you like to add anything? If yes, press 0, if not press 1"))
    print("Your Order is: ", orderlst)
    print("Your total is: ", total)

# displays menu and selection options for the 
# misc items sold at La Piazza
def otherStuff():
    orderlst = []
    total = 0
    print(glblRests.lst[5].menu)
    
    select = 0
    while(select == 0):
        selection = input("Select the order that you want excatly how its spelled: ")
        if(selection not in glblRests.lst[5].menu):
            print("Type it again correctly")
        else:
            orderlst.append(selection)
            total += glblRests.lst[5].menu[selection]
            
            print("Successfully added: ", selection)
            print("With a total price of: ", total)
            select = int(input("Would you like to add anything? If yes, press 0, if not press 1"))
    print("Your Order is: ", orderlst)
    print("Your total is: ", total)
    
# displays restuarants avaliable to choose from
def restMenu():
    restSelection = input("Pick the Restaurant you would like to order from\n 1. CreationX\n 2. Eggcetra\n 3. Global Delights\n 4. HammerTown\n 5. PizzaPizza\n 6. Other\n Press -99 to exit")
    if(restSelection == '-99'):
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
 
# displays main homescreen of the application
def main():
    selection = 0
    print("Welcome to La Piazza\n")
    while(selection == 0):
        stdNum = input("Please enter your student number. If you do not have a student number press 0      ")
        if(stdNum == '0'):
            restMenu()
        #else:
        
main()
    

