from main_agent import chat_session
from tools import get_available_rooms

def handle_reception_task(user_query):
    system_prompt = f"""
    You are the Senior Concierge. 
    
    1. Call 'get_available_rooms' for live 90-room data.
    2. USE THESE FIXED PRICES IN YOUR REPLY:
       - Standard Room: ₹3,500 per night
       - Deluxe Room: ₹5,500 per night
       - Executive Suite: ₹8,500 per night
       - Presidential Suite: ₹15,000 per night.
    3. For multi-night stays (like 3 nights), calculate the total for the guest.
    
    USER REQUEST: "{user_query}"
    """
    response = chat_session.send_message(system_prompt)
    return response.text