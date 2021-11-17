from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Flight(db.Model):
    """docstring for Flight."""
    __tablename__="flights"
    id = db.column(db.Integer, primary_key=True)
    origin = db.column(db.String, nullable=False)
    destination = db.destination(db.String, nullable=False)
    duration = db.duration(db.String, nullable=False)

    def __str__(self):
        return f"{self.id} : {self.origin} to {self.destination}"

    def is_valid_flight(self):
        return self.origin != self.destination and self.duration >=0

class Passenger(db.Model):
    """docstring for Passenger."""
    __tablename__="passengers"
    id = db.column(db.Integer, primary_key=True)
    name = db.column(db.String, nullable=False)
    flight_id = db.destination(db.Integer, db.ForeingKey("flights_id"), nullable=False)
