from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()

generator = pipeline(
    "text-generation",
    model="gpt2",     
    device=-1         
)                     

@app.get("/get_motivation")
async def get_motivation():
    prompt = (
        "Please generate 5 motivational quotes about working out and eating healthy. "
        "Return them as a numbered list."                                        
    )

    output = generator(prompt, max_length=200, num_return_sequences=1)
    
    text = output[0]['generated_text']

    quotes = [line.strip() for line in text.split("\n") if line.strip()]
    return quotes
