# Logan H's Employee Records Program

# 1) DEFINE the Employee class with name, ID number, department, and job title
class Employee:
    # Constructor method to initialize all attributes
    def __init__(self, name, id_number, department, job_title):
        self.name = name                  # Employee name
        self.id_number = id_number        # Employee ID number
        self.department = department      # Employee department
        self.job_title = job_title        # Employee job title

    # Method to display employee info
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"ID Number: {self.id_number}")
        print(f"Department: {self.department}")
        print(f"Job Title: {self.job_title}")
        print("-----------------------------")

# 2) CREATE three Employee objects with the provided data
employee1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
employee2 = Employee("Mark Jones", 39119, "IT", "Programmer")
employee3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")

# 3) DISPLAY each employee's information using display_info method
print("Employee Records:\n")
employee1.display_info()
employee2.display_info()
employee3.display_info()
