from flask import Blueprint, render_template, request, flash, redirect, url_for
from .query_handler import create_new_emp, search_for_emp

viewsBP = Blueprint("view", __name__)


@viewsBP.route("/", methods=["GET", "POST"])
def home_page():
    if request.method == "POST":
        auth_form = request.form
        print(auth_form)
        emp = search_for_emp(emp_id=auth_form.get("emp_id"))
        if emp:
            flash("Employee: {} - Department ID: {} - e-mail: {}".format(emp.name, emp.department_id, emp.emp_email))
        else:
            flash("ID not associated with any employee")
    return render_template("app_page.html")


@viewsBP.route("/add_new_emp", methods=["GET", "POST"])
def add_new_emp():
    if request.method == "POST":
        auth_form = request.form
        print(auth_form)
        if create_new_emp(auth_form.get("firstname"),
                          auth_form.get("lastname"), auth_form.get("department")):
            return redirect(url_for("view.home_page"))

        else:
            flash("Failed to create new employee - There is already someone with this name in this department")
    return render_template("add_new_emp.html")

