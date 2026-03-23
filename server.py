from typing import Annotated
from pydantic import Field
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("OfficeAutomationServer")

@mcp.tool()
async def get_weather(
    city: Annotated[str, Field(description="The name of the city to check")]
):
    """Check the weather for a specific city."""
    return f"It's sunny in {city}! Perfect for an outdoor meeting."

@mcp.tool()
async def calculate_travel_time(
    distance_km: Annotated[float, Field(description="Distance in kilometers", gt=0)],
    speed_kmh: Annotated[float, Field(description="Average speed in km/h", gt=0)]
):
    """Estimate travel time between locations."""
    hours = distance_km / speed_kmh
    return f"Estimated travel time: {hours:.2f} hours."

@mcp.tool()
async def format_meeting_notes(
    raw_text: Annotated[str, Field(description="The messy notes from the meeting")]
):
    """Cleans up raw notes into a bulleted list."""
    return f"Formatted Notes:\n- " + raw_text.replace(". ", "\n- ")

@mcp.tool()
async def convert_currency(
    amount: Annotated[float, Field(description="Amount to convert")],
    to_currency: Annotated[str, Field(description="Target currency code (e.g. USD, EUR)")]
):
    """Convert expenses to a target currency (mock conversion)."""
    rate = 1.1 
    result = amount * rate
    return f"{amount} converted to {to_currency} is approximately {result:.2f}"

@mcp.tool()
async def admin_system_reboot():
    """HIGH PRIVILEGE: Reboots the office server system."""
    return "SYSTEM REBOOTING... (This tool should be filtered for non-admin agents!)"

if __name__ == "__main__":
    mcp.run()