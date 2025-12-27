from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

Base = declarative_base()
engine = create_engine('sqlite:///resort.db')

class Room(Base):
    __tablename__ = 'rooms'
    room_number = Column(String, primary_key=True)
    room_type = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    status = Column(String, default="Available") # Available, Occupied, Maintenance
    features = Column(String)

class Guest(Base):
    __tablename__ = 'guests'
    guest_id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    room_number = Column(String, ForeignKey('rooms.room_number'))
    pending_bill = Column(Float, default=0.0) # Systematic billing tracking

class MenuItem(Base):
    __tablename__ = 'menu_items'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    description = Column(String)  # <--- Add this line back
    price = Column(Float)
    category = Column(String)

class FoodOrder(Base):
    __tablename__ = 'food_orders'
    id = Column(Integer, primary_key=True)
    room_number = Column(String)
    guest_id = Column(String)
    items = Column(String)
    total_amount = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

class ServiceRequest(Base):
    __tablename__ = 'service_requests'
    id = Column(Integer, primary_key=True)
    room_number = Column(String, nullable=False)
    request_type = Column(String, nullable=False) # e.g., "Towels", "Cleaning"
    status = Column(String, default="Pending")
    timestamp = Column(DateTime, default=datetime.utcnow)

def init_db():
    Base.metadata.create_all(engine)
    print("SUCCESS: Database initialized.")

if __name__ == "__main__":
    init_db()