import os
import pandas as pd
from database import engine, Room, Base
from sqlalchemy.orm import sessionmaker

def complete_room_setup():
    # 1. Force the correct directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    excel_path = os.path.join(script_dir, "Resort_Inventory.xlsx")
    
    print(f"Targeting Folder: {script_dir}")

    # 2. GENERATE THE DATA (Systematic 90-room inventory)
    data = []
    # Standard Rooms (101-140)
    for i in range(1, 41): 
        data.append({
            "Room_Number": 100+i, 
            "Room_Type": "Standard", 
            "Price_per_Night": 3500, 
            "Status": "Available" if i % 5 != 0 else "Occupied",
            "Features": "Garden View, Wifi"
        })
    # Deluxe Rooms (201-230)
    for i in range(1, 31): 
        data.append({
            "Room_Number": 200+i, 
            "Room_Type": "Deluxe", 
            "Price_per_Night": 5500, 
            "Status": "Available" if i % 4 != 0 else "Occupied",
            "Features": "Balcony, King Bed"
        })
    # Executive Suites (301-315)
    for i in range(1, 16): 
        data.append({
            "Room_Number": 300+i, 
            "Room_Type": "Executive Suite", 
            "Price_per_Night": 8500, 
            "Status": "Available" if i % 3 != 0 else "Maintenance",
            "Features": "Living Area, Bathtub"
        })
    # Presidential Suites (401-405)
    for i in range(1, 6): 
        data.append({
            "Room_Number": 400+i, 
            "Room_Type": "Presidential", 
            "Price_per_Night": 15000, 
            "Status": "Available",
            "Features": "Private Pool, Butler"
        })

    # 3. SAVE EXCEL
    df = pd.DataFrame(data)
    df.to_excel(excel_path, index=False, sheet_name="Rooms")
    print(f"FILE CREATED: {excel_path}")

    # 4. SYNC TO DATABASE
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    
    print("Clearing database and importing rooms...")
    session.query(Room).delete()
    
    for _, row in df.iterrows():
        # Updated to match new 'status' and 'features' columns
        room = Room(
            room_number=str(row['Room_Number']),
            room_type=row['Room_Type'],
            price=float(row['Price_per_Night']),
            status=str(row['Status']), # Replaced is_available
            features=str(row['Features'])
        )
        session.add(room)
        
    session.commit()
    print(f"SUCCESS: {len(df)} Rooms are now in resort.db with proper Status codes.")
    session.close()

if __name__ == "__main__":
    complete_room_setup()