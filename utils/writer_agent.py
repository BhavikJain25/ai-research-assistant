from utils.gemini_api import ask_gemini

def writer_agent(topic_summary, summaries):
    prompt = f"""Write a 300-word literature review using the following:

Topic Summary:
{topic_summary}

Summaries of 3 papers:
{summaries}
"""
    return ask_gemini(prompt)
