import os
import textwrap
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import black, grey, blue, darkgreen
from reportlab.pdfgen import canvas

# ------------------------------
# Load Environment & OpenAI Client
# ------------------------------
load_dotenv()
client = OpenAI()

# ------------------------------
# RESET FIX: FORM KEY
# ------------------------------
if "form_key" not in st.session_state:
    st.session_state.form_key = 0

# ------------------------------
# AI: Generate Travel Plan
# ------------------------------
def generate_travel_plan_ai(destination, days, interests, guardrails):
    prompt = f"""
Create a {days}-day travel plan for {destination}.
Interests: {interests}
Preferences: {guardrails}

Rules:
- Different activities each day
- Family friendly where applicable
- No repetition across days
- Clear Day-wise structure
- Do NOT start with words like "Sure", "Here is", etc.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content


# ------------------------------
# AI: Generate Hotel Recommendations
# ------------------------------
def generate_hotels_ai(destination, stars):
    prompt = f"""
Recommend hotels in {destination}.

Requirements:
- {stars}-star hotels
- Provide exactly 3 hotels
- Do NOT use markdown
- Do NOT use separators like ---

Format EXACTLY (6 lines per hotel):

Hotel Name
⭐⭐⭐⭐⭐
Short description text
https://www.expedia.com/Hotel-Search?destination=HOTEL_NAME+DESTINATION
https://www.hotels.com/Hotel-Search?destination=HOTEL_NAME+DESTINATION
https://www.booking.com/hotel/...
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content


