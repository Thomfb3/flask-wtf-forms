from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


######## MODELS

class Pet(db.Model):
    """Pet Model"""
    __tablename__ = "pets"

    # Set the Pet columns
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, nullable=True, default="https://picsum.photos/id/433/300/300")
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    available = db.Column(db.Boolean, nullable=False)

    # Backreference all posts for user and cascade delete posts
    #posts = db.relationship("Post", backref="user", cascade="all, delete-orphan")

    # Pet Model Representation
    def __repr__(self):
        p = self
        return f"<Pet id={p.id} name={p.name} species={p.species} photo_url={p.photo_url} age={p.age} notes={p.notes}  available={p.available}>"

    @property
    def availability(self):
        if self.available:
            return "Available"
        else:
            return "Unavailable"

    @property
    def species_cap(self):
        return self.species.capitalize()