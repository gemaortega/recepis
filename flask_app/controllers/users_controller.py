from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


@app.route('/login_reg')
def login_reg():
    return render_template('login_reg.html')


@app.route('/register', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        return redirect('/')
    return redirect('/login')


@app.route('/create_user', methods=['POST'])
def create_user():
    if not User.validate_user(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(f"pw_hash: {pw_hash}")
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': pw_hash
    }
    print(data, "EFECTIVAMENTE ATRAPAMOS LA INFO DEL FORMULARIO")
    id_user = User.save(data)
    print(id_user, "QUE RETORNO EL HABER REGISTRADO UN USUARIO NUEVO?")
    session['user_id'] = id_user
    session['user_name'] = request.form['first_name']
    print(f"session['user_id']: {session['user_id']}")
    print(f"session['user_name']: {session['user_name']}")
    # A diferencia del render_template("recipes.html") del login, aquí no le pasamos la variable "all_recipes"
    # ya que como el usaurio acaba de ser creado no debe tener ninguna receta asociada a él.
    return render_template("recipes.html")


@app.route('/login', methods=['POST'])
def login():
    # ver si el nombre de usuario proporcionado existe en la base de datos
    data = { "email" : request.form["email_login"] }
    user_in_db = User.get_by_email(data)
    # usuario no está registrado en la base de datos
    if not user_in_db:
        flash("1 Invalid Email/Password", 'login')
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password_login']):
        # si obtenemos False después de verificar la contraseña
        flash("2 Invalid Email/Password", 'login')
        return redirect('/')
    # si las contraseñas coinciden, configuramos el user_id en sesión
    # ¡¡¡Nunca renderices en una post!!!
    session['user_id'] = user_in_db.id
    session['user_name'] = user_in_db.first_name
    print(f"session['user_id']: {session['user_id']}")
    print(f"session['user_name']: {session['user_name']}")
    return render_template('recipes.html', all_recipes=Recipe.all_recipes_with_user())
