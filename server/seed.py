from app import app, db
from models import Pet

with app.app_context():
    print("Clearing existing data...")
    Pet.query.delete()

    print("Seeding new data...")
    pet1 = Pet(name='Buddy', species='Dog', color='Brown', age='5')
    pet2 = Pet(name='Mittens', species='Cat', color='White', age='3')

    db.session.add_all([pet1, pet2])
    db.session.commit()

    print("Database seeded successfully.")
