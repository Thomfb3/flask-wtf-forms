from flask import Flask, render_template, flash, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import NewPetForm
from seed import run_seed

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_agency'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False

app.config['SECRET_KEY'] = "keepthissecret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

#run_seed()


@app.route('/')
def show_pet_list():
    """Show Homepage Pet list"""
    pets = Pet.query.all()
    return render_template('pet_list.html', pets=pets)



@app.route('/pets/<int:pet_id>')
def show_pet_details(pet_id):
    """Show Homepage Pet list"""
    pet = Pet.query.get_or_404(pet_id)
    return render_template('pet_details.html', pet=pet)



@app.route('/pets/new', methods=["GET", "POST"])
def add_pet():
    """Renders new Pet form (GET) or handles New Pets form submission (POST)"""
    form = NewPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes, available=available)
        
        db.session.add(pet)
        db.session.commit()

        flash(f"New Pet Created: Name is {name}", "alert-success")
        return redirect(f'/pets/{pet.id}')
    else:
        return render_template("add_pet.html", form=form)



@app.route('/pets/<int:pet_id>/edit', methods=["GET", "POST"])
def update_pet(pet_id):
    """Update pet"""
    pet = Pet.query.get_or_404(pet_id)

    form = NewPetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.add(pet)
        db.session.commit()
    
        flash(f"Pet {pet.name} had been Updated", "alert-success")
        return redirect(f'/pets/{pet.id}')
    else:
        return render_template("edit_pet.html", form=form)



@app.route('/pets/<int:pet_id>/delete')
def delete_pet(pet_id):
    """Delete pet"""
    pet = Pet.query.get_or_404(pet_id)
    # Delete from db
    db.session.delete(pet)
    db.session.commit()
    # Return to Pets lists homepage
    flash("Pet has been deleted", "alert-danger")
    return redirect(f"/")


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('misc/404.html'), 404