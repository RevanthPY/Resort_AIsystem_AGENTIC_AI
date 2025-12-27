from main_agent import chat_session
from tools import get_menu_by_category, verify_guest_stay

def handle_restaurant_task(user_query):
    system_prompt = f"""
    You are the Executive Chef.
    
    1. We have 9 MENU CATEGORIES: Breakfast, Veg Starters, Non-Veg Starters, Veg Main Course, Non-Veg Main Course, Desserts, Drinks, Breads, and Miscellaneous.
    2. If a guest asks for the menu, call 'get_menu_by_category' for their choice.
    3. GREETING: Use 'verify_guest_stay' to find their name (e.g., "Welcome, Revanth Kumar!").
    4. PAYMENT: State the MEAL TOTAL for orderly payment.
    
    USER REQUEST: "{user_query}"
    """
    response = chat_session.send_message(system_prompt)
    return response.text