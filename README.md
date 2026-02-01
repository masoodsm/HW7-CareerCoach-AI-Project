# HW7-CareerCoach-AI-Project
Assignment 6: Build App  “ AI Travel Guide”
This project is an AI-powered Travel Planning application built using **Python**, **Streamlit**, and the **OpenAI API**.
It generates a **day-by-day travel itinerary** based on user preferences and exports the plan as a **professionally formatted PDF**.

**Problem Statement**

This project solves the problem of manual travel planning by generating personalized, day-by-day travel itineraries based on user inputs such as destination, number of days, interests, and preferences. It automates the creation of travel plans, including recommendations for activities, meals, and accommodations, saving users time and enhancing their travel experience.

**Relation to AI and AI-Assisted Workflows**

The project leverages AI, specifically OpenAI's GPT language model, to generate customized travel plans by interpreting natural language inputs. This showcases AI-assisted workflows where AI augments human tasks—here, by synthesizing relevant and tailored travel information dynamically. It exemplifies how AI can support decision-making and creative planning through natural language understanding and content generation.

✨ Features
- Generate a multi-day travel itinerary
- Each day includes:
  - Morning
  - Lunch
  - Afternoon
  - Evening Activity
  - Dinner
- Family-friendly and non-repetitive activities
- Clean, structured output
- Downloadable PDF travel plan
- Simple, user-friendly Streamlit UI
  
🧠 How the AI/Code Works

- User inputs destination, number of days, interests, and preferences
- The OpenAI model:
  - Interprets preferences
  - Generates structured, natural-language itineraries
  - Ensures daily coverage of activities and meals
- The app post-processes the output to:
  - Fix missing sections (if any)
  - Prevent text overflow in PDF
  - Ensure readable formatting
    
🛠 Tech Stack
- Python
- Streamlit
- OpenAI API
- ReportLab (PDF generation)
- dotenv (.env for environment variables)

**How to Run & Use**

**Run**
**Use Visual Studio : Terminal**
**Create Virual Environment**

python -m venv venv

**Install dependencies**

pip install -r requirements.txt

**Upgrade pip**

*python -m pip install --upgrade pip*

**Create a .env** 
*OPENAI_API_KEY=your_openai_api_key_here*

File in the project root folder and add your OpenAI API key:

**source venv/bin/activate**

 *.venv\Scripts\activate.ps1*

*streamlit run app.py*

**How to use the the Application**

**Enter Destination**
•	Example: San Francisco, CA

**Select Number of Days**
Choose how many days you plan to travel (e.g., 3 days)

**Enter Special Interests** (eg Museums, nature, family-friendly activities)

**Enter Preferences** (e.g Kids friendly, less walking) These act as guardrails for the AI.

**OUTPUT**

**Click “Generate Travel Plan”**

The AI will generate a day-by-day itinerary.
•  Each day includes:
  •	 Morning
  •	Lunch
  •	Afternoon
  •	Evening Activity
  •	Dinner

**Review the Travel Itinerary**
•	The plan is displayed directly on the screen.
•	You can scroll and review all days.

**Download the PDF**
**Click “Download Travel Plan PDF”**
A professionally formatted PDF is generated with:
•	Clear day sections
•	Proper text wrapping
•	No text cutoff across pages

**What the AI Is Doing** 

Uses OpenAI’s language model to:

•	Understand travel preferences

•	Generate structured daily plans

•	Ensure completeness (morning, lunch, evening, etc.)

•  Automatically fixes missing sections if the AI response is incomplete.

•  Formats output for both screen display and PDF export.

**Resetting the Form**

•	If you want to start over or clear all inputs and outputs, click the Reset Form button.

•	This will clear your previous entries and generated plans so you can enter new travel preferences.
