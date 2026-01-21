from app.extensions import db
from datetime import datetime
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy import String

class ObjetivoNutricionales(db.Model):
    __tablename__ = 'objetivos_nutricionales'

    id_objetivos = db.Column(db.Integer,primary_key = True,)
    paciente_id = db.Column(
        db.Integer,
        db.ForeignKey('pacientes.id_pacientes', ondelete='CASCADE'),
        nullable=False,
        unique=True  # asegura relación 1 a 1
    )
    objetivo = db.Column(db.String(60), nullable=False)
    intorelancias = db.Column(ARRAY(String),default=list) #Quitar del modelo y base de datos
    peso_objetivo = db.Column(ARRAY(String),default=list)
    fecha_objetivo = db.Column(ARRAY(String),default=list)
    objetivo = db.Column(db.TEXT, nullable=False)


    # Relación ORM
    paciente = db.relationship(
        'Pacientes',
        back_populates='objetivos_nutricionales'
    )