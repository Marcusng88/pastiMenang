from datetime import date

from google.adk.agents import Agent
from google.adk.agents.callback_context import CallbackContext
from google.adk.tools import load_artifacts

from solar_investigator.tools import tools

from .prompts import return_instruction_problem_finder
from .tools import call_daily_pr_agent, call_detailed_plant_timeseries_agent

# ['compare_daily_inverter_performance', 'get_all_alarms', 'get_daily_plant_summary', 'get_detailed_plant_timeseries', 'get_inverters_alarms', 'list_available_plants', 'list_inverters_for_plant', 'track_single_inverter_performance']

# 0  comparing daily inverter performance
# 1  get all alarm
# 2  get daily plant summary
# 3  get detailed plant timeseries
# 4  get inverters alarms
# 5  list available plant
# 6  list inverters for plant
# 7  track single inverter performance


date_today = date.today()


def setup_before_agent_call(callback_context: CallbackContext):
    """Setup the agent."""

    # setting up database settings in session.state
    if "daily_pr_agent_settings" not in callback_context.state:
        daily_pr_agent_settings = dict()
        daily_pr_agent_settings["daily_pr_output"] = "None"
        callback_context.state["daily_pr_settings"] = daily_pr_agent_settings


root_agent = Agent(
    name="problem_finder",
    model="gemini-2.0-flash-001",
    global_instruction=f"You are responsible to tackle problems and errors for solar plant cells performance and today date is {date_today}",
    instruction=return_instruction_problem_finder(),
    description="You are an expert of problem finder",
    tools=[
        call_daily_pr_agent,
        call_detailed_plant_timeseries_agent,
        tools[5],
        load_artifacts,
    ],
)
