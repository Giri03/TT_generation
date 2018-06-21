class course:
    # pass #to escape empty class errors.
    def __init__(self, name, no_students, instructor = [] ):#constructor
        self.name = name
        self.no_students = no_students
        self.instructor = instructor
