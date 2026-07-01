from google import genai
from config import Config


client = genai.Client(api_key=Config.GEMINI_API_KEY)

response = client.models.generate_content(
    model=Config.CHAT_MODEL,
    contents="hey gimini what is css and tailwend "
)

print("=*" * 80)
print(response.text)
print("=*" * 80)