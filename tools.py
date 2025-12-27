from database import engine, Room, MenuItem, FoodOrder, Guest, ServiceRequest
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

def get_available_rooms():
    """Returns a summary of available rooms from the 90-room inventory."""
    session = Session()
    rooms = session.query(Room).filter(Room.status == "Available").all()
    session.close()
    if not rooms: return "We are fully booked."
    # Grouping for cleaner response
    types = [r.room_type for r in rooms]
    summary = {t: types.count(t) for t in set(types)}
    return "Available: " + ", ".join([f"{count} {t}" for t, count in summary.items()])

def verify_guest_stay(room_number: str, guest_id: str):
    """Verifies identity against the 15-guest registry."""
    session = Session()
    guest = session.query(Guest).filter_by(room_number=str(room_number), guest_id=str(guest_id)).first()
    session.close()
    if guest: return f"Verified: {guest.name} in Room {guest.room_number}."
    return "Error: Guest not found."

def get_menu_by_category(category_name: str):
    """Fetches items for the menu."""
    session = Session()
    items = session.query(MenuItem).filter(MenuItem.category.ilike(f"%{category_name}%")).all()
    session.close()
    if not items: return "Category not found. Try: Breakfast, Starters, Main Course, or Drinks."
    return "\n".join([f"{i.name}: ₹{i.price}" for i in items])

def place_restaurant_order(room_number: str, item_name: str, quantity: int, guest_id: str):
    """Places order and calculates the meal total for orderly payment."""
    session = Session()
    item = session.query(MenuItem).filter(MenuItem.name.ilike(item_name.strip())).first()
    guest = session.query(Guest).filter_by(room_number=str(room_number), guest_id=str(guest_id)).first()
    if not item or not guest:
        session.close()
        return "Order failed. Check item name or guest ID."
    
    total = item.price * quantity
    guest.pending_bill += total
    new_order = FoodOrder(room_number=room_number, guest_id=guest_id, items=f"{quantity}x {item.name}", total_amount=total)
    session.add(new_order)
    session.commit()
    session.close()
    return f"TOTAL FOR THIS MEAL: ₹{total}. (Ordered: {quantity}x {item.name})"

def request_room_service(room_number: str, request_type: str):
    """Handles housekeeping requests."""
    session = Session()
    new_req = ServiceRequest(room_number=room_number, request_type=request_type, status="Pending")
    session.add(new_req)
    session.commit()
    session.close()
    return f"Success: {request_type} request logged for Room {room_number}."