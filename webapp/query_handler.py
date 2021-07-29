from .model import Employee, Department
from . import db


def create_new_emp(first_name, last_name, department):
    if last_name:
        name = first_name + " " + last_name
    else:
        name = first_name
    department_id = find_dep_id(department)

    old_emp = Employee.query.filter_by(name=name).first()
    if old_emp:
        old_emp = Employee.query.filter_by(department_id=department_id).first()
        if old_emp:
            return False

    new_emp = Employee(name=name, department_id=department_id,
                       emp_email=create_emp_email(first_name, last_name))

    db.session.add(new_emp)
    db.session.commit()

    return True


def search_for_emp(emp_id):
    print("Looking for employee ID {}".format(emp_id))
    emp = Employee.query.filter_by(employee_id=emp_id).first()
    if emp:
        print("Found {}".format(emp.name))
        return emp
    print("Not Found")
    return 0


def find_dep_id(dep_name):
    print("Searching for Department {}".format(dep_name))
    if not Department.query.all():
        populate_departments()
    dep = Department.query.filter_by(name=dep_name).first()
    if dep:
        print("Department ID: {}".format(dep.department_id))
        return dep.department_id
    return 0


def create_emp_email(first_name, last_name):
    if last_name:
        emp_email = first_name.lower() + last_name.lower() + "@totallynotfakecompany.com"
    else:
        emp_email = first_name.lower() + "@totallynotfakecompany.com"

    i = 0
    while Employee.query.filter_by(emp_email=emp_email).first():
        emp_email = first_name.lower() + str(i) + "@totallynotfakecompany.com"
        i += 1

    return emp_email


def populate_departments():
    departments = []
    aiml = Department(name="AI/ML", department_id=100)
    departments.append(aiml)
    design = Department(name="Design")
    departments.append(design)
    development = Department(name="Development")
    departments.append(development)
    finance = Department(name="Finance")
    departments.append(finance)
    gm = Department(name="General Management")
    departments.append(gm)
    hr = Department(name="HR")
    departments.append(hr)
    marketing = Department(name="Marketing")
    departments.append(marketing)
    ops = Department(name="Operations")
    departments.append(ops)
    qa = Department(name="Quality Assurance")
    departments.append(qa)
    sales = Department(name="Sales")
    departments.append(sales)

    for d in departments:
        db.session.add(d)

    db.session.commit()
