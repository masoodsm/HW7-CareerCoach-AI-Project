# HW7-CareerCoach-AI-Project

📌**Project Overview**

***Assignment 6: Build App  “ AI Travel Guide”***

This project is an AI-powered Travel Planning application built using **Python**, **Streamlit**, and the **OpenAI API**.
It generates a **day-by-day travel itinerary** based on user preferences and exports the plan as a **professionally formatted PDF**.

❓**Problem Statement**

This project solves the problem of manual travel planning by generating personalized, day-by-day travel itineraries based on user inputs such as destination, number of days, interests, and preferences. It automates the creation of travel plans, including recommendations for activities, meals, and accommodations, saving users time and enhancing their travel experience.

🤖 **Relation to AI and AI-Assisted Workflows**

The project leverages AI, specifically OpenAI's GPT language model, to generate customized travel plans by interpreting natural language inputs. This showcases AI-assisted workflows where AI augments human tasks—here, by synthesizing relevant and tailored travel information dynamically. It exemplifies how AI can support decision-making and creative planning through natural language understanding and content generation.


✨ **Features**
- Generate a multi-day travel itinerary
- Each day includes:
  - Morning
  - Lunch
  - Afternoon
  - Dinner
  - Activities 
- Family-friendly and non-repetitive activities
- Clean, structured output
- Downloadable PDF travel plan
- Simple, user-friendly Streamlit UI
  
🧠 **How the AI/Code Works**

**Workflow**

<img width="352" height="647" alt="image" src="https://github.com/user-attachments/assets/837b9b06-11fd-4033-af36-61cefed863bb" />
    
🛠 **Tech Stack**
- Python
- Streamlit
- OpenAI API
- ReportLab (PDF generation)
- dotenv (.env for environment variables)

▶️**How to Run & Use**



**Prerequisites**

Python 3.6.0 or higher

pip (Python package installer)

**Project Structure** 

<img width="551" height="207" alt="image" src="https://github.com/user-attachments/assets/1ef0e91f-e1e8-402f-ae95-8fd537ebb7cb" />

**1.** **Clone the repository** 

*git clone https://github.com/your-username/travel-plan-ai.git*

**2.** **Create Virual Environment**

*python -m venv venv*

**3.** **Install dependencies**

*pip install -r requirements.txt*

**4.** **Upgrade pip**

*python -m pip install --upgrade pip*

**5.** **Create a .env** 

***This file stays local and is NOT uploaded to GitHub***

*OPENAI_API_KEY=your_openai_api_key_here*

File in the project root folder and add your OpenAI API key:

**6.** **-source venv/bin/activate**-

 *.venv\Scripts\activate.ps1*

*python -m streamlit run main.py*

💻**How to use the the Application**

**Enter Destination**
•	Example: San Francisco, CA

**Select Number of Days**
Choose how many days you plan to travel (e.g., 3 days)

**Enter Special Interests** (eg Museums, nature, family-friendly activities)

**Enter Preferences** (e.g Kids friendly, less walking) These act as guardrails for the AI.

<img width="606" height="412" alt="image" src="https://github.com/user-attachments/assets/97c4fe83-a9e2-4d0f-9601-071ac4aa620c" />


**OUTPUT**

🧭**Click “Generate Travel Plan”**

**Open Browser**

***http://localhost:8501***

The AI will generate a day-by-day itinerary.
•  Each day includes:
  •	 Morning
  •	Lunch
  •	Afternoon
  •	Evening Activity
  •	Dinner

📅**Review the Travel Itinerary**
•	The plan is displayed directly on the screen.
•	You can scroll and review all days.

📄**Download the PDF**
***Click “Download Travel Plan PDF”***

A professionally formatted PDF is generated with:

•	Clear day sections

•	Proper text wrapping

•	No text cutoff across pages

⚙️**What the AI Is Doing** 

***Uses OpenAI’s language model to*:**

•	Understand travel preferences

•	Generate structured daily plans

•	Ensure completeness (morning, lunch, evening, etc.)

•  Automatically fixes missing sections if the AI response is incomplete.

•  Formats output for both screen display and PDF export.

🔄**Resetting the Form**

•	If you want to start over or clear all inputs and outputs, click the Reset Form button.

•	This will clear your previous entries and generated plans so you can enter new travel preferences.

🛠️**Troubleshooting**

**.** **API Key Issues**
Ensure your .env file contains a valid OpenAI API key. Check for typos and make sure .env is loaded correctly.

**.** **Module Not Found Errors**

Run *pip install -r requirements.txt to install all dependencies*.

**.** **Streamlit Not Launching**

Verify Streamlit is installed (pip show streamlit). Use streamlit run your_script.py to start the app.

**.** **PDF Not Generating Properly**

Check if ReportLab is installed and your environment has write permissions to save files.

⚡**Performance**

**.** The app responds quickly to user inputs with itinerary generation typically taking a few seconds, depending on API response time.

**.** PDF generation is fast and efficient, producing well-formatted travel plans without noticeable delay.

**.** Streamlit’s lightweight framework ensures smooth interaction on most modern devices.

**.** Performance may vary based on internet speed and OpenAI API latency.

📚**Learning Outcomes**

**.** Integrating AI multiprompt workflows with Python using the OpenAI API

**.** Managing prompt engineering techniques to improve AI output relevance and coherence

**.** Building interactive user interfaces with Streamlit

**.** Handling environment variables securely with .env files

**.** Generating professional PDFs programmatically using ReportLab

🌟**Potential Features** 

**-** **Personalized Recommendations:**

Integrate user preferences like budget, dietary restrictions, or mobility needs to tailor the itinerary.

**-** **Real-Time Data Integration:**

Pull live data such as weather forecasts, local events, or COVID-19 restrictions for more accurate plans.

**-** **Map Visualization:**

Add interactive maps showing travel routes, landmarks, and distances between stops.

**-** **Multi-Destination Planning:**

Support itineraries covering multiple cities or countries in one trip.

**-** **Accommodation & Transport Booking:**

Link to booking platforms for hotels, flights, or local transport.

**-** **Multi-language Support:**

Use AI to generate plans in different languages for international users.

**-** **Budget Tracking:**

Include estimated costs for accommodations, meals, and activities with budget alerts.

**-** **Map Visualization:**

Add interactive maps showing travel routes, landmarks, and distances between stops.

**Collaborating**

**-** Contributions are welcome! Feel free to submit issues

**-** Please contribute by reporting bugs, suggesting features, or improving the code.

**-** Contributions make this project better — join in by sharing ideas or code.

✍️**Author** 

This project was developed as a learning experience to explore AI integration, create interactive Streamlit apps, automate PDF generation, and begin managing prompt engineering techniques to improve AI output relevance and coherence.


🙌**Acknowledgemnt**

I sincerely thank my instructor for their exceptional teaching in the AI Practitioner class. Their expertise and encouragement greatly contributed to my learning and growth.
