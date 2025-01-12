from crewai import Agent
from browserbase import browserbase
from kayak import kayak

flights_agent = Agent(
    role='Flight Search Specialist',
    goal='Find the best flight options based on user criteria.',
    backstory=(
        "As a seasoned travel expert, you have extensive knowledge of flight routes, airlines, "
        "and booking systems. Your mission is to find the most suitable flights for clients."
    ),
    tools=[browserbase, kayak],
)

summarize_agent = Agent(
    role='Flight Summary Specialist',
    goal='Summarize flight options into a user-friendly format.',
    backstory=(
        "With a keen eye for detail, you excel at presenting complex information in an accessible way, "
        "helping clients make informed travel decisions."
    ),
    tools=[],
)
