
from planeador import db
import datetime
class Clase(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    fecha = db.Column(db.Date, default=datetime.date.today)
    cursoId = db.Column(db.Integer, db.ForeignKey('curso.id'), nullable=False)
    materiaId = db.Column(db.Integer, db.ForeignKey('materia.id'), nullable=False)
    titulo = db.Column(db.String(40), nullable = False) #Maximum of 40 characters
    materiales = db.Column(db.String(500))
    objetivo = db.Column(db.String(500))
    explicacion = db.Column(db.String(2000))
    practica = db.Column(db.String(2000))
    conclusion = db.Column(db.String(2000))
    
    def __repr__(self):
        return f"Clase de {self.materia} para {self.curso} con titulo: {self.titulo}"
class Curso(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(10), nullable=False)
    seccion = db.Column(db.String(1), default='A', nullable=False)
    clases = db.relationship('Clase', backref='curso', lazy=True)
    def __repr__(self):
        return f"{self.nombre} {self.seccion}"

class Materia(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(20), nullable=False)
    clases = db.relationship('Clase', backref='materia', lazy=True)
    def __repr__(self):
        return f"{self.nombre}"