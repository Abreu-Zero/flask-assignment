from webapp import db


class Employee(db.Model):
    employee_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    department_id = db.Column(db.Integer, db.ForeignKey("department.department_id"))
    date_of_hire = db.Column(db.DateTime)
    emp_email = db.Column(db.String(43))


class Department(db.Model):
    department_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(43), unique=True)
    employees = db.relationship("Employee")
