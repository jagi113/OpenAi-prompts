# Loading dependencies for environment variables (we want to keep openAi-API-key hidden)
from dotenv import load_dotenv
import os

# Loading openai library
import openai

# Loading .env file with stored environment variables,
# getting from it openAi-API-key value and assigning it to openai
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = API_KEY

# Defining function for sending prompt to openai API and receiving a response as completion.
# Response provides various data as dictionary, but the app cares only for a text provided.
# From given response it chooses value of "choices" key, which is a list.
# From that list it takes first element with index 0 and grabs value of its "text" key.
# Since response starts with two new lines, the app gets rid of them.
def chatting(prompt):
    completion = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0,
    )
    return completion.choices[0].text.replace("\n\n", "", 1)


# Function that asks a user whether he wants to ask another question.
# Returns "continue" or "break".
def anotherquestion():
    another = str(
        input("Do you want to ask another question? (yes/no) >> ").lower().strip()
    )
    if another == "yes":
        return "continue"
    elif another == "no":
        return "break"
    else:
        anotherquestion()


# App cycle that allows a user to ask chatGPT questions until he decides to end
# the conversation.
while True:
    prompt = str(input("Enter your question: ")).strip()
    response = chatting(prompt)
    print(f"OpenAI: {response}")

    if anotherquestion() == "break":
        break
    else:
        continue
