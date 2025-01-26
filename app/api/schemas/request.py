from pydantic import BaseModel


class News(BaseModel):
    """
    Attributes:
        text (str): The text content of the news article that needs to be checked if it is fake or real.
    """

    text: str
