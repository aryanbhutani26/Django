import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load the environment variable
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Set API key
genai.configure(api_key=api_key)

# Prompt builder
def construct_prompt(user_query):
    return f"""
You are WealthGenie — an intelligent and friendly AI financial literacy assistant for Indian users.

The user input is: "{user_query}"

If the user asks a personal query (e.g., I am 24 years old, earning ₹30k/month...), use the data to create a 3-step action plan and one caution. You can assume the user might be a beginner and needs guidance.

Respond in a simplified, engaging, and non-technical tone that even a beginner can understand. Use markdown formatting for readability and end with a tip or myth-busting fact.
"""

# Response using Gemini
def generate():
    user_input = input("\n💬 Ask WealthGenie your financial query: ").strip()

    if not user_input:
        print("❗ Please enter something meaningful.")
        return

    full_prompt = construct_prompt(user_input)

    try:
        model = genai.GenerativeModel("gemini-2.5-pro-exp-03-25")

        print("\n🔍 Generating WealthGenie's response...\n")
        response = model.generate_content(full_prompt)

        print(response.text)

    except Exception as e:
        print(f"\n⚠️ Something went wrong: {str(e)}")

# Run the app in a loop
if __name__ == "__main__":
    while True:
        generate()
        again = input("\n\n❓ Do you want to ask another question? (yes/no): ").strip().lower()
        if again not in ["yes", "y"]:
            print("👋 Thank you for using WealthGenie. Stay financially smart!")
            break

