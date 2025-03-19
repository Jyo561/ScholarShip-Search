import requests
import json,os
from dotenv import load_dotenv
import re

load_dotenv()
api_key = os.getenv("api_key")

def extract_html_from_gemini_response(response_json):
    """
    Extracts the HTML part from the Gemini AI response, handling variations.

    Args:
        response_json (dict): The JSON response from the Gemini AI.

    Returns:
        str: The extracted HTML content, or None if not found.
    """
    try:
        text_content = response_json['candidates'][0]['content']['parts'][0]['text']
        html_match = re.search(r'```(?:html)?\n(.*?)\n```', text_content, re.DOTALL)
        if html_match:
            return html_match.group(1).strip()
        else:
            return None
    except (KeyError, IndexError, TypeError):
        return None

def call_gemini_ai(prompt: str) -> str:
    # Replace with your actual API key
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{"parts": [{"text": f"{prompt}"}]}]
    }
    answer = ""
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        result = response.json()
        #print(json.dumps(result, indent=2)) #print nicely formatted json.
        answer = result
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    # Replace this with your actual Gemini AI integration
    return extract_html_from_gemini_response(answer)

def get_all_posts(caste: str, religion: str, converted: bool):
    prompt = f"Find scholarship available for a student with Caste: {caste}, Religion: {religion} "

    if converted is not None:
        prompt += f", Converted: {converted}"

    prompt += """. Provide a list of relevant scholarships. With links. Provide the answer in form of 
        <h1>Name of Scholarship</h1>
        <h3>Offered by: Name<h3>
        <h3>Description: Primarily for ST students, but worth investigating if provisions exist for individuals who have converted from SC and meet socio-economic conditions.</h3>
        <h3>Website: <a href="https://tribal.nic.in">tribal.nic.in</a>"""

    ai_response = call_gemini_ai(prompt)
    print(ai_response) 
    return ai_response


