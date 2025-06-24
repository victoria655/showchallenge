from app import app  # your Flask app instance
from models import User, Guest, Episode, Appearance
from models.database import db

with app.app_context():
    print("🧹 Clearing existing data...")

    # Delete in order to avoid foreign key issues
    Appearance.query.delete()
    Episode.query.delete()
    Guest.query.delete()
    User.query.delete()
    db.session.commit()

    print("🌱 Seeding users...")
    user1 = User(username="Toria")
    user1.password = "T3st!ng1"

    user2 = User(username="praise")
    user2.password = "Qw3rty!8"

    db.session.add_all([user1, user2])
    db.session.commit()

    print("🌱 Seeding guests...")
    guest1 = Guest(name="Alice")
    guest2 = Guest(name="Bob")
    db.session.add_all([guest1, guest2])
    db.session.commit()

    print("🌱 Seeding episodes...")
    episode1 = Episode(date="2025-06-01", number=1)
    episode2 = Episode(date="2025-06-15", number=2)
    db.session.add_all([episode1, episode2])
    db.session.commit()

    print("🌱 Seeding appearances...")
    appearance1 = Appearance(rating_id=7, guest_id=guest1.id, episode_id=episode1.id)
    appearance2 = Appearance(rating_id=8, guest_id=guest2.id, episode_id=episode2.id)
    db.session.add_all([appearance1, appearance2])
    db.session.commit()

    print("✅ Database seeded successfully!")
