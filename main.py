import os
import textwrap
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import black, grey, darkgreen
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
- Each day MUST include:
  Breakfast, Morning, Lunch, Afternoon, Evening Activity, Dinner
- Do NOT start with words like "Sure", "Here is", etc.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content


# ------------------------------
# AUTO-REPAIR: Missing Sections
# ------------------------------
def repair_missing_sections(plan_text):
    fixed_lines = []
    current_day = []
    sections = {
        "breakfast": False,
        "lunch": False,
        "evening activity": False
    }

    def flush():
        if not sections["breakfast"]:
            current_day.append("- Breakfast: Enjoy breakfast at a nearby café or hotel restaurant.")
        if not sections["lunch"]:
            current_day.append("- Lunch: Have a relaxed meal at a family-friendly restaurant.")
        if not sections["evening activity"]:
            current_day.append("- Evening Activity: Take a calm evening stroll or attend a local cultural event.")
        fixed_lines.extend(current_day)

    for line in plan_text.split("\n"):
        lower = line.lower()

        if lower.startswith("day"):
            if current_day:
                flush()
                current_day.clear()
                sections.update({k: False for k in sections})
            current_day.append(line)
        else:
            for key in sections:
                if key in lower:
                    sections[key] = True
            current_day.append(line)

    if current_day:
        flush()

    return "\n".join(fixed_lines)


# ------------------------------
# Helpers
# ------------------------------
def clean_markdown(line):
    line = line.strip()
    while line.startswith("#"):
        line = line[1:].strip()
    return line.replace("**", "")

def is_time_heading(line):
    l = line.lower().lstrip("•- ").strip()
    return l.startswith(("breakfast", "morning", "lunch", "afternoon", "evening", "dinner"))

def split_bullets(line):
    if " - " in line:
        parts = line.replace("–", "-").split(" - ")
        return ["- " + p.strip() for p in parts if p.strip()]
    return [line]

def iconize_heading(text):
    t = text.lower()
    if t.startswith("breakfast"):
        return "🍳 " + text
    if t.startswith("morning"):
        return "🌅 " + text
    if t.startswith("lunch"):
        return "🍴 " + text
    if t.startswith("afternoon"):
        return "☀️ " + text
    if t.startswith("evening activity"):
        return "🎭 " + text
    if t.startswith("dinner"):
        return "🍽️ " + text
    return text

def pdf_safe(text):
    return text.encode("ascii", "ignore").decode().strip()


# ------------------------------
# PDF Generator (FIXED)
# ------------------------------
def generate_pdf(destination, plan_text):
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

    for raw_line in plan_text.split("\n"):
        if y < 120:
            y = new_page()

        line = clean_markdown(raw_line)

        if line.lower().startswith("day"):
            c.setFont("Helvetica-Bold", 16)
            c.setFillColor(grey)
            c.drawString(LEFT, y, line)
            y -= 10
            c.line(LEFT, y, RIGHT, y)
            y -= 20
            c.setFillColor(black)
            c.setFont("Helvetica", 11)
            continue

        for logical_line in split_bullets(line):

            if is_time_heading(logical_line):
                heading = pdf_safe(iconize_heading(logical_line.lstrip("•- ").strip()))
                text = c.beginText(LEFT + 10, y)
                text.setFont("Helvetica-Bold", 12)
                for w in textwrap.wrap(heading, 70):
                    text.textLine(w)
                    y -= 14
                c.drawText(text)
                continue

            body = pdf_safe(logical_line)
            text = c.beginText(LEFT + 25, y)
            text.setFont("Helvetica", 11)
            for w in textwrap.wrap(body, 70):
                text.textLine(w)
                y -= 14
            c.drawText(text)

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

# ---- RESET ----
if st.button("Reset Form"):
    st.session_state.form_key += 1
    st.session_state.pop("plan", None)
    st.rerun()

# ---- OUTPUT ----
if submit:
    if not destination.strip() or not interests.strip() or not guardrails.strip():
        st.error("Please fill in ALL required fields before generating the plan.")
        st.stop()

    with st.spinner("Generating your travel plan..."):
        raw_plan = generate_travel_plan_ai(destination, days, interests, guardrails)
        st.session_state.plan = repair_missing_sections(raw_plan)

    st.success("Travel plan generated!")

if "plan" in st.session_state:
    st.subheader("📅 Travel Itinerary")
    st.write(st.session_state.plan)

    pdf = generate_pdf(destination, st.session_state.plan)

    with open(pdf, "rb") as f:
        st.download_button(
            "📄 Download Travel Plan PDF",
            f,
            file_name="Travel_Plan.pdf",
            mime="application/pdf"
        )
