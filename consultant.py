import openai
import keys

'''
Financial Consultant 
- Take inputs of financial advice
- Create outlets using specific prompts
'''

MAX_TOKENS = 100
TEMPERATURE = 1
MODEL = "gpt-3.5-turbo"


openai.api_key = keys.API_KEY
user_prompt = "An anonymous individual has several gigabytes of pirates movies on his computer. What are you going to do you buffoon?"

def generate_fresponse(prompt):
    response = openai.ChatCompletion.create(
            model=MODEL,
            temperature=1,
            max_tokens=MAX_TOKENS,
            messages = [{"role":"user", "content": prompt}]
        )

    f_response = response["choices"][0]["message"]["content"]
    return f_response

print(generate_fresponse(user_prompt))