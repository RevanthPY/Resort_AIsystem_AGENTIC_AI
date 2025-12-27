from main_agent import chat_session
from reception_agent import handle_reception_task
from restaurant_agent import handle_restaurant_task
from room_service_agent import handle_room_service_task

def resort_manager_planner(user_input):
    routing_logic = f"""
    Analyze intent: '{user_input}'
    - 'SERVICE': Request for towels, cleaning, laundry, or amenities.
    - 'EXISTING': Request for food or the restaurant menu.
    - 'PROSPECTIVE': Questions about room booking or resort facilities.
    
    Reply ONLY with the category name.
    """
    category = chat_session.send_message(routing_logic).text.strip().upper()

    if "SERVICE" in category:
        return handle_room_service_task(user_input)
    elif "EXISTING" in category:
        return handle_restaurant_task(user_input)
    else:
        return handle_reception_task(user_input)