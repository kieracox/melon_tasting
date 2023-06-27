"""Database models for melon tasting app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, unique=True, nullable=False)

    appointments = db.relationship("Appointment", back_populates="user")

    def __repr__(self):
        return f"User id={self.id}, username={self.username}"

class Appointment(db.Model):
    __tablename__ = "appointment"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    date = db.Column(db.Date)
    time = db.Column(db.Time)


    user = db.relationship("User", back_populates="appointments")

    def __repr__(self):
        return f"Appointment id={self.id} for user: {self.user_id} on: {self.date}"

def connect_to_db(flask_app, db_uri="postgresql:///jobs", echo=False):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = False
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    connect_to_db(app)