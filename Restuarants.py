# class Restuarant denotes a single restuarant located within La Piazza
class Restuarant:
    # constructor for an instance of Restuarant
    def __init__(self, name):
        # an instance of restuarant has fields denoting the restuarant name (string) and a menu (dictionary)
        # the constructor initializes an instance with a name and an empty menu
        self.name = name
        self.menu = {}

    # method of Restuarant that allows for updating of menu items of the restuarants
    def add_to_menu(self, item, price):
        # updates/appends items to the meny of the restuarant instance
        self.menu[item] = price

# class Restuarants denotes the list of Restuarant objects which
# in turn denotes the restuarants located in La Piazza
# having this class allows the addition/updating of restuarants in
# La Piazza
class Restuarants:
    # constructor for the list of restuarants
    def __init__(self, lstRest):
        self.lst = lstRest

    # method of Restuarants that allows for the updating/adding of restuarants into 
    # the list of restuarants in La Piazza
    def add_to(self, rest):
        self.lst.append(rest)

'''
- The below are simply the initlization of the restuarants
- in La Piazza. Along with there current menu items with the
- corresponding prices.
'''
# initlizing the Restuarants instance
glblRests = Restuarants([])

# initliazing Creation X restuarant instance of the Restuarant class
# with the corresponding menu
rest1 = Restuarant("Creation X")
rest1.add_to_menu("Chicken Strips",7.29)
rest1.add_to_menu("Traditional Poutine",6.95)
rest1.add_to_menu("Butter Chicken Poutine",7.95)
rest1.add_to_menu("Pulled Pork Poutine",8.75)
rest1.add_to_menu("Steak N' Eggs",11.75)
rest1.add_to_menu("Perogies",5.95)
rest1.add_to_menu("Popcorn Shrimp Dinner",10.95)
rest1.add_to_menu("Curly Fries",5.25)
rest1.add_to_menu("Regular Fries",2.99)
rest1.add_to_menu("Baked Potato",3.40)
rest1.add_to_menu("Southwest Wrap (chicken/Beef)",7.55)
rest1.add_to_menu("Falafel & Hummus Wrap",6.99)
rest1.add_to_menu("Kale Chicken Caesar Wrap",7.50)
rest1.add_to_menu("Popcorn Shrimp Wrap",8.65)
rest1.add_to_menu("Buffalo Chicken Wrap",8.25)
rest1.add_to_menu("Steak Sandwich",8.45)
rest1.add_to_menu("Texas Grilled Cheese (with bacon, ham, or tomato)",4.25)
rest1.add_to_menu("Pulled Port Hoagie",8.95)
rest1.add_to_menu("Tabasco Buffalo Chicken Sanwich",8.25)
rest1.add_to_menu("Texas B.L.T",4.30)

# adds the Creation X instance into Restuarants
glblRests.add_to(rest1)

# initliazing Eggcetera restuarant instance of the Restuarant class
# with the corresponding menu
rest2 = Restuarant("Eggcetera")
rest2.add_to_menu("the hungry marauder",8.99)
rest2.add_to_menu("the slam dunk",5.95)
rest2.add_to_menu("build a waffle",6.75)
rest2.add_to_menu("homestyle panacakes",4.25)
rest2.add_to_menu("chipotle steak & egss wrap",7.95)
rest2.add_to_menu("toasted western",4.25)
rest2.add_to_menu("three egg omelette on a wrap",5.99)
rest2.add_to_menu("three egg omelette with toast",4.99)
rest2.add_to_menu("two eggs & toast with protein",4.15)
rest2.add_to_menu("hashbrown",1.25)

# adds the Eggcetera instance into Restuarants
glblRests.add_to(rest2)

