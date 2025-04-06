import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load the environment variable
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Set API key
genai.configure(api_key=api_key)

# Global user context
user_name = ""
user_goal = ""

# prompt builder
def construct_prompt(user_query):
    base_intro = "You are WealthGenie — an intelligent and friendly AI financial literacy assistant for Indian users."

    personalized_context = f"The user's name is {user_name}. "
    if user_goal:
        personalized_context += f"They have a financial goal: '{user_goal}'. "

    final_prompt = f"""
{base_intro}

{personalized_context}They asked: "{user_query}"

If the user asks a personal query (e.g., I am 24 years old, earning ₹30k/month...), use the data to create a 3-step action plan and one caution. 
You can assume the user might be a beginner and needs guidance.

Respond in a simplified, engaging, and non-technical tone that even a beginner can understand. Use markdown formatting for readability and end with a tip or myth-busting fact.
"""
    return final_prompt

# response using Gemini
def generate():
    user_input = input(f"\n💬 What would you like to ask, {user_name}? ").strip()

    if not user_input:
        print("❗ Please enter something meaningful.")
        return

    full_prompt = construct_prompt(user_input)

    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")
        response = model.generate_content(full_prompt, stream=True)

        print("\n🔍 Generating WealthGenie's response...\n")
        for chunk in response:
            print(chunk.text, end="")

    except Exception as e:
        print(f"\n⚠️ Something went wrong: {str(e)}")

# Run the app in a loop
if __name__ == "__main__":
    print("👋 Welcome to WealthGenie — your smart financial guide!")

    user_name = input("👤 What's your name? ").strip().title()
    user_goal = input("🎯 Do you have a financial goal you'd like WealthGenie to consider? (Press Enter to skip): ").strip()

    while True:
        generate()
        again = input("\n\n❓ Do you want to ask another question? (yes/no): ").strip().lower()
        if again not in ["yes", "y"]:
            print(f"👋 Thank you for using WealthGenie, {user_name}. Stay financially smart!")
            break
