from app.extensions import db
from datetime import datetime


from app.extensions import db
from datetime import datetime

class Mediciones(db.Model):
    __tablename__ = 'mediciones'

    id_medicion = db.Column(db.Integer, primary_key=True)

    paciente_id = db.Column(
        db.Integer,
        db.ForeignKey('pacientes.id_pacientes', ondelete='CASCADE'),
        nullable=False
    )

    fecha = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    peso = db.Column(db.Float, nullable=False)
    masa_muscular = db.Column(db.Float, nullable=False)
    grasa_corporal = db.Column(db.Float, nullable=False)
    cintura = db.Column(db.Float)
    altura = db.Column(db.Float)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    paciente = db.relationship(
        'Pacientes',
        back_populates='mediciones'
    )
