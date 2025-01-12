from crewai.tools import tool
from typing import Optional

@tool("Kayak tool")
def kayak(departure: str, destination: str, date: str, return_date: Optional[str] = None) -> str:
    """
    Generates a Kayak URL for flights between departure and destination on the specified date.
    :param departure: The IATA code for the departure airport (e.g., 'SFO' for San Francisco)
    :param destination: The IATA code for the destination airport (e.g., 'JFK' for New York)
    :param date: The date of the flight in the format 'YYYY-MM-DD'
    :param return_date: Only for two-way tickets. The return date in the format 'YYYY-MM-DD'
    :return: A valid Kayak search URL
    """
    base_url = "https://www.kayak.com/flights"
    if return_date:
        return f"{base_url}/{departure}-{destination}/{date}/{return_date}"
    else:
        return f"{base_url}/{departure}-{destination}/{date}"
