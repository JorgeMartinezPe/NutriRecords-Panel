from app.extensions import db
from datetime import datetime
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy import Text

class Alimentacion(db.Model):
    __tablename__ = 'alimentacion'

    id_alimentacion = db.Column(db.Integer, primary_key=True)

    paciente_id = db.Column(
        db.Integer,
        db.ForeignKey('pacientes.id_pacientes', ondelete='CASCADE'),
        nullable=False,
        unique=True  # relación 1 a 1
    )

    tipo_dieta = db.Column(db.String(100))

    intolerancias = db.Column(ARRAY(Text))
    preferencias = db.Column(ARRAY(Text))
    alimentos_no_gustan = db.Column(ARRAY(Text))
    suplementos = db.Column(ARRAY(Text))

    horarios_comida = db.Column(db.JSON)

    observaciones = db.Column(db.Text)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relación ORM
    paciente = db.relationship(
        'Pacientes',
        back_populates='alimentacion'
    )
