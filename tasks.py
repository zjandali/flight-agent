from crewai import Task
from agents import flights_agent, summarize_agent

search_flights_task = Task(
    description=(
        "Search for flights from {departure} to {destination} on {date}. "
        "If a return date is provided, search for round-trip flights. "
        "Provide the top 5 flight options with details including airline, departure time, arrival time, duration, layovers, and price."
    ),
    expected_output='A list of the top 5 flight options with complete details.',
    agent=flights_agent,
)

summarize_flights_task = Task(
    description=(
        "Summarize the provided flight options into a user-friendly list. "
        "Ensure the information is clear and concise, highlighting key details such as airline, times, duration, layovers, and price."
    ),
    expected_output='A formatted summary of the top 5 flight options.',
    agent=summarize_agent,
)