# initliazing Global Delights restuarant instance of the Restuarant class
# with the corresponding menu
rest3 = Restuarant("Global Delights")
rest3.add_to_menu("Fried Chicken Meal",10.99)
rest3.add_to_menu("2 Piece Chicken",6.99)
rest3.add_to_menu("3 Piece Chicken",7.99)
rest3.add_to_menu("Mac N' Cheese Meal",6.99)
rest3.add_to_menu("Cajun Pollock",8.99)
rest3.add_to_menu("Corn Cobettes",1.99)
rest3.add_to_menu("Malibu Vegtables",2.99)
rest3.add_to_menu("New Potatoes",1.99)
rest3.add_to_menu("Smashed Potatoes",2.99)
rest3.add_to_menu("Mac N' Cheese Side",4.99)
rest3.add_to_menu("Garlic Stick",1.00)
rest3.add_to_menu("Jerk Chicken Meal",10.99)
rest3.add_to_menu("3 Piece Chicken",7.99)
rest3.add_to_menu("2 Piece Chicken",6.99)
rest3.add_to_menu("Curried Roti",9.99)
rest3.add_to_menu("Jamaican Fish Rundown",9.99)
rest3.add_to_menu("Rice & Beans",2.99)
rest3.add_to_menu("Teriyaki Chicken",10.99)
rest3.add_to_menu("Sweet & Sour Chicken",10.99)
rest3.add_to_menu("Vegetable Fried Rice",9.99)
rest3.add_to_menu("Stir-Fried Begetables",9.99)
rest3.add_to_menu("Vegtable Spring Rools",2.25)
rest3.add_to_menu("Chowmein Noddles",3.99)
rest3.add_to_menu("Stir-Fried Rice",2.99)
rest3.add_to_menu("Chicken Quesadilla",10.99)
rest3.add_to_menu("Veggie & Mushroom Quesadilla",10.99)
rest3.add_to_menu("Beef Chimichanga Meal",10.99)
rest3.add_to_menu("Tex-Mex Rice",2.99)
rest3.add_to_menu("Refired Beans",1.99)
rest3.add_to_menu("Black Beans",0.99)
rest3.add_to_menu("Chicken Parmesan",10.99)
rest3.add_to_menu("Beef Lasagna",10.99)
rest3.add_to_menu("Vegetable Lasgna",10.99)
rest3.add_to_menu("Seafood Pasta",8.99)
rest3.add_to_menu("Cheese Tortellini",8.99)

# adds the Global Delights instance into Restuarants
glblRests.add_to(rest3)

# initliazing HammerTown restuarant instance of the Restuarant class
# with the corresponding menu
rest4 = Restuarant("HammerTown")
rest4.add_to_menu("Big Breakfast Crunch",6.45)
rest4.add_to_menu("Egg Mac",3.15)
rest4.add_to_menu("Ham N' Egg Croissant",4.99)
rest4.add_to_menu("Breakfast Bagel",4.99)
rest4.add_to_menu("The Reuben",9.00)
rest4.add_to_menu("Roast Beef Sanwich",8.55)
rest4.add_to_menu("Turkey Bacon Club",7.25)
rest4.add_to_menu("Grilled Beggie Sanwich",9.00)
rest4.add_to_menu("Tuna Melt",6.25)
rest4.add_to_menu("Pho Beef Deep",7.50)
rest4.add_to_menu("Pesto Chicken",7.50)
rest4.add_to_menu("Curried Vegetable Roti",6.00)
rest4.add_to_menu("The Al Capone",8.95)
rest4.add_to_menu("Ultimate Ham N' Cheese",5.75)
rest4.add_to_menu("Turkey Havarti",6.00)

# adds the HammerTown instance into Restuarants
glblRests.add_to(rest4)

# initliazing Pizza Pizza restuarant instance of the Restuarant class
# with the corresponding menu
rest5 = Restuarant("Pizza Pizza")
rest5.add_to_menu("Cheese Slice",5.49)
rest5.add_to_menu("Pepporni Slice",6.49)
rest5.add_to_menu("Veggie Slice",6.49)

# adds the Pizza Pizza instance into Restuarants
glblRests.add_to(rest5)

# initliazing misc items sold in La Pizza as an instance of the Restuarant class
# with the corresponding menu
rest6 = Restuarant("Other")
rest6.add_to_menu("Bag of Chips",1.99)
rest6.add_to_menu("Piece of Fruit",2.99)
rest6.add_to_menu("Pastry",3.99)
rest6.add_to_menu("Drink",3.99)

# adds the misc instance into Restuarants
glblRests.add_to(rest6)
