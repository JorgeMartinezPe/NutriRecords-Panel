from app.extensions import db
from datetime import datetime

class EstiloVida(db.Model):
    __tablename__ = 'estilo_vida'

    id_estilo_vida = db.Column(db.Integer, primary_key=True)

    paciente_id = db.Column(
        db.Integer,
        db.ForeignKey('pacientes.id_pacientes', ondelete='CASCADE'),
        nullable=False,
        unique=True  # asegura relación 1 a 1
    )

    nivel_actividad = db.Column(db.String(50), nullable=False)
    tipo_ejercicio = db.Column(db.String(255))
    horas_sueno = db.Column(db.Float)
    nivel_estres = db.Column(db.String(50))

    alcohol = db.Column(db.Boolean, default=False)
    tabaco = db.Column(db.Boolean, default=False)

    observaciones = db.Column(db.Text)

    # Relación ORM
    paciente = db.relationship(
        'Pacientes',
        back_populates='estilo_vida'
    )