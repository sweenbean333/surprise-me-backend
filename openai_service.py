from openai import OpenAI
from activities import Activities

class OpenAIService :

    # Generate a User message for the OpenAI API based on data received from the user
    def generate_user_message(city: str, state: str, participants: int, duration: int, max_price: int, number_of_activities = 1):
        message = f"""Give me a list of {number_of_activities} {"different activities" if number_of_activities > 1 else "activity"} that I can do in {city}, {state} that consists of {participants} {"person" if participants == 1 else "people"} for a maximum of {duration} {"hour" if duration == 1 else "hours"} that costs no more than ${max_price} per person.For each activity please provide a title (less than 5 words), description (less then 20 words), duration (in hours), cost (USD), name of location, the address for the activity, and a website URL for the activity."""
        return message
    
    def generate_chat_completion(user_message: str, client: OpenAI):
        developer_message = "You are an expert event planner."
        completion = client.beta.chat.completions.parse(
            model= "gpt-4o-mini",
            messages= [
                {"role" : "developer", "content" : developer_message},
                {"role" : "user", "content": user_message},
            ],
            response_format= Activities
        )
        return completion