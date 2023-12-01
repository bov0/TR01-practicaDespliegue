from database import db
from sqlalchemy.sql import func

# Para crear las tablas, desde el entorno de ejecución de Python, ejecutar:
# from database import app, db
# from empleado import Empleado
# app.app_context().push()
# db.create_all()

class Empleado(db.Model):
    __tablename__ = 'empleados'
         
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    telefono = db.Column(db.Integer, unique=True, nullable=False)
     
    def __init__(self, nombre, email, telefono):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def __repr__(self):
        return f'<Empleado {self.id}>: {self.nombre}, {self.email}'

    
    