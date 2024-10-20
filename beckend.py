import openai 

import os

from dotenv_vault import load_dotenv
load_dotenv()

key = os.getenv("API_KEY") # API key from OpenAI
client = openai.OpenAI(api_key=key)

# Function to call the GPT model
def perform_response(input):
    prompt = """Tu sei un assistente di studio francese.
    L'utente ha bisogno che tu lo aiuti a studiare il francese"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": f"{prompt}"},
            {"role": "user", "content": f"- USER QUESTION:{input} \n\n"}
        ],
        temperature=0.2
    )
    answer = response.choices[0].message.content
    return answer

# Function to call the GPT model
def perform_response_grammatica(input):
    with open("grammatica.txt", "r") as g:
        file = g.read()
    prompt = """Tu sei un assistente di studio francese.
    L'utente ha bisogno che tu lo aiuti a studiare il francese"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": f"{prompt}"},
            {"role": "user", "content": f"- USER QUESTION:{input} \n\n-GRAMMATICA: {file}"}
        ],
        temperature=0.2
    )
    answer = response.choices[0].message.content
    return answer

# Function to call the GPT model
def perform_response_vocaboli(input):
    with open("vocaboli.txt", "r") as v:
        file = v.read()
    prompt = """Quando lo studente ti chiederà di fare un quiz sui vocaboli tu scegli dei vocaboli e fagli dei quiz.
    Quando ti chiede spiegazioni o chiarimenti, sii a sua disposizione per farlo.
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": f"{prompt}"},
            {"role": "user", "content": f"- USER QUESTION:{input} \n\n-VOCABOLI: {file}"}
        ],
        temperature=0.2
    )
    answer = response.choices[0].message.content
    return answer