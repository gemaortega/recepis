from flask import render_template, redirect, request

from flask_app import app
from flask_app.models.recepi import Dojo
from flask_app.models.ninja_model import Ninja


@app.route('/ninjas')
def form_ninja():
    all_dojos = Dojo.all_dojos()
    return render_template('ninjas.html', all_dojos=all_dojos)


@app.route("/created_ninja", methods=['POST'])
def created_ninja():
    print(request.form, "CONTIENE")
    id_ninja = Ninja.created_ninja(request.form)
    data = {
        "id": id_ninja
    }
    ninja = Ninja.get_ninja(data)
    print(ninja, "CONTIENE")
    return redirect(f'/dojos/{ninja.dojo_id}')
