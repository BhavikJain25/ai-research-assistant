from utils.gemini_api import ask_gemini

def summary_agent(title, abstract):
    prompt = f"""Summarize the following research abstract in 100 words:

Title: {title}

Abstract: {abstract}
"""
    return ask_gemini(prompt)
