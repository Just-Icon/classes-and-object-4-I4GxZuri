from unicodedata import name


class Student:
    # [assignment] Skeleton class. Add your code here

    def __init__(self, name="", age=int(), tracks=[''], score=float()):

        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self, name):
        print(f"New Student: {self.name}")
    
    def change_age(self, age):
        print(f"Age: {self.age}")

    def add_track(self, tracks):
        print(f"Learning Track: {self.tracks}")

    def get_score(self, score):
        score = print(f"Score: {self.score}")
        return score

        pass


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.name = "Peter"
Bob.change_name("Peter")
Bob.age = 34
Bob.change_age(34)
Bob.tracks = "UI/UX"
Bob.add_track("UI/UX")
Bob.score = 20.9
Bob.get_score(20.9)
