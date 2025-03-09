from fastapi import FastAPI 
import random

app = FastAPI()

side_hustles = [
    "Custom API development (FastAPI)",
    "API integration with frontend (React, Vue, Next.js)",
    "Web scraping APIs",
    "Authentication & security (JWT, OAuth)",
    "Database-backed APIs (SQLAlchemy, MongoDB)",
    "AI/ML API deployment using FastAPI",
    "Platforms: Upwork, Fiverr, Freelancer, PeoplePerHour",
    "Sell APIs on RapidAPI, API Marketplace, Gumroad", 
    "Weather API",
    "AI-based chatbot API",
    "Crypto price tracking API",
    "Stock market API",
    "AI Image generation API (OpenAI, Hugging Face)",
    "Develop micro SaaS with FastAPI + React/Vue",
    "SEO analysis tool",
    "AI-generated blog writer",
    "Automated resume builder",
    "AI-powered chatbot",
    "Sentiment analysis tool",
    "Create & sell a FastAPI course (Udemy, Gumroad, YouTube)",
    "Start blogging on Medium, Hashnode, or Dev.to",
    "Offer one-on-one coaching on Zoom",
    "Build an open-source project (FastAPI templates, authentication modules)",
    "Get GitHub sponsorships",
    "Participate in Hackathons for prizes & exposure",
    "Work as a part-time backend developer",
    "Apply for remote jobs in startups",
    "Deploy AI-powered APIs using FastAPI",
    "Offer AI automation services (Chatbots, OCR, Voice recognition)",
    "Build AI-powered apps using OpenAI APIs"
]

money_quotes = [
    "Money is a tool. Use it wisely, and it will serve you well.",
    "The secret to wealth is simple: Save more than you spend and invest wisely.",
    "Rich people stay rich by living like they’re broke. Broke people stay broke by living like they’re rich.",
    "Do not save what is left after spending, but spend what is left after saving. - Warren Buffett",
    "Wealth is not about having a lot of money; it’s about having a lot of options.",
    "A penny saved is a penny earned.",
    "Investing in yourself is the best investment you will ever make.",
    "The goal isn’t more money. The goal is living life on your terms."
]


@app.get("/side_hustles")
def get_side_hustle():
   
    """"Return a random side hustle idea"""
    return{"side_hustle" : random.choice(side_hustles)}



@app.get("/money_quotes")
def get_money_quotes():
   
    """returns a random money quotes"""
    return {"money_quotes" : random.choice(money_quotes)}