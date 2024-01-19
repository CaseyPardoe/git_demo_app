#class Student:
#    def __init__(self, first, last, age, class_): 
#        self.first = first 
#        self.last = last 
#        self.age = age 
#        self.class_ = class_
#        self.scores = []
#    
#    def take_scores(self, score1, score2, score3):
#        self.scores = [score1, score2, score3]

#    def calc_score(self):
#        if not self.scores:
#            return "No scores available"
#        average_score = sum(self.scores) / len(self.scores)
#        return f"The average score for {self.first} is {average_score}"
        
            

#student1 = Student("john", "smith", 10, "maths")
#student2 = Student("katie", "smith", 12, "english")

#student1.take_scores (56, 60, 12)

#print(student1.calc_score())

#print(student1.__dict__)

class Bird:
    def __init__(self, name, wingspan):
        self.name = name
        self.wingspan = wingspan

    def make_sound(self):
        raise NotImplementedError("Subclasses must implement make_sound method.")

    def fly(self):
        print(f"{self.name} is flying with a wingspan of {self.wingspan} units.")

class Owl(Bird):
    def __init__(self, name, wingspan, nocturnal=True):
        super().__init__(name, wingspan)
        self.nocturnal = nocturnal

    def make_sound(self):
        return "Hoot, hoot!"

    def hunt(self):
        if self.nocturnal:
            print(f"{self.name} is hunting at night.")
        else:
            print(f"{self.name} hunts during the day.")

class Dodo(Bird):
    def __init__(self, name, wingspan, extinct=True):
        super().__init__(name, wingspan)
        self.extinct = extinct

    def make_sound(self):
        return "Squawk, squawk!"

    def display_status(self):
        if self.extinct:
            print(f"{self.name} is extinct.")
        else:
            print(f"{self.name} is not extinct.")


owl = Owl("Barn Owl", 75)
dodo = Dodo("Mauritius Dodo", 100)

owl.fly()
print(f"{owl.name} says: {owl.make_sound()}")
owl.hunt()

print("\n")

dodo.fly()
print(f"{dodo.name} says: {dodo.make_sound()}")
dodo.display_status()