# ------------------------------
# AI: Generate Restaurant Recommendations (Yelp)
# ------------------------------
def generate_restaurants_ai(destination, cuisines):
    prompt = f"""
Recommend restaurants in {destination}.

Preferred cuisines: {cuisines}

Rules:
- Provide exactly 3 restaurants
- Use REAL restaurant names
- Do NOT use markdown
- Do NOT use separators like ---
- Format EXACTLY as 4 lines per restaurant

Format:
Restaurant Name
Cuisine
Short description
https://www.yelp.com/search?find_desc=RESTAURANT_NAME&find_loc=DESTINATION
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content


# ------------------------------
# Helpers
# ------------------------------
def clean_markdown(line):
    line = line.strip()
    while line.startswith("#"):
        line = line[1:].strip()
    return line.replace("**", "")

def normalize_stars(star_line):
    count = star_line.count("⭐")
    return "★" * count if count else star_line

def is_time_heading(line):
    l = line.lower().lstrip("•- ").strip()
    return l.startswith(("morning", "afternoon", "evening"))


# ------------------------------
# PDF Generator (V2.1 STABLE)
# ------------------------------
def generate_pdf(destination, plan_text, hotels_text, restaurants_text):
    file_name = "Travel_Plan.pdf"
    c = canvas.Canvas(file_name, pagesize=letter)
    width, height = letter

    LEFT, RIGHT = 50, width - 50
    y = height - 60

    def new_page():
        c.showPage()
        c.setFont("Helvetica", 11)
        return height - 60

    # ---- Title ----
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(width / 2, y, "Travel Plan")
    y -= 30

    c.setFont("Helvetica", 16)
    c.drawCentredString(width / 2, y, destination)
    y -= 30

    c.line(LEFT, y, RIGHT, y)
    y -= 35

    # ---- Itinerary ----
    c.setFont("Helvetica-Bold", 18)
    c.drawString(LEFT, y, "Travel Itinerary")
    y -= 25
    c.setFont("Helvetica", 11)

    intro_done = False

    for raw_line in plan_text.split("\n"):
        if y < 120:
            y = new_page()

        line = clean_markdown(raw_line)

        if not intro_done and line and not line.lower().startswith("day"):
            c.setFont("Helvetica-Bold", 13)
            c.setFillColor(darkgreen)
            for w in textwrap.wrap(line, 85):
                c.drawString(LEFT + 20, y, w)
                y -= 16
            y -= 14
            c.setFillColor(black)
            c.setFont("Helvetica", 11)
            intro_done = True
            continue

        if line.lower().startswith("day"):
            c.setFont("Helvetica-Bold", 16)
            c.setFillColor(grey)
            c.drawString(LEFT, y, line)
            y -= 10
            c.line(LEFT, y, RIGHT, y)
            y -= 20
            c.setFillColor(black)
            c.setFont("Helvetica", 11)

        elif is_time_heading(line):
            c.setFont("Helvetica-Bold", 12)
            c.drawString(LEFT + 10, y, line)
            y -= 16
            c.setFont("Helvetica", 11)

        else:
            for w in textwrap.wrap(line, 90):
                c.drawString(LEFT + 20, y, w)
                y -= 14

    # ---- Restaurants ----
    if restaurants_text:
        y = new_page()
        c.setFont("Helvetica-Bold", 20)
        c.drawCentredString(width / 2, y, "Restaurant Recommendations")
        y -= 30
        c.line(LEFT, y, RIGHT, y)
        y -= 35

        lines = [l.strip() for l in restaurants_text.split("\n") if l.strip()]
        i = 0

        while i + 3 < len(lines):
            if y < 140:
                y = new_page()

            c.setFont("Helvetica-Bold", 14)
            c.drawString(LEFT, y, lines[i])
            y -= 18

            c.setFont("Helvetica-Oblique", 12)
            c.drawString(LEFT, y, lines[i + 1])
            y -= 18

            c.setFont("Helvetica", 11)
            for w in textwrap.wrap(lines[i + 2], 90):
                c.drawString(LEFT + 15, y, w)
                y -= 14

            c.setFillColor(blue)
            link = lines[i + 3]
            c.drawString(LEFT + 15, y, link)
            c.linkURL(link, (LEFT + 15, y - 2, RIGHT, y + 10))
            c.setFillColor(black)

            y -= 25
            i += 4

    # ---- Hotels ----
    if hotels_text:
        y = new_page()
        c.setFont("Helvetica-Bold", 20)
        c.drawCentredString(width / 2, y, "Hotel Recommendations")
        y -= 30
        c.line(LEFT, y, RIGHT, y)
        y -= 35

        lines = [l.strip() for l in hotels_text.split("\n") if l.strip()]
        i = 0

        while i + 5 < len(lines):
            if y < 160:
                y = new_page()

            c.setFont("Helvetica-Bold", 14)
            c.drawString(LEFT, y, lines[i])
            y -= 18

            c.setFont("Helvetica", 12)
            c.drawString(LEFT, y, normalize_stars(lines[i + 1]))
            y -= 18

            c.setFont("Helvetica", 11)
            for w in textwrap.wrap(lines[i + 2], 90):
                c.drawString(LEFT + 15, y, w)
                y -= 14

            c.setFillColor(blue)
            for link in lines[i + 3:i + 6]:
                c.drawString(LEFT + 15, y, link)
                c.linkURL(link, (LEFT + 15, y - 2, RIGHT, y + 10))
                y -= 16
            c.setFillColor(black)

            y -= 25
            i += 6

    c.save()
    return file_name


# ------------------------------
# Streamlit UI
# ------------------------------
st.set_page_config("Travel Guide", layout="centered")
st.title("🌍 Travel Guide")

with st.form(f"travel_form_{st.session_state.form_key}"):
    destination = st.text_input("Destination (e.g., San Francisco)")
    days = st.number_input("Number of Days", 1, 30, 3)
    interests = st.text_input("Special Interests (e.g., Museums, Food, Nature)")
    guardrails = st.text_input("Preferences (e.g., Kids friendly, less walking)")
    submit = st.form_submit_button("Generate Travel Plan")

# ---- RESET BUTTON (CORRECT & RELIABLE) ----
if st.button("Reset Form"):
    st.session_state.form_key += 1
    for k in ["plan", "restaurants", "hotels"]:
        st.session_state.pop(k, None)
    st.rerun()

# ---- OUTPUT ----
if submit:
    if not destination.strip() or not interests.strip() or not guardrails.strip():
        st.error("Please fill in ALL required fields before generating the plan.")
        st.stop()

    with st.spinner("Generating your travel plan..."):
        st.session_state.plan = generate_travel_plan_ai(
            destination,
            days,
            interests,
            guardrails
        )
        st.session_state.restaurants = None
        st.session_state.hotels = None

    st.success("Travel plan generated!")

if "plan" in st.session_state:
    st.subheader("📅 Travel Itinerary")
    st.write(st.session_state.plan)

if st.session_state.get("restaurants"):
    st.subheader("🍽️ Restaurant Recommendations")
    st.write(st.session_state.restaurants)

if st.session_state.get("hotels"):
    st.subheader("🏨 Hotel Recommendations")
    st.write(st.session_state.hotels)

if "plan" in st.session_state:
    pdf = generate_pdf(
        destination,
        st.session_state.plan,
        st.session_state.get("hotels"),
        st.session_state.get("restaurants")
    )

    with open(pdf, "rb") as f:
        st.download_button(
            "📄 Download Travel Plan PDF",
            f,
            file_name="Travel_Plan.pdf",
            mime="application/pdf"
        )


