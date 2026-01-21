from flask import Flask,render_template,Blueprint,request,session,redirect,url_for
from app.models.usuario import Usuario
from app.extensions import db
from app.utils.hashing import verificar_password


sesion_bp = Blueprint('sesion', __name__)


@sesion_bp.route('/login',methods = ['GET','POST'])
def verifica_sesion_form():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        usuario = Usuario.query.filter_by(email=email).first()
        user_id = ( db.session.query(Usuario.uid).filter(Usuario.email == email).scalar())
        user_name = ( db.session.query(Usuario.nombre) .filter(Usuario.uid == user_id).scalar())
        
        if not usuario:
            return 'Credenciales incorrectas'

        if verificar_password(password, usuario.contrasena):
            session['user'] = user_id
            session['name'] = user_name
            return redirect(url_for('main.index'))

    return render_template('login.html')
        

            


        
