from app.extensions import db
from datetime import datetime
from app.models.historial_clinico import HistorialClinico
from app.models.constants import CASCADE_ALL_DELETE
from app.models.alimentacion_paciente import Alimentacion
from app.models.estilo_vida import EstiloVida
from app.models.objetivos_nutricionales import ObjetivoNutricionales
from app.models.mediciones import Mediciones
from app.models.consultas import Consultas
class Pacientes(db.Model):
    __tablename__ = 'pacientes'

    id_pacientes = db.Column(db.Integer, primary_key=True)  # identity en postgres
    usuario = db.relationship(
    'Usuario',
    back_populates='pacientes'
    )
    nombre = db.Column(db.String(255), nullable=False)
    apellido = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    edad = db.Column (db.Integer,nullable = False)
    telefono = db.Column(db.String(20))
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    usuario_id = db.Column(
    db.Integer,
    db.ForeignKey('usuarios.uid', ondelete='CASCADE'),
    nullable=False
    )

    historial_clinico = db.relationship( #para crear la relacion entre tablas hay que agregar esto
        'HistorialClinico', #Tabla a relacionar
        back_populates = 'pacientes',
        cascade = CASCADE_ALL_DELETE
    )
    
    consultas = db.relationship(
        'Consultas',
        back_populates='paciente',
        cascade=CASCADE_ALL_DELETE,
        order_by='Consultas.fecha.desc()'
    )
    
    alimentacion = db.relationship(
    'Alimentacion',
    back_populates='paciente',
    uselist=False,
    cascade=CASCADE_ALL_DELETE
    )
    
    estilo_vida = db.relationship(
    'EstiloVida',
    back_populates = 'paciente',
    uselist = False,
    cascade = CASCADE_ALL_DELETE
    )
    
    objetivos_nutricionales= db.relationship(
    'ObjetivoNutricionales',
    back_populates='paciente',
    uselist = False,
    cascade = CASCADE_ALL_DELETE
    )
    mediciones = db.relationship(
    'Mediciones',
    back_populates='paciente',
    uselist = False,
    cascade = CASCADE_ALL_DELETE,
    order_by='Mediciones.fecha.desc()'
    )
    