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

@app.route('/edit/<int:recipe_id>')
def edit_recipe(recipe_id):
    data = {
        "id": recipe_id
    }
    recipe= Recipe.get_recipe(data)
    print(f'recipe:{recipe}')
    return render_template('/edit_recipe.html', recipe=recipe)


@app.route('/recipe/<int:recipe_id>')
def show_recipe(recipe_id):
    recipe = Recipe.get_recipe_with_user(recipe_id)
    print(f"recipe: {recipe}")
    return render_template('show.html', recipe=recipe)
