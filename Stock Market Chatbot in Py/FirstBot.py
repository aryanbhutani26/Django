
# genai.configure(api_key="AIzaSyAKFNYPNWvZ1lefBXWYXzSbIBGjzqPD1DM")
# Abhi Gemini Key yahi p paste kri h taaki tum log bhi use kr sako
# ye first and free model h ise first page p lgana h


import base64
import os
from google import genai
from google.genai import types

def generate():
    # Prompt the user for their question
    user_question = input("Ask WealthGenie your question: ")

    # Initialize the Gemini client
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-2.5-pro-exp-03-25"

    # Prepare the contents for the request
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="What’s the difference between SIP and FD?"),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""
SIP (Systematic Investment Plan) and FD (Fixed Deposit) are both popular financial instruments in India, but they serve different purposes and come with distinct features:

1. Investment Type:
- SIP: It's a way to invest in mutual funds periodically (usually monthly). It allows investors to invest a fixed amount regularly into mutual fund schemes.
- FD: A fixed deposit is a lump-sum investment in a bank or financial institution for a fixed tenure at a predetermined interest rate.

2. Returns:
- SIP: Returns are market-linked and vary depending on the performance of the underlying mutual fund scheme. Returns can be higher in the long term, but they also carry some risk.
- FD: Returns are fixed and guaranteed. The interest rate is locked in when you invest and is not affected by market fluctuations.

3. Risk:
- SIP: Subject to market risks as they are linked to equity or debt markets depending on the fund type.
- FD: Very low-risk. Backed by banks and typically insured up to a certain amount.

4. Liquidity:
- SIP: You can withdraw anytime (if it’s not a lock-in ELSS fund). However, for optimal benefits, long-term holding is advised.
- FD: Premature withdrawal is possible but may come with a penalty.

5. Taxation:
- SIP: Gains from equity mutual funds held for more than 1 year are taxed at 10% (LTCG) beyond ₹1 lakh. Short-term gains are taxed at 15%.
- FD: Interest earned is fully taxable as per your income tax slab.

6. Flexibility:
- SIP: Highly flexible. You can start/stop/change amounts anytime.
- FD: Less flexible. Once booked, you cannot change the tenure or interest rate without breaking the FD.

In summary:
- SIPs are better suited for long-term wealth creation and beating inflation.
- FDs are better for capital protection and guaranteed returns with low risk.

The best choice depends on your financial goals, risk tolerance, and investment horizon.
""")
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=user_question),
            ],
        ),
    ]

    tools = [
        types.Tool(google_search=types.GoogleSearch())
    ]

    generate_content_config = types.GenerateContentConfig(
        temperature=0.35,
        top_p=1,
        safety_settings=[
            types.SafetySetting(category="HARM_CATEGORY_HARASSMENT", threshold="BLOCK_LOW_AND_ABOVE"),
            types.SafetySetting(category="HARM_CATEGORY_HATE_SPEECH", threshold="BLOCK_ONLY_HIGH"),
            types.SafetySetting(category="HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold="BLOCK_LOW_AND_ABOVE"),
            types.SafetySetting(category="HARM_CATEGORY_DANGEROUS_CONTENT", threshold="BLOCK_LOW_AND_ABOVE"),
        ],
        tools=tools,
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(text="""
You are WealthGenie — an intelligent and friendly AI financial literacy assistant for Indian users. You are designed to simplify complex financial topics and empower users with practical knowledge.

Tone: Friendly, Motivational, Clear.
Personality: Smart & helpful mentor who explains even the most complex financial terms like a friend would.
Audience: Young adults, students, and early jobbers in India seeking to improve their financial knowledge.

Always answer in simple, non-jargon language unless specifically asked to explain technical terms. If the user asks a basic or general query like "What is a mutual fund?" or "Best ways to save money as a student", give examples with relatable Indian context (e.g., chai prices, tuition fees, pocket money, UPI apps, etc.).

Include emojis when helpful (not overused) and make the answer engaging like a chat, not a Wikipedia page.

If the user asks about stocks, insurance, loans, taxes, SIPs, FDs, or any financial concept — give clear pros/cons and when it’s right to use.

If you're unsure or the question is unrelated to finance, reply: "I'm designed to help you with finance-related topics 😊. Try asking something about savings, investing, or managing money!"

NEVER respond with: "As an AI language model...".

If the user asks for emotional support, respond with kindness and redirect them to self-care or support.
"""),
        ],
    )

    # Stream the output
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

if __name__ == "__main__":
    generate()
