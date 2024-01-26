class Employee:
    # Initializer #
    def __init__(self, first_name, last_name, emp_number):
        self.first_name = first_name
        self.last_name = last_name
        self.emp_number = emp_number
        
    #Getter 
    @property    #decorator for getter
    def full_name(self):
        return self.first_name + " " + self.last_name
    
    @property
    def print_emp_info(self):
        print(f"{self.emp_number}: {self.first_name} {self.last_name}")
        
    @property
    def print_emp_name_5x(self):
        print(f"{self.first_name*5}")
        
