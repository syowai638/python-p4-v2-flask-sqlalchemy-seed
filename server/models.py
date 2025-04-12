from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    species = db.Column(db.String(100), nullable=False)
    color = db.Column(db.String(50))
    age = db.Column(db.String(50))

    def __repr__(self):
        return f'<Pet {self.id}, {self.name}, {self.species}>'
