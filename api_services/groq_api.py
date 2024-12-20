from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()

client = Groq( api_key=os.environ.get("GROQ_API_KEY") )


def get_city_from_summary(summary, country):
    prompt = f"""
        You are an advanced language model trained to analyze text descriptions. 
        Your task is to extract the name of the city or the closest city or a central city where an event occurred based on the provided description and country. 
        If it is impossible to determine the city, return "Unknown". 
        Here is the input:
        Description: "{summary}"
        Country: "{country}"
        Your response should be in the following format:
        City: <city_name> !!
        don't explain your answer just answer as the provided format
        and pay attention to add space and !! (as the format) after you finished writing the name of the city
        """
    try:
        chat_completion = client.chat.completions.create(
            messages=[ {"role": "user","content": prompt,} ],
            model="llama3-8b-8192",
        )
        answer = chat_completion.choices[0].message.content.strip()
        print(answer)
        if "City:" in answer:
            city = answer.split("City:")[1].strip()
            city = city.split("!!")[0].strip()
            return city
        else:
            return "Unknown"
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Unknown"








