from flask import Flask,Blueprint,render_template,request
home_bp = Blueprint('home_page',__name__, url_prefix="/home")



@home_bp.route('/')
def home_page():

    return render_template('home_page.html')




