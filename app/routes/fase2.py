from flask import Flask,render_template,Blueprint,session,redirect,url_for,request
from app.utils.metricas import contar_pacientes




consulta_fase2_bp = Blueprint('consultafase2',__name__)


@consulta_fase2_bp.route('/consultafase2')
def consulta_fase_2():

    return render_template("ConsultaPhase2.html")