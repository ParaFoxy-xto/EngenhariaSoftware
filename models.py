from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Presenca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    matricula = db.Column(db.String(20), nullable=False)
    datahora = db.Column(db.DateTime, nullable=False)
