
class Unit:
    def __init__(self, name: str, code: str, length_weeks: int = 13, credit_points: int = 6):
        self.name: str = name
        self.code: str = code.lower()
        self.length_weeks: str = length_weeks
        self.credit_points: int = credit_points

    def get_name(self) -> str:
        return self.name

    def get_code(self) -> str:
        return self.code
    
    def get_length_weeks(self) -> int:
        return self.length_weeks

    def get_credit_points(self) -> int:
        return self.credit_points

    def __str__(self) -> str:
        return f"{self.code}: {self.name}"

    def __repr__(self) -> str:
        return f"{self.code}: {self.name}, {self.length_weeks}, {self.credit_points}"

class Student:
    def __init__(self, name: str, SID: str, units: list[Unit]):
        # Check name
        if name == "":
            raise ValueError("Cannot have an empty name")
        # Set name
        self.name: float = name
        
        # Calculate total credit points
        self.total_credit_points = 0
        for unit in units:
            self.total_credit_points += unit.get_credit_points()

        # Check credit points
        if self.total_credit_points < 18 or self.total_credit_points > 32:
            raise ValueError(f"{self.name}'{'s' if self.name[-1] != 's' else ''} units are wrong. They're doing {self.total_credit_points} many credits")
        
        # Turn units into a dictionary of (unit, mark) pairs, mark is originally 0
        self.units: dict[Unit, float] = {}
        for unit in units:
            self.units[unit] = 0
    
    def get_unit_from_code(self, unit_code: str) -> Unit:
        for unit in self.units.keys():
            if unit.get_code() == unit_code:
                return unit
        return None

    def get_name(self) -> str:
        return self.name
    
    def get_units(self) -> dict[Unit, float]:
        return self.units
    
    def add_mark(self, unit_code: str, unit_mark_percent: float, weighting: float):
        unit_to_add_mark_too: Unit = self.get_unit_from_code(unit_code)
        if unit_to_add_mark_too is None:
            raise ValueError(f"{unit_code} is not a unit done by this student")
        
        self.units[unit_to_add_mark_too] += unit_mark_percent * weighting

        epsilon: float = 1E-5
        for unit, mark in self.units.items():
            if mark > 1 + epsilon:
                raise ValueError("Mark cannot exceed 100% in {unit}")
    
    def average_mark(self) -> float:
        student_average_mark: float = 0
        # This if statement is so we don't divide by zero
        if len(self.get_units()) != 0:
            for unit, mark in self.get_units().items():
                student_average_mark += mark * unit.get_credit_points()
            student_average_mark /= self.total_credit_points
        return student_average_mark
    
    def __str__(self) -> str:
        output = f"{self.name} is doing the following units with the following marks:"
        for unit, mark in self.units.items():
            output += f"\n\t{unit}: {mark}"
        return output
    
    def __repr__(self) -> str:
        return f"{self.name}: {self.total_credit_points} - {self.units.keys()}"
        
class Cohort:
    def __init__(self, students: list[Student] = []):
        self.students: list[Student] = students
        self.best_student: Student = None
        self.worst_student: Student = None
        self.most_popular_unit: Unit = None
        self.no_failing: int = 0
        self.update_stats()
    
    def get_best_student(self) -> Student:
        return self.best_student
    
    def get_worst_student(self) -> Student:
        return self.worst_student
    
    def get_most_popular_unit(self) -> Unit:
        return self.most_popular_unit
    
    def get_no_students_failing(self) -> int:
        return self.no_failing

    def update_stats(self):
        self.update_outlier_students()
        self.update_popular_unit()
        self.update_failing_students()
    
    def update_outlier_students(self):
        # Define where things will be stored
        max_average_student: Student = None
        max_average: float = 0.00

        min_average_student: Student = None
        min_average: float = 1.00

        # Iterate through students and keep track of max and min
        for student in self.students:
            # Find average mark
            student_average_mark = student.average_mark()
            
            # Update if neccessary
            if student_average_mark > max_average:
                max_average_student: Student = student
                max_average: float = student_average_mark
            if student_average_mark < min_average and student_average_mark != 0:
                min_average_student: Student = student
                min_average: float = student_average_mark
        
        self.best_student = max_average_student
        self.worst_student = min_average_student
    
    def update_popular_unit(self):
        unit_frequency: dict[Unit, int] = {}

        # Fill table with frequency data
        for student in self.students:
            for unit in student.get_units().keys():
                if unit in unit_frequency.keys():
                    unit_frequency[unit] += 1
                else:
                    unit_frequency[unit] = 1

        # Determine max popularity unit from dictionary
        most_popular_unit: Unit = None
        no_students_in_popular_unit: int = 0
        for unit, no_students in unit_frequency.items():
            if no_students > no_students_in_popular_unit:
                no_students_in_popular_unit = no_students
                most_popular_unit = unit
        
        self.most_popular_unit = most_popular_unit
    
    def update_failing_students(self):
        self.no_failing = 0
        # Iterate through students
        for student in self.students:
            # Check condition and update
            if student.average_mark() < .5:
                self.no_failing += 1


def main():
    engg1810: Unit = Unit("Introduction to Engineering Computing", "engg1810")
    comp2022: Unit = Unit("Models of Computation", "comp2022")
    math2923: Unit = Unit("Analysis (Advanced)", "math2923")
    math3968: Unit = Unit("Differential Geometry (Advanced)", "math3968")
    scdl3991: Unit = Unit("Science Dalyell Individual Project", "scdl3991")

    nicholas: Student = Student("Nicholas Bertollo", "123456789", [engg1810, comp2022, math2923, math3968, scdl3991])
    daniel: Student = Student("Daniel Friedrich", "798234789", [engg1810, scdl3991, math3968, comp2022])
    atif: Student = Student("Muhammad Atif Iqbal", "092523631", [math3968, comp2022, math2923, engg1810])
    michael: Student = Student("Vincent Zhu", "092465234", [scdl3991, engg1810, math2923])

    nicholas.add_mark("engg1810", 1.0, 1.0)
    nicholas.add_mark("comp2022", 1.0, 1.0)
    nicholas.add_mark("math3968", 1.0, 1.0)
    nicholas.add_mark("scdl3991", 1.0, 1.0)

    atif.add_mark("engg1810", 1.0, 0.7)
    michael.add_mark("math2923", 0.71, 1.0)
    daniel.add_mark("comp2022", 0.22, 1.0)
    daniel.add_mark("math3968", 0.7, 0.73)    

    tutor_cohort: Cohort = Cohort([nicholas, daniel, atif, michael])
    print(f"{tutor_cohort.get_best_student()}")
    print(f"{tutor_cohort.get_worst_student()}")
    print(f"{tutor_cohort.get_most_popular_unit() = }")
    print(f"{tutor_cohort.get_no_students_failing() = }")

if __name__ == "__main__":
    main()