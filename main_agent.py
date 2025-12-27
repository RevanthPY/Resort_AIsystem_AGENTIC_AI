import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
# Import all tools to ensure the AI has 'access' to everything
from tools import (get_available_rooms, place_restaurant_order, 
                   request_room_service, verify_guest_stay, get_menu_by_category)

# 1. Load the .env file FIRST
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# 2. Safety Check
if not api_key:
    raise ValueError("CRITICAL ERROR: GEMINI_API_KEY not found! Check your .env file.")

client = genai.Client(api_key=api_key)

# 3. Register all 5 tools so the AI doesn't say "I don't have access"
tools_list = [get_available_rooms, place_restaurant_order, 
              request_room_service, verify_guest_stay, get_menu_by_category]

config = types.GenerateContentConfig(
    system_instruction="""You are the Resort Manager. 
    - VERIFY: Use 'verify_guest_stay' for security.
    - MENU: Use 'get_menu_by_category' when guests ask for food.
    - ORDER: Use 'place_restaurant_order' and show the MEAL TOTAL for immediate payment.""",
    tools=tools_list
)

chat_session = client.chats.create(model="gemini-2.0-flash", config=config)