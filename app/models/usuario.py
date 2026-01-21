from app.extensions import db
from sqlalchemy import LargeBinary
from datetime import datetime
from app.models.pacientes import Pacientes
class Usuario(db.Model):
    __tablename__ = 'usuarios'

    uid = db.Column(db.Integer, primary_key=True)  # identity en postgres
    nombre = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    contrasena = db.Column(LargeBinary(60),nullable=False) 
    telefono = db.Column(db.String(20))
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    rol = db.Column(db.String(50), default='usuario')
    apellido = db.Column(db.String(255), nullable=False)

    pacientes = db.relationship( #para crear la relacion entre tablas hay que agregar esto
        'Pacientes', #Tabla a relacionar
        back_populates='usuario',
        cascade='all, delete'
    )
    def __repr__(self):
        return f'<Usuario {self.nombre}>'
