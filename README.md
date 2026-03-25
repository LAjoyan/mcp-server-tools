# Office Automation MCP Server

A high-performance MCP server built with **FastMCP** providing office automation tools.

## 🛠 Tools Provided
This server exposes 5 tools for agent interaction:
1. `get_weather`: Check the weather for a specific city.
2. `calculate_travel_time`: Estimate travel time based on distance and speed.
3. `format_meeting_notes`: Clean up raw text into bulleted lists.
4. `convert_currency`: Perform mock currency conversions for expenses.
5. `admin_system_reboot`: **(Restricted)** A high-privilege tool for system reboots.

## 🔗 System Relationship
This repository acts as the **Service Provider**. It is designed to be consumed by the [mcp-agent](https://github.com/LAjoyan/mcp-agent) repository via a Decoupled Architecture.


## 🚀 Requirements
- Python 3.10+
- uv

## 📦 Installation
```bash
uv add mcp pydantic
```
## 🔌 Integration
This server is designed to be called via Stdio by an MCP Client (Agent).

```
# Example Client Config
server_params = StdioServerParameters(
    command="uv",
    args=["--directory", "path/to/mcp-server-tools", "run", "server.py"],
)
```