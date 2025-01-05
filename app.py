from flask import Flask, request
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel

# Load .env file
load_dotenv()

client = OpenAI()

def generate_user_message(city: str, state: str, participants: int, duration: int, max_price: int, number_of_activities = 1):
    message = f"""Give me {number_of_activities} {"activities" if number_of_activities > 1 else "activity"} that I can do in {city}, {state} that consists of {participants} {"person" if participants == 1 else "people"} for a maximum of {duration} {"hour" if duration == 1 else "hours"} that costs less than ${max_price} per person.
    For each activity please provide a title (less than 5 words), description (less then 20 words), duration (in hours), cost (USD), name of location, the address for the activity, and a website URL for the activity."""
    return message

developer_message = "You are an expert event planner."
user_message1 = generate_user_message("Baltimore", "Maryland", 2, 2, 20)
user_message2 = generate_user_message("Denver", "Colorado", 2, 2, 50, 3)
user_message3 = generate_user_message("York", "Pennsylvania", 2, 2, 50, 3)


# Pydantic Address class for OpenAI structured output
class Address(BaseModel):
    street_address: str
    city: str
    state: str
    postal_code: int
    country: str

# Pydantic Activity class for OpenAI structured output 
class Activity(BaseModel):
    title : str
    description : str
    duration : int
    cost : float
    locationName : str
    address : Address
    websiteUrl : str 

completion = client.beta.chat.completions.parse(
model= "gpt-4o-mini",
messages= [
    {"role" : "developer", "content" : developer_message},
    {"role" : "user", "content": user_message1}
],
response_format= Activity
)
print(completion)
activities = completion.choices[0].message.parsed
print(activities)

# app = Flask(__name__)

# @app.route('/')
# def hello():
#     return 'Hello, World!'


# @app.post('/openai')
# def callChatGPT():

#     clientData = request.get_json()
#     print(clientData)

#     activity1 = generateActivities()
#     activity2 = generateActivities()
#     activity3 = generateActivities()
#     activity4 = generateActivities()
#     activity5 = generateActivities()
#     activity6 = generateActivities()
#     activity7 = generateActivities()
#     activity8 = generateActivities()
#     activity9 = generateActivities()
#     activity10 = generateActivities()

#     generated_activities = [activity1, activity2, activity3, activity4, activity5, activity6, activity7, activity8, activity9, activity10]

#     return generated_activities

# def generateActivities():
    # return {
    #     "id": uuid.uuid4(),
    #     "title" : "Explore the Baltimore Basilica",
    #     "description" : "Visit the Basilica of the National Shrine of the Assumption of the Blessed Virgin Mary, the first metropolitan cathedral built in the United States. Marvel at its stunning neoclassical architecture, historic artifacts, and serene interior. Self-guided tours allow you to explore at your own pace, making it a peaceful yet enriching experience.",
    #     "duration" : 2,
    #     "cost" : 0,
    #     "isFavorite" : False,
    #     "locationName" : "Basilica of the National Shrine of the Assumption of the Blessed Virgin Mary",
    #     "address" : "409 Cathedral Street, Baltimore, MD 21201",
    #     "websiteUrl" : "https://www.americasfirstcathedral.org/"
    # }