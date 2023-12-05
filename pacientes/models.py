from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200))
    correo = db.Column(db.String(200))
    cc = db.Column(db.Integer, default=0)
    plan_Salud = db.Column(db.String(200), default="N/A")
