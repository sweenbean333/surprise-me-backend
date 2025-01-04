from flask import Flask, request
from dotenv import load_dotenv
import os
import uuid

# Load .env file
load_dotenv()

api_key = os.getenv("API_KEY")

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'


@app.post('/openai')
def callChatGPT():

    clientData = request.get_json()
    print(clientData)

    activity1 = generateActivities()
    activity2 = generateActivities()
    activity3 = generateActivities()
    activity4 = generateActivities()
    activity5 = generateActivities()
    activity6 = generateActivities()
    activity7 = generateActivities()
    activity8 = generateActivities()
    activity9 = generateActivities()
    activity10 = generateActivities()

    generated_activities = [activity1, activity2, activity3, activity4, activity5, activity6, activity7, activity8, activity9, activity10]

    return generated_activities

def generateActivities():
    return {
        "id": uuid.uuid4(),
        "title" : "Explore the Baltimore Basilica",
        "description" : "Visit the Basilica of the National Shrine of the Assumption of the Blessed Virgin Mary, the first metropolitan cathedral built in the United States. Marvel at its stunning neoclassical architecture, historic artifacts, and serene interior. Self-guided tours allow you to explore at your own pace, making it a peaceful yet enriching experience.",
        "duration" : 2,
        "cost" : 0,
        "isFavorite" : False,
        "locationName" : "Basilica of the National Shrine of the Assumption of the Blessed Virgin Mary",
        "address" : "409 Cathedral Street, Baltimore, MD 21201",
        "websiteUrl" : "https://www.americasfirstcathedral.org/"
    }