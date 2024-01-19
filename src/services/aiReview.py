import os
from openai import OpenAI

# load te .env file for the API key 
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

def generate_review(review):
    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
                {"role": "user", "content": review}
            ]
        )
        response_message = completion["choices"][0]["message"]["content"]
    except Exception as e:
        print("Some error occurred::", e)
        response_message = "sad"

    if response_message == "happy":
        return "Thanks for shopping with us, come back soon!!!"
    return "Sorry to hear about your experience, here's a coupon for 20%, type GTP20 to use"
