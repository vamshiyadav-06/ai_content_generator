from fastapi import FastAPI, HTTPException
from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI()


from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get API key from .env
groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ_API_KEY not found in environment variables")

# Create Groq client
client = Groq(api_key=groq_api_key)


@app.get("/")
def home():
    return {"message": "AI Content Generator API is running"}


@app.post("/generate")
def generate_content(
    topic: str,
    technology: str,
    content_type: str,
    tone: str
):
    try:
        prompt = f"""
Generate a {content_type}

Topic: {topic}
Technology: {technology}
Tone: {tone}

Make it engaging and well-structured.
"""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        generated_content = response.choices[0].message.content

        return {
            "content": generated_content
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
    


