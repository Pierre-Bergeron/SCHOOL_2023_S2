# Main document

# Class for employee details


class Employee_List(object):
    def __init__(self, employee_id):
        self._employee = [None] * employee_id

    def __setitem__(self, employee_number, data):
        self._employee[employee_number] = data

    def __getitem__(self, employee_number):
        return self._employee[employee_number]


employees_all = Employee_List(10)  # Create 10 employee
employees_all[0] = 'Pierre.Bergeron'
employees_all[1] = 'Simon.Dubosq'
employees_all[2] = 'Regis.Godin'
employees_all[3] = 'Samuel.Baril'
employees_all[4] = 'Olivier.Girouard'
employees_all[5] = 'Nicola.Girouard'
employees_all[6] = 'FirstN.LastN'
employees_all[7] = 'Hello.World'
employees_all[8] = 'Pablo.Megan'
employees_all[9] = 'Soupe.Friday'
print(employees_all[2])

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
