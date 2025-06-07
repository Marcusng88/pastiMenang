from google.adk.agents import Agent

# TOOLBOX_URL = os.getenv("MCP_TOOLBOX_URL", "http://127.0.0.1:5000")
# toolbox = ToolboxSyncClient(TOOLBOX_URL)
from solar_investigator.tools import tools

from .prompts import return_instruction_daily_pr

# Load all the tools from toolset
# ['compare_daily_inverter_performance', 'get_all_alarms', 'get_daily_plant_summary', 'get_detailed_plant_timeseries', 'get_inverters_alarms', 'list_available_plants', 'list_inverters_for_plant', 'track_single_inverter_performance']
daily_pr_agent = Agent(
    name="daily_pr_agent",
    model="gemini-2.0-flash-001",
    description="You are agent to retrieve daily and monthly PR data for specific plant",
    instruction=return_instruction_daily_pr(),
    tools=[
        tools[2],
        tools[5],
    ],
    output_key="problematic_daily_pr_output",
)
