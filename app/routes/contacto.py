from flask import Flask,Blueprint,render_template


contacto_bp = Blueprint('contacto', __name__, url_prefix="/contacto") #Nombres deben coincidir




@contacto_bp.route('/contacto/<nombre>')
def contacto(nombre):
    
    data= {
        'titulo':'Contacto',
        'nombre':nombre
    }
    return render_template('contacto.html',data=data)



