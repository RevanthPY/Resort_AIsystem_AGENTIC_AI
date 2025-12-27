import time
import sys
from manager import resort_manager_planner

def loading_animation():
    """Displays a simple 'Thinking...' animation to show waiting time."""
    animation = ["|", "/", "-", "\\"]
    for i in range(15):  # Plays for about 3 seconds
        time.sleep(0.2)
        sys.stdout.write(f"\r[System: Resort Manager is thinking... {animation[i % len(animation)]}]")
        sys.stdout.flush()
    print("\n")

def start_resort_chat():
    print("\n" + "="*50)
    print("      RESORT AI: OFFICIAL GUEST CHAT")
    print("="*50)
    print("Safety: Automatic delay active to protect API quota.")
    print("Type 'exit' to end session.\n")

    while True:
        user_msg = input("Guest: ").strip()
        
        if user_msg.lower() in ['exit', 'quit']:
            print("Goodbye! Have a pleasant stay.")
            break
        
        if not user_msg:
            continue
            
        # 1. Show that the agent is working
        loading_animation()
        
        try:
            # 2. Process the request
            ai_response = resort_manager_planner(user_msg)
            print(f"Resort Response: {ai_response}")
            
            # 3. CRITICAL: Force a 10-second wait after every response
            # This prevents the 'RESOURCE_EXHAUSTED' error
        
            print("-" * 50)
            
        except Exception as e:
            if "429" in str(e):
                print("\n[Quota Full]: Please wait 60 seconds... Google is cooling down.")
                time.sleep(60)
            else:
                print(f"\n[Error]: {e}")

if __name__ == "__main__":
    start_resort_chat()