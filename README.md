# AI Research Assistant - Multi-Agent System

## Overview
The **AI Research Assistant** is an advanced multi-agent system designed to assist academic researchers in the task of research paper management. By leveraging the power of AI, this tool automates the process of identifying trending research topics, summarizing academic papers, and writing structured literature reviews. This system employs **Google Gemini 1.5** and utilizes multiple specialized AI agents, each responsible for a distinct task, creating an efficient and seamless research workflow.

## Problem Statement
Conducting academic research involves managing large volumes of information: finding relevant papers, summarizing them, and synthesizing them into coherent literature reviews. These tasks are repetitive and time-consuming, often taking valuable time away from deep analysis and original thought. The **AI Research Assistant** aims to solve this problem by automating the identification of trending topics, summarization of research papers, and the writing of literature reviews, helping researchers focus more on high-level tasks.

### Why Multi-Agent Systems?
Multi-agent systems offer significant benefits in complex tasks like research automation:
- **Specialization**: Each agent specializes in a specific task such as summarization, topic generation, or writing.
- **Collaboration**: The agents collaborate seamlessly to produce a comprehensive research workflow, ensuring higher efficiency and more accurate outcomes.
- **Independence**: Each agent operates independently within its scope, yet integrates with the other agents for an end-to-end solution.

---

## Project Description
The project consists of three AI-powered agents, each playing a key role in the research process:

### 1. Topic Agent
The **Topic Agent** generates trending research topics within a given domain, enabling researchers to stay up-to-date with cutting-edge trends. By querying **Google Gemini**, the agent returns a list of relevant topics with a brief explanation for each, tailored to the specified domain.

#### Example Output:

Trending Topics in AI for Education:

Adaptive Learning Systems: AI's role in personalizing education.

AI for Grading: Automating and enhancing assessment practices.

Intelligent Tutoring Systems: Improving learning through AI-powered tutoring.

### 2. Summary Agent
Once the topics are selected, the **Summary Agent** condenses research abstracts into concise summaries. This agent works by summarizing key information from the abstracts of academic papers, helping researchers get the gist of the paper without reading the full text.

#### Example Output:

Summary: AI for Adaptive Learning
This paper explores AI's role in adaptive learning, which personalizes educational experiences based on individual learner data. The study shows that adaptive learning systems lead to higher student engagement and performance.


### 3. Writer Agent
The **Writer Agent** integrates the topic summaries and paper abstracts to generate a comprehensive **Literature Review**. This agent combines the information to form a coherent narrative, summarizing the key findings from the selected papers and providing an in-depth review of the research topic.

#### Example Output:
Literature Review on AI in Education:
AI's impact on education is most notable in adaptive learning systems, which tailor educational content based on students' individual learning preferences. These systems have been shown to improve engagement and academic outcomes, and are being increasingly adopted in modern classrooms...


---

## Technologies and Tools Used
- **Google Generative AI**: For the core task of generating research topics, summarizing abstracts, and drafting literature reviews. Specifically, **Google Gemini 1.5** is utilized for content generation.
- **python-dotenv**: For securely managing the environment variables, such as the Google API key, which ensures proper integration with the Gemini API.
- **Flask/Streamlit** (Optional): For building a user-friendly interface for interacting with the system (if you choose to deploy with a UI).
- **GitHub Actions** (Optional): For continuous integration and deployment workflows.

### Setup Instructions:
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/ai-research-assistant.git

2. **Install dependencies:**:
   ```bash
   pip install -r requirements.txt

3. **Set up the Google API key**:
Create a .env file and add your API key:
```bash
GOOGLE_API_KEY=your_google_api_key_here




