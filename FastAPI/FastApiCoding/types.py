from pydantic import BaseModel, Field
from typing import List, Dict, Optional


# validations
class validations(BaseModel):
    name: Optional[str] = None
    age: Optional[str] = None
