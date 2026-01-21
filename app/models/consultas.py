from app.extensions import db
from datetime import datetime

class Consultas(db.Model):
    __tablename__ = 'consultas'

    id_consulta = db.Column(db.Integer, primary_key=True)

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

    peso = db.Column(db.Float)
    imc = db.Column(db.Float)
    grasa_corporal = db.Column(db.Float)
    masa_muscular = db.Column(db.Float)

    notas = db.Column(db.Text)

    proxima_cita = db.Column(db.DateTime)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relación ORM
    paciente = db.relationship(
        'Pacientes',
        back_populates='consultas'
    )
