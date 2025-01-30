import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("AIzaSyA-eiYwlDQ3R2_gEY_rAV8whjfQXi0tPoQ")

genai.configure(api_key=GEMINI_API_KEY)

def ask_gemini(prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text

def analyze_image(image_path):
    model = genai.GenerativeModel("gemini-pro-vision")
    response = model.generate_content([{"image": open(image_path, "rb").read()}, "Describe this image"])
    return response.text
