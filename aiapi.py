from openai import OpenAI
import openai
import config

openai.api_key = config.DevelopmentConfig.OPENAI_KEY
client = OpenAI(api_key=openai.api_key)  # Pass the api_key when initializing the client

def generateChatResponse(prompt):
    messages=[]
    messages.append({"role": "developer", "content": "You are a helpful assistant."})

    question = {}
    question['role'] = 'user'
    question['content'] = prompt
    messages.append(question)
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    #print(response.choices[0].message)
    try:
        answer = response.choices[0].message.content.replace('\n', '<br>')
    except:
        answer = "You beat the AI, try a different question"

    return answer
