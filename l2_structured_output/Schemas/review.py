# using Typed Dictionary
# Cons of using the Typed_dict is you can't apply type validation

from typing import TypedDict,Annotated,Optional,Literal

class Review(TypedDict):
    key_themes:Annotated[list[str],"List all Key Theme"]
    summary: Annotated[str,"A very brief summary of review"]
    sentiment: Annotated[Literal["pos","neg","neu"],"one word sentiment of review"]
    pros:Annotated[Optional[list[str]],"Write Dwon all Props of list"]
    cons:Annotated[Optional[list[str]],"Write Dwon all Props of list"]