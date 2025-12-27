import pandas as pd
from database import engine, Guest, Room
from sqlalchemy.orm import sessionmaker

def populate_guests():
    # 1. Load your 90-room inventory to see who should be 'Occupied'
    inventory_df = pd.read_excel("Resort_Inventory.xlsx")
    occupied_data = inventory_df[inventory_df['Status'] == 'Occupied']
    
    names = [
        "Revanth Kumar", "Alice Sharma", "Bob Varma", "Charlie Khan", 
        "Diana Prince", "Ethan Hunt", "Fiona Gallagher", "George Miller",
        "Hannah Abbott", "Ian Wright", "Julia Roberts", "Kevin Hart",
        "Laura Palmer", "Michael Scott", "Nina Simone"
    ]

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        for i, (index, row) in enumerate(occupied_data.iterrows()):
            if i >= len(names): break # Stop at 15
            
            new_guest = Guest(
                guest_id=f"G-{1001 + i}",
                name=names[i],
                room_number=str(row['Room_Number']),
                pending_bill=0.0
            )
            session.add(new_guest)
            
        session.commit()
        print(f"SUCCESS: {i+1} guests added to Guest Registry.")
    except Exception as e:
        print(f"Error: {e}")
        session.rollback()
    finally:
        session.close()

if __name__ == "__main__":
    populate_guests()