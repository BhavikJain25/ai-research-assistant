from utils.topic_agent import topic_agent
from utils.summary_agent import summary_agent
from utils.writer_agent import writer_agent

sample_abstract = """
AI is transforming education through personalized learning, intelligent tutoring, and automated grading. 
This paper explores adaptive learning systems and their impact on academic performance and teacher roles.
"""

print("=== AI Research Assistant (Gemini Version) ===")

domain = input("Enter your research domain (e.g., AI in Education): ")
topics = topic_agent(domain)
print("\n[TOPIC AGENT OUTPUT]:\n", topics)

print("\nSummarizing 3 sample papers...")
summary1 = summary_agent("AI for Adaptive Learning", sample_abstract)
summary2 = summary_agent("AI Grading Systems", sample_abstract)
summary3 = summary_agent("AI Tutors in Classrooms", sample_abstract)

print("\n[SUMMARY AGENT OUTPUT - Paper 1]:\n", summary1)
print("\n[SUMMARY AGENT OUTPUT - Paper 2]:\n", summary2)
print("\n[SUMMARY AGENT OUTPUT - Paper 3]:\n", summary3)

combined_summaries = f"1. {summary1}\n\n2. {summary2}\n\n3. {summary3}"
final_review = writer_agent(topics, combined_summaries)

print("\n[WRITER AGENT OUTPUT - Literature Review]:\n", final_review)
