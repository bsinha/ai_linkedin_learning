import os
from openai import OpenAI

# load the .env file it is a must
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
#client = OpenAI(
#   api_key=os.environ.get("OPENAI_API_KEY"),
#)

while True:
  # Taking user input
  userInput = input("Enter a phrase and we'll tell you its happy or sad \n")

  if(userInput == "exit" or userInput == "quit"):
    break;
  try:
    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "You are a sentiment classification bot, print out if the user is happy or sad."},
        {"role": "user", "content": userInput}
      ]
    )

    print(completion.choices[0].message)
  except Exception as e:
    print(e)
