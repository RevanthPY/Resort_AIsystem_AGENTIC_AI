from database import engine, Guest, Room
from sqlalchemy.orm import sessionmaker

def check_registry():
    Session = sessionmaker(bind=engine)
    session = Session()
    
    print("\n--- GUEST REGISTRY (Top 5) ---")
    guests = session.query(Guest).limit(5).all()
    for g in guests:
        print(f"ID: {g.guest_id} | Name: {g.name} | Room: {g.room_number}")
        
    print("\n--- ROOM STATUS (Sample) ---")
    occupied_rooms = session.query(Room).filter_by(status='Occupied').limit(5).all()
    for r in occupied_rooms:
        print(f"Room: {r.room_number} | Type: {r.room_type} | Status: {r.status}")
    
    session.close()

if __name__ == "__main__":
    check_registry()