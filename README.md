# HW7-CareerCoach-AI-Project
Assignment 6: Build App  “ AI Travel Guide”
This project is an AI-powered Travel Planning application built using **Python**, **Streamlit**, and the **OpenAI API**.
It generates a **day-by-day travel itinerary** based on user preferences and exports the plan as a **professionally formatted PDF**.

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
  
🧠 How the AI Works

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
- 
Install dependencies
pip install -r requirements.txt

Create a .env file

Run the app
streamlit run app.py

Output

On-screen travel itinerary

Downloadable PDF Travel Plan

Clean, readable formatting suitable for sharing or printing
