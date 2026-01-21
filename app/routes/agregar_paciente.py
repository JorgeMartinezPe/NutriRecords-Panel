from flask import Flask,render_template,Blueprint,session
"""
Funcion para agregar pacientes
"""
from app.extensions import db
from app.models.usuario import Pacientes

agregar_paciente_bp = Blueprint('agregar_paciente',__name__)

@agregar_paciente_bp.route('/agregar_pacientee')




def agregar_paciente_boton():
    
    user_name = ( db.session.query(Pacientes.nombre).filter(Pacientes.usuario_id == 4).scalar()) #el metodo filter permite concatenacion
    print(user_name)
    return render_template('agregar_paciente.html',user_name=user_name)

