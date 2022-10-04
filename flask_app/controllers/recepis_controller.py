from flask import render_template, redirect, request

from flask_app import app
from flask_app.models.recepi import Recepi


@app.route("/recepis")
def recepis():
    all_recepis = Recepi.all_recepis()
    return render_template('recepis.html', all_recepis=all_recepis)


@app.route('/created', methods=['POST'])
def created():
    Recepi.created(request.form)
    return redirect('/recepis')


@app.route('/recepis/<int:recepi_id>')
def show_recepi(recepi_id):
    data = {
        "id": recepi_id
    }
    recepi = recepi.get_recepi(data)
    users_with_recepi = recepi.get_users_with_recepi(data)
    return render_template('recepis.html', recepi=recepi, ninjas_in_recepi=users_with_recepi)

