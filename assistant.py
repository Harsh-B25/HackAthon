import requests
import json
import sys
from datetime import datetime
import os

class LegalAssistant:
    def __init__(self):
        self.base_url = "http://localhost:11434/api/generate"
        self.system_prompt = """You are a professional Indian legal assistant with expertise in Indian laws and legal procedures. Your role is to:

1. Provide accurate information about Indian laws, including:
   - Constitutional Law
   - Civil Law
   - Criminal Law
   - Family Law
   - Property Law
   - Corporate Law
   - Labor Law
   - Consumer Protection Laws
   - Cyber Laws

2. Guide users through Indian legal processes and procedures
3. Explain relevant sections of Indian legal codes and statutes
4. Provide information about Indian courts and their jurisdictions
5. Explain fundamental rights and duties under the Indian Constitution

Please maintain a professional, authoritative tone while being clear and accessible. When discussing laws, cite relevant sections and precedents where appropriate. Focus on providing practical, actionable information while being mindful of jurisdictional variations across different states in India.

Please be clear, professional, and ethical in your responses."""
        
        self.fact_checker_prompt = """You are a legal fact-checker specializing in Indian law. Your role is to:
1. Verify the accuracy of legal information provided
2. Check for any factual errors or misstatements
3. Ensure citations and references are correct
4. Verify the applicability of laws across different states
5. Confirm the currency of legal information

If you find any errors, provide corrections with proper citations. If the information is accurate, confirm its correctness."""
        
        self.conversation_history = []
        self.max_history = 5
        self.disclaimer_shown = False
        self.observatory_log = []
        self.observatory_mode = False

    def log_to_observatory(self, stage, content):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = {
            "timestamp": timestamp,
            "stage": stage,
            "content": content
        }
        self.observatory_log.append(log_entry)
        
        if self.observatory_mode:
            print(f"\n=== Observatory Log ===")
            print(f"Time: {timestamp}")
            print(f"Stage: {stage}")
            print(f"Content: {content}")
            print("=" * 30)

    def get_response(self, user_input):
        # Add user input to conversation history
        self.conversation_history.append(f"User: {user_input}")
        self.log_to_observatory("User Input", user_input)
        
        # Create conversation context from history
        conversation_context = "\n".join(self.conversation_history[-self.max_history:])
        
        # Only include disclaimers in the first message
        if not self.disclaimer_shown:
            prompt = f"{self.system_prompt}\n\nIMPORTANT DISCLAIMERS:\n- This is not a substitute for professional legal advice\n- Always consult with a qualified Indian attorney for specific legal matters\n- Information provided is general in nature and may vary by state\n- No attorney-client relationship is created through this interaction\n- Laws and procedures may vary across different states in India\n\nPrevious conversation:\n{conversation_context}\nAssistant:"
            self.disclaimer_shown = True
        else:
            prompt = f"{self.system_prompt}\n\nPrevious conversation:\n{conversation_context}\nAssistant:"
        
        # Get initial response from primary model
        data = {
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        }
        
        try:
            response = requests.post(self.base_url, json=data)
            response.raise_for_status()
            initial_response = response.json()["response"]
            self.log_to_observatory("Primary Response", initial_response)
            
            # Fact checking with second model
            fact_check_prompt = f"{self.fact_checker_prompt}\n\nPlease verify the following legal information:\n\n{initial_response}\n\nFact Checker:"
            fact_check_data = {
                "model": "llama3.2",
                "prompt": fact_check_prompt,
                "stream": False
            }
            
            fact_check_response = requests.post(self.base_url, json=fact_check_data)
            fact_check_response.raise_for_status()
            fact_check_result = fact_check_response.json()["response"]
            self.log_to_observatory("Fact Check", fact_check_result)
            
            # Add both responses to conversation history
            self.conversation_history.append(f"Assistant: {initial_response}")
            self.conversation_history.append(f"Fact Checker: {fact_check_result}")
            
            return initial_response, fact_check_result
            
        except Exception as e:
            error_msg = f"Error: {str(e)}"
            self.log_to_observatory("Error", error_msg)
            return error_msg, None

    def clear_history(self):
        """Clear the conversation history"""
        self.conversation_history = []
        self.disclaimer_shown = False
        self.log_to_observatory("System", "Conversation history cleared")

    def toggle_observatory(self):
        """Toggle observatory mode"""
        self.observatory_mode = not self.observatory_mode
        status = "enabled" if self.observatory_mode else "disabled"
        self.log_to_observatory("System", f"Observatory mode {status}")

    def save_observatory_log(self):
        """Save observatory log to file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"legal_assistant_log_{timestamp}.json"
        
        with open(filename, 'w') as f:
            json.dump(self.observatory_log, f, indent=2)
        
        return filename

def main():
    assistant = LegalAssistant()
    print("\n=== Indian Legal Assistant ===")
    print("Type 'quit' to exit")
    print("Type 'clear' to clear conversation history")
    print("Type 'observatory' to toggle observatory mode")
    print("Type 'save' to save observatory log")
    print("DISCLAIMER: This is not a substitute for professional legal advice.")
    print("=" * 30 + "\n")
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() == 'quit':
            print("\nThank you for using the Indian Legal Assistant. Goodbye!")
            break
        elif user_input.lower() == 'clear':
            assistant.clear_history()
            print("\nConversation history cleared.")
            continue
        elif user_input.lower() == 'observatory':
            assistant.toggle_observatory()
            print(f"\nObservatory mode {'enabled' if assistant.observatory_mode else 'disabled'}")
            continue
        elif user_input.lower() == 'save':
            filename = assistant.save_observatory_log()
            print(f"\nObservatory log saved to {filename}")
            continue
            
        response, fact_check = assistant.get_response(user_input)
        print("\nAssistant:", response)
        if fact_check:
            print("\nFact Check:", fact_check)

if __name__ == "__main__":
    main()
