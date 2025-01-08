from pydantic import BaseModel

# Pydantic Address class for OpenAI structured output
class Address(BaseModel):
    street_address: str
    city: str
    state: str
    postal_code: int
    country: str