from datetime import datetime
from flask import render_template, redirect, request

from flask_app import app
from flask_app.models.recipe import Recipe


@app.route("/create_recipe")
def create_recipe():
    now = datetime.now()
    today = now.strftime('%Y-%m-%d')
    return render_template("new_recipes.html", today=today)

@app.route("/recipes")
def recipes():
    all_recipes = Recipe.all_recipes_with_user()
    return render_template('recipes.html', all_recipes=all_recipes)


@app.route('/created', methods=['POST'])
def created():
    if not Recipe.validate_recepi(request.form):
        return redirect("/create_recipe")
    Recipe.created(request.form)
    return redirect('/recipes')

@app.route('/recepis', methods=['POST'])
def edit_recepi():
    Recipe.edited(request.form)
    return redirect('/edit_recepis.html')


@app.route('/recipes/<int:recipe_id>')
def show_recepi(recipe_id):
    
    data = {
        "id": recipe_id
    }
    recepi = Recipe.get_recepi(data)
    users_with_recepi = recepi.get_users_with_recepi(data)
    return render_template('show.html', recepi=recepi, ninjas_in_recepi=users_with_recepi)

