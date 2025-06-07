from google.adk.agents import Agent
from google.adk.agents.callback_context import CallbackContext
from google.adk.tools.tool_context import ToolContext

from solar_investigator.tools import tools

from .prompts import return_instruction_detailed_plant_timeseries


def append_problematic_rows(rows: str, tool_context: ToolContext):
    """tools to store problematic rows
    parameters
    String rows : the json response for the problematic five minutes data eg. "{problematic_five_minutes_pr : [row_data_here] ,analysis : "A general explaination on why you think these data is abnormal}"
    """
    if "problematic_five_minutes_pr" not in tool_context.state:
        problematic_five_minutes_pr_settings = []
        tool_context.state["problematic_five_minutes_pr"] = (
            problematic_five_minutes_pr_settings
        )

    problematic_five_minutes_pr_settings = tool_context.state[
        "problematic_five_minutes_pr"
    ]
    problematic_five_minutes_pr_settings.append(rows)
    tool_context.state["problematic_five_minutes_pr"] = (
        problematic_five_minutes_pr_settings
    )


def setup(callback_context: CallbackContext):
    if "problematic_five_minutes_pr" not in callback_context.state:
        problematic_five_minutes_pr_settings = []
        callback_context.state["problematic_five_minutes_pr"] = (
            problematic_five_minutes_pr_settings
        )
    callback_context.state["problematic_five_minutes_pr"] = []


def clear_problematic_rows(callback_context: CallbackContext):
    callback_context.state["problematic_five_minutes_pr_output"] = None


detailed_plant_timeseries_agent = Agent(
    name="detailed_plant_timeseries_agent",
    model="gemini-2.0-flash-001",
    description="You are an expert in retrieving detailed data for target days for specific plants",
    instruction=return_instruction_detailed_plant_timeseries(),
    tools=[tools[3], append_problematic_rows],
    # code_executor=VertexAiCodeExecutor(),
    # output_key='problematic_five_minutes_pr_output',
    before_agent_callback=setup,
)
