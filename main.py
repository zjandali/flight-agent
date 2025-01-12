from crewai import Crew
from tasks import search_flights_task, summarize_flights_task

flight_booking_crew = Crew(
    agents=[search_flights_task.agent, summarize_flights_task.agent],
    tasks=[search_flights_task, summarize_flights_task],
    memory=True,
    cache=True,
    max_rpm=100,
)

if __name__ == "__main__":
    import sys
    user_input = sys.argv[1]
    # Parse user input to extract departure, destination, date, and return_date if applicable
    # This parsing logic will depend on the expected input format
    inputs = {
        'departure': 'SFO',  # Example: Extracted from user_input
        'destination': 'JFK',  # Example: Extracted from user_input
        'date': '2025-1-21',  # Example: Extracted from user_input
        'return_date': None,  # Example: Extracted from user_input if round-trip
    }
    result = flight_booking_crew.kickoff(inputs=inputs)
    print(result)
