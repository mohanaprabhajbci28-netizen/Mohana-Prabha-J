from collections import namedtuple, defaultdict, Counter, deque, OrderedDict

Employee = namedtuple('Employee', ['emp_id', 'name', 'department', 'salary'])
all_employees = OrderedDict()
dept_groups = defaultdict(list)
task_queue = deque()

def add_employee():
    try:
        emp_id = int(input("Enter Employee ID: "))
        if emp_id in all_employees:
            return print("Error: ID already exists!")
        name = input("Enter Name: ")
        dept = input("Enter Department: ")
        salary = float(input("Enter Salary: "))
        
       
        new_emp = Employee(emp_id, name, dept, salary)
        all_employees[emp_id] = new_emp
        dept_groups[dept].append(new_emp)
        print(f"Successfully added {name}!")
    except ValueError:
        print("Invalid input! ID and Salary must be numbers.")


def main_menu():
    while True:
        print("\n--- Employee Management System ---")
        print("1. Add Employee\n2. Exit")
        choice = input("Select an option (1-2): ")
        if choice == '1': add_employee()
        elif choice == '2': break
        else: print("Invalid choice.")

if __name__ == "__main__":
    main_menu()
