from app.extensions import db
from sqlalchemy import LargeBinary
from datetime import datetime
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy import String


class HistorialClinico(db.Model):
    __tablename__ = 'historial_clinico'
    id_historial_clinico = db.Column(db.Integer, primary_key=True)  # identity en postgres
    enfermedades = db.Column(ARRAY(String),default=list)
    alergias = db.Column(ARRAY(String),default=list)
    cirugias = db.Column(ARRAY(String),default=list)
    medicamentos = db.Column(ARRAY(String),default=list)
    notas = db.Column(db.Text, nullable = False)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)


    pacientes_id = db.Column(
    db.Integer,
    db.ForeignKey('pacientes.id_pacientes', ondelete='CASCADE'),
    nullable=False
    )
    pacientes = db.relationship(
        'Pacientes',
        back_populates = 'historial_clinico'
    )