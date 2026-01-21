from flask import Flask,render_template,Blueprint,session,redirect,url_for,request
from app.utils.metricas import contar_pacientes
"""
Nombre de la aplicacion NutriRecords Panel
"""

main_bp = Blueprint('main', __name__)

logout_bp = Blueprint('logout',__name__)

consulta_bp = Blueprint('consulta',__name__)
@main_bp.route('/')
def index():
    user_id = session.get('user')
    user_name = session.get('name')
    datos_home = {
        'total_pacientes': contar_pacientes()
    }
    if user_id and user_name:
        return render_template('home_page.html', user_id=user_id,user_name=user_name,datos_home = datos_home)
    
    else:
        return render_template( 'index.html')



@main_bp.route('/home/')
def home():
    return redirect(url_for('main.index'))

@main_bp.after_request
def no_cache(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@logout_bp.route('/logout')
def logout_session():
    session.pop('user',None)
    return redirect(url_for('main.index'))

@consulta_bp.route('/consulta')
def modo_consulta():

    return render_template("ConsultaPhase1.html")