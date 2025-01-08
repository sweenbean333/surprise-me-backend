from pydantic import BaseModel
import address

# Pydantic Activity class for OpenAI structured output 
class Activity(BaseModel):
    title : str
    description : str
    duration : int
    cost : float
    locationName : str
    address : address.Address
    websiteUrl : str 
