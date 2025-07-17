from utils.gemini_api import ask_gemini

def topic_agent(domain):
    prompt = f"List 3 trending research topics in {domain}. Provide a 1-line explanation for each."
    return ask_gemini(prompt)
