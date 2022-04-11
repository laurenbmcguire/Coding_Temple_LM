class Employee:
    all_ = []

    def __init__(self, first_name, last_name, email_address, department, active_status):
        # once a new employee is created, you can view your employees with "Employee.all"
        self.all_.append(self)
        self.first_name=first_name
        self.last_name=last_name
        self.email_address=email_address
        self.department=department
        self.active_status=active_status


    def __repr__(self):
        return f'<Employee: {self.email}>'

employee1 = Employee("John", "Smith","abc@gmail.com", "sales", "active") 
employee2 = Employee("Jill", "Jones", "def@gmail.com","sales", "active")
employee3 = Employee("Jane", "Bates", "ghi@gmail.com", "marketing", "active")
employee4 = Employee("Jack", "Miller", "jkl@gmail.com" ,"creative", "active")
employee5 = Employee("Jim", "Brown", "mno@gmail.com", "IT", "active")
employee6 = Employee("Jessica", "Hunter", "pqr@gmail.com", "IT", "inactive")
employee7 = Employee("Justin", "Dean", "stu@gmail.com", "sales", "active")
employee8 = Employee("Julie", "Ward", "vwx@gmail.com" ,"marketing", "active")
employee9 = Employee("James", "Allen", "yza@gmail.com" ,"creative", "inactive")
employee10 = Employee("Jake", "Harding", "bcd@gmail.com" , "IT", "active")

employees = [employee1,employee3,employee4,employee5]

class Manager(Employee):
    def __init__(self, first_name, last_name, email_address, department, active_status, employees=[]):
        self.employees=employees

    def add_employee(self, department):
        managed=[]
        if Employee.department==Manager.department:
            managed.append(Employee)
            return managed
    def show_employees(self):
        pass

    def remove_employee(self, email_address):
        pass

    
    

Manager1=Manager("Karen","Cane", "456@gmail.com", "IT","active",managed=[])
Manger2=Manager("Katie","Carter", "789@hotmail.com"",marketing","active", employees=[])
Manager3=Manager("Karen","Cane", "910@gmail.com" "sales","active", employees=[])
Manager4=Manager("Karen","Cane", "555@aol.com""creative","active", employees=[])


Manager1.add_employee(Employee.all)