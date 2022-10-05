from flask_app.models.user import User
from flask_app.models.recepi import Recepi
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/login')
def login_reg():
    return render_template('login_reg.html')

@app.route('/register', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        # redirigimos a la plantilla con el formulario
        return redirect('/')
    # ...hacer otras cosas
    return redirect('/login')

# RUTAS DE CREACION (CREATE)
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
    return render_template('recepis.html', user_name=request.form['first_name'])


@app.route('/clearsession')
def limpiar_session():
    session.clear()
    return redirect('/')

# TODO Yo creo que este método no se usa
@app.route('/register/user', methods=['POST'])
def register_user():
    # validar el formulario aquí...
    # crear el hash
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    # poner pw_hash en el diccionario de datos
    data = {
        "username": request.form['username'],
        "password" : pw_hash
    }
    # llama al @classmethod de guardado en Usuario
    user_id = User.save(data)
    # almacenar id de usuario en la sesión
    session['user_id'] = user_id
    return redirect("/dashboard")

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
    return render_template('recepis.html', user_name=user_in_db.first_name)
