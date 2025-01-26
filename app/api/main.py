from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from internal.models import Model
from schemas.request import News


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/detect-news")
async def detect(news: News):
    """
    Detects fake news.

    Args:
        news (News): An instance of the News class containing the text to be analyzed.

    Returns:
        dict: A dictionary containing the original text and the prediction result.
    """

    model = Model()

    return {
        "prediction": model.predict(news.text),
        "probabilities": model.predict_prob(news.text),
    }
