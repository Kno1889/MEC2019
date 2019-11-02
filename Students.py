# class Student that denotes a student at McMaster
class Student(object): 
    # constructor for class Student 
    def __init__(self, name, num):
        # initlizes an instance of the class with a student name (string),
        # a students number (int), a student's saved favorites (list) as empty, 
        # and a student's last order from La Piazza (list) as empty
        self.name = name
        self.num = num
        self.fav = []
        self.last = []
    
    # a method of the class Student that allows the updating/adding
    # of items into a student's favorite saved orders
    def setFav(self, favs):
        self.fav = favs
        
    # a method of the class Student that allows the updating/adding
    # of items into a student's last order
    def setLast(self, lasTime):
        self.last = lasTime

# class Students that denotes a list of instance of the class Student
# which in turn denotes students at McMaster
class Students:
    # constructor to initlize the list of students
    def __init__(self, lstStd):
        self.lst = lstRest

    # a method that appends a Student instance into
    # this instance of Students (updates the list of students)
    def add_to(self, std):
        self.lst.append(rest)

