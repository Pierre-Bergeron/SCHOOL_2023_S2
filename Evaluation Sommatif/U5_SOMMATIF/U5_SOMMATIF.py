# Main document

# Class for employee details
class Employee_Information:

    def __init__(self, name, dob, empId):
        self.name = name
        self.dob = dob
        self.empId = empId

class Employee_List(object):
    def __init__(self, employee):
        self._employee = [None]
    def __setitem__(self, employee_number, data):
        self._employee[employee_number] = data
    def __getitem__(self, employee_number):
        return self._employee[employee_number]

    employees_all = Employee_List(10)  # Construct a building with 4 floors
    employees_all[0] = 'Pierre Bergeron'
    employees_all[1] = 'Simon Dubosq'
    employees_all[2] = 'Regis Godin'
    employees_all[3] = 'Samuel Baril'
    employees_all[4] = 'Olivier Girouard'
    employees_all[5] = 'Nicola Girouard'
    employees_all[6] = 'FirstN LastN'
    employees_all[7] = 'Hello World'
    employees_all[8] = 'Pablo Megan'
    employees_all[9] = 'Soupe Friday'
    print(employees_all[2])


def find(id_ref):

def pull(id_ref, id_sel):

def push(id_ref, id_sel, data_push):

strSelection = ''
while not (strSelection == "Q" or strSelection == "q"):
    print("""
  Menu
  ----
  1 - 
  2 - 
  3 - 
  4 -  
  5 - 
  6 - 
  Q - Quitter
  """)
    strSelection = input("Indiquer votre choix : ")

    if strSelection == "1":

    elif strSelection == "2":
        print()
    elif strSelection == "3":
        print()
    elif strSelection == "4":
        print()
    elif strSelection == "5":
        print()
    elif strSelection == "6":
        print()
print("Passé une belle journée.")
