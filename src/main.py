"""
Mock Sales Call Application

This module provides a simple command-line interface for simulating sales calls.
"""

def main():
    """Main entry point for the Mock Sales Call application."""
    print("Welcome to Mock Sales Call!")
    print("-" * 30)
    
    # Basic user interaction
    name = input("Please enter your name: ")
    print(f"\nHello, {name}! Let's get started with your mock sales call.")
    
    # Simple conversation flow
    print("\n[System] The call has started...")
    print("[System] Type 'exit' to end the call at any time.")
    
    while True:
        user_input = input("\nYou: ").strip().lower()
        
        if user_input == 'exit':
            print("\n[System] Ending the call. Goodbye!")
            break
            
        # Simple response logic (to be replaced with AI integration)
        if any(greeting in user_input for greeting in ['hi', 'hello', 'hey']):
            print("AI: Hello! How can I assist you with our product today?")
        elif 'price' in user_input:
            print("AI: Our pricing starts at $99/month for the basic plan.")
        elif 'feature' in user_input:
            print("AI: Our product includes features like AI-powered analytics, real-time reporting, and 24/7 support.")
        elif 'demo' in user_input:
            print("AI: I'd be happy to schedule a demo for you. When would be a good time?")
        else:
            print("AI: I'm here to help you learn more about our product. Could you tell me what interests you the most?")

if __name__ == "__main__":
    main()
