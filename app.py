from flask import Flask, request
from dotenv import load_dotenv
from openai import OpenAI
from openai_service import OpenAIService

# Load .env file
load_dotenv()

# Create OpenAI client
client = OpenAI()

app = Flask(__name__)

@app.post('/activities')
def callChatGPT():

    clientData = request.get_json()

    city = clientData["city"]
    state = clientData["state"]
    max_duration = clientData["maxDuration"]
    max_price = clientData["maxPrice"]
    number_of_participants = clientData["numberOfParticipants"]
    number_of_activities = clientData["numberOfActivities"]

    user_message = OpenAIService.generate_user_message(city, state, max_duration, max_price, number_of_participants, number_of_activities)
    completion = OpenAIService.generate_chat_completion(user_message, client)
    activities = completion.choices[0].message.parsed

    # return "Generated Activities"
    return activities.model_dump()
