# it Perfrom Type Validation
# it can be converted to json and dict

from pydantic import BaseModel, EmailStr, Field  
from typing import Optional


class Student(BaseModel):
    name: str = Field(
        default="Anonymous",
        description="Name of the student"
    ) 
    age: Optional[int] = Field(
        default=None,
        description="Age of the student"
    )
    email: EmailStr = Field(
        ...,
        description="Valid email address of the student"
    ) 
    cgpa: float = Field(
        ge=0,
        lt=10,
        description="Student score in the academic journey"
    )
    height:Optional[str]=Field(description="height in cm")