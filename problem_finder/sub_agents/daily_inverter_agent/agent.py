from google.adk.agents import Agent
from google.adk.agents.callback_context import CallbackContext

from solar_investigator.tools import tools

from .prompts import return_instruction_daily_inverter
from .tools import append_problematic_rows


def setup(callback_context: CallbackContext):
    if "problematic_daily_inverter" not in callback_context.state:
        problematic_daily_inverter_settings = []
        callback_context.state["problematic_daily_inverter"] = (
            problematic_daily_inverter_settings
        )


daily_inverter_agent = Agent(
    name="daily_inverter_agent",
    model="gemini-2.5-flash-preview-05-20",
    instruction=return_instruction_daily_inverter(),
    tools=[
        tools[0],
        append_problematic_rows,
    ],
    before_agent_callback=setup,
    output_key="daily_inverter_agent_output",
)
