from app.extensions import db
from sqlalchemy import func, select
from sqlalchemy.orm import Session
from app.models.pacientes import Pacientes



def contar_pacientes() -> int:
    statement = select(func.count()).select_from(Pacientes)
    if statement == None:
        return 0
    else:
        return db.session.execute(statement).scalar_one()


"""
Notas: Es necesario que todo valor que se necesite procesar, consultas, etc se tenga en una funcion, para evitar app context error
Solo cuando se hacen consultas, y al momento de importar no se hara la ejecucion si no hasta que el codigo llegue al flujo de la funcion que necesite dicho valor
Al hacer esto:
No se ejecuta nada hasta que la función es llamada
Flask ya tendrá contexto si se llama desde una ruta
"""