from pydantic import BaseModel
import activity

# Pydantic Activities class for OpenAI structured output
class Activities(BaseModel):
    activities : list[activity.Activity]