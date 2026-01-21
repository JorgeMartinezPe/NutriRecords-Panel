from flask import Flask,render_template,Blueprint,request,session,redirect,url_for
from app.models.usuario import Usuario
from app.extensions import db
from app.utils.hashing import proteccion
from app.utils.comprobar_rol import comprobar_rol
register_bp = Blueprint('register', __name__)


@register_bp.route('/register',methods = ['GET','POST'])
def registrar_usuario_form():
    if request.method =='POST':
        nombre = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        telefono = request.form.get('telefono')

        user_id = ( db.session.query(Usuario.uid) .filter(Usuario.email == email) .scalar() )
        user_name = ( db.session.query(Usuario.nombre) .filter(Usuario.uid == user_id) .scalar() ) #el metodo filter permite concatenacion

        
        
        print(nombre,email,password,telefono)
        if not all([nombre, email, password, telefono]):
            return "Faltan campos obligatorios", 400
        password_hash = proteccion(password)
        nuevo_usuario = Usuario(
            nombre=nombre,
            email=email,
            contrasena=password_hash,
            telefono=telefono,
            rol=comprobar_rol(email)
            )
        db.session.add(nuevo_usuario)
        db.session.commit()
        session['user'] = user_id
        session['name'] = user_name
        return "Usuario registrado correctamente"
    return redirect(url_for('main.index'))
    
    

