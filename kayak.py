from crewai.tools import tool
from typing import Optional, Dict

@tool("Kayak tool")
def kayak(departure: str, destination: str, date: str, return_date: Optional[str] = None) -> Dict[str, str]:
    """
    Generates Kayak URLs for flights between departure and destination on the specified date.
    :param departure: The IATA code for the departure airport (e.g., 'SFO' for San Francisco)
    :param destination: The IATA code for the destination airport (e.g., 'JFK' for New York)
    :param date: The date of the flight in the format 'YYYY-MM-DD'
    :param return_date: Only for two-way tickets. The return date in the format 'YYYY-MM-DD'
    :return: Dictionary containing search and booking URLs
    """
    base_url = "https://www.kayak.com/flights"
    booking_base = "https://www.kayak.com/book/flights"
    
    if return_date:
        search_url = f"{base_url}/{departure}-{destination}/{date}/{return_date}"
        booking_url = f"{booking_base}/{departure}-{destination}/{date}/{return_date}"
    else:
        search_url = f"{base_url}/{departure}-{destination}/{date}"
        booking_url = f"{booking_base}/{departure}-{destination}/{date}"
    
    return {
        "search_url": search_url,
        "booking_url": booking_url
    }
