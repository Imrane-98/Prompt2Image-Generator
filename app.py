import gradio as gr
import requests
import io
import os
from PIL import Image

# Load the API key from an environment variable
API_KEY = os.getenv("HF_API_KEY")
if API_KEY is None:
    raise ValueError("Please set the HF_API_KEY environment variable with your Hugging Face API key.")

API_URL = "https://router.huggingface.co/hf-inference/v1"
headers = {"Authorization": API_KEY}

def query(payload):
    response = requests.post(API_URL, json=payload, headers=headers)
    return response.content

def generate_image(prompt):
    image_bytes = query({"inputs": prompt})
    
    # Debug: Print the first 20 bytes
    print("First 20 bytes of the response:", image_bytes[:20])
    
    # Save the bytes to a file for inspection (optional)
    with open("debug_image.jpg", "wb") as f:
        f.write(image_bytes)
    print("Saved image bytes to debug_image.jpg")
    
    try:
        image = Image.open(io.BytesIO(image_bytes))
    except Exception as e:
        print("Error opening image:", e)
        raise e
    return image

#create the Gradio interface
demo = gr.Interface(
    fn=generate_image,
    inputs=gr.Textbox(placeholder="Enter a prompt"),
    outputs=gr.Image(label="Generated Image"),
    title="Prompt-to-Image Generator",
    description="Generate images using Hugging Face's CLIP and Stable Diffusion"
)

demo.launch(share=True)
