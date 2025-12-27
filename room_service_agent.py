from main_agent import chat_session
from tools import request_room_service, verify_guest_stay

def handle_room_service_task(user_query):
    system_prompt = f"""
    You are the Guest Services Agent.
    
    TASK: Handle the request: "{user_query}"
    
    SYSTEMATIC RULES:
    1. VERIFY: You MUST have the Room Number and Guest ID. Call 'verify_guest_stay' first.
    2. LOG REQUEST: Use 'request_room_service' to save the request to the database.
    3. CATEGORIES: Handle Laundry, Cleaning, and Amenities (toothbrush, paste, towels, etc.).
    4. CONFIRMATION: Tell the guest: "Your request for [item] has been logged for Room [number]. Our staff will arrive shortly."
    """
    response = chat_session.send_message(system_prompt)
    return response.text