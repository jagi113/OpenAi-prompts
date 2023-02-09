OpenAi Prompts
is a simple app that sends users prompts to chatGPT and returns its answers.
After each answer app asks a user whether he wants to give another question.

Installation guide:

1. Create folder for the app and open it in the terminal
2. Create and activate a virtual environment
   (for more info: https://docs.python.org/3/library/venv.html )
3. Copy app files into your folder
4. Install dependencies (in the terminal - run: pip3 install -r requirements.txt )
5. In the app folder create a file ".env", open it and copy your OPENAI_API_KEY in there:
   OPENAI_API_KEY="copy_your_api_key_in_here"
6. To run app, in the terminal run:
   python openai_prompts.py
