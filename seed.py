"""Seed file to make sample data for db."""
from models import db, connect_db, Pet


def run_seed():
    # Create all tables
    db.drop_all()
    db.create_all()

    Pet.query.delete()


    # Add sample Pets
    p1 = Pet(name='Spot', species='dog', photo_url='https://picsum.photos/id/237/300/300', age=1, notes="It's a dog", available=True )
    p2 = Pet(name='Grizz', species='Bear', photo_url='https://picsum.photos/id/433/300/300', age=20, notes="It's a bear", available=True )
    p3 = Pet(name='Snuggles', species='dog', photo_url='https://picsum.photos/id/1062/300/300', age=101, notes="Here are my notes.", available=True )
    p4 = Pet(name='Marcus', species='lion', photo_url='https://picsum.photos/id/1074/300/300', age=5, notes="Here are my notes.", available=True )
    p5 = Pet(name='Marcus', species='tiger', photo_url='https://picsum.photos/id/593/300/300', age=5, notes="Here are my notes.", available=True )
    p6 = Pet(name='Marcus', species='tiger', photo_url='https://picsum.photos/id/718/300/300', age=5, notes="Here are my notes.", available=True )



    db.session.add_all([p1, p2, p3, p4, p5, p6])
    db.session.commit()




