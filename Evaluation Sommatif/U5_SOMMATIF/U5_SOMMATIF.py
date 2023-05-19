# Main document

# Class for employee details


class Employee_List(object):
    def __init__(self, employee_id):
        self._employee = [None] * employee_id

    def __setitem__(self, employee_number, name):
        self._employee[employee_number] = name

    def __getitem__(self, employee_number):
        return self._employee[employee_number]



employees_all = Employee_List(10)  # Create 10 employee
employees_all[0] = 'Pierre Bergeron', '12121.00', '000-000-000'
employees_all[1] = 'Simon Dubosq', '10000.00', '000-000-000'
employees_all[2] = 'Regis Godin', '10000.00', '000-000-000'
employees_all[3] = 'Samuel Baril', '10000.00', '000-000-000'
employees_all[4] = 'Olivier Girouard', '10000.00', '000-000-000'
employees_all[5] = 'Nicola Girouard', '10000.00', '000-000-000'
employees_all[6] = 'FirstN LastN', '10000.00', '000-000-000'
employees_all[7] = 'Hello World', '10000.00', '000-000-000'
employees_all[8] = 'Pablo Megan', '10000.00', '000-000-000'
employees_all[9] = 'Soupe Friday', '10000.00', '000-000-000'

def set_emp_salerie(id, salerie):
    name = employees_all[id][0]
    employees_all[id] = name, salerie

def set_emp_social(id, ssn):
    name = employees_all[id][0]
    salerie = employees_all[id][1]
    employees_all[id] = name, salerie, ssn

def set_emp_name(id, name):
    salerie = employees_all[id][1]
    ssn = employees_all[id][2]
    employees_all[id] = name, salerie, ssn




print(employees_all[0])

# verification
set_emp_salerie(0, 10000)
print(employees_all[0][1])
# verification
set_emp_social(0, "100-200-300")
print(employees_all[0][2])
# verification
set_emp_name(0, "Pierre Bergy")
print(employees_all[0][0])

# def add_emp(name, dob, salerie, ssn):



strSelection = ''
while not (strSelection == "Q" or strSelection == "q"):
    print("""
  Menu
  ----
  1 - Ajouter un employé
  2 - Modifier un employé
  3 - Conjédier un employé
  4 - Afficher les dossier d'un employé
  5 - 
  6 - 
  Q - Quitter
  """)
    strSelection = input("Indiquer votre choix : ")

    if strSelection == "1":
        print()
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
