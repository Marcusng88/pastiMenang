from datetime import date

from google.adk.agents import Agent, SequentialAgent
from google.adk.agents.callback_context import CallbackContext
from google.adk.models.llm_response import types
from google.adk.tools import load_artifacts

from solar_investigator.tools import tools

from .prompts import return_instruction_planner, return_instruction_problem_finder
from .sub_agents import code_agent
from .tools import (
    call_daily_inverter_agent,
    call_daily_pr_agent,
    call_detailed_inverter_performance_agent,
    call_detailed_plant_timeseries_agent,
)

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

planner_agent = Agent(
    name="planner_agent",
    model="gemini-2.5-flash-preview-05-20",
    instruction=return_instruction_planner(),
    description="You are an expert planner",
    output_key="planner_agent_output",
    generate_content_config=types.GenerateContentConfig(temperature=0.1),
)

orchestrator_agent = Agent(
    name="orchestrator_agent",
    model="gemini-2.5-flash-preview-05-20",
    global_instruction=f"You are responsible to tackle problems and errors for solar plant cells performance and today date is {date_today}",
    instruction=return_instruction_problem_finder(),
    description="You are an expert of problem finder",
    sub_agents=[code_agent],
    tools=[
        call_daily_pr_agent,
        call_detailed_plant_timeseries_agent,
        call_daily_inverter_agent,
        call_detailed_inverter_performance_agent,
        tools[5],
        tools[6],
        load_artifacts,
    ],
    generate_content_config=types.GenerateContentConfig(temperature=0.1),
)


def setup(callback_context: CallbackContext):
    callback_context.state["daily_inverter_agent_output"] = None
    callback_context.state["daily_pr_agent_output"] = None
    callback_context.state["detailed_inverter_performance_agent_output"] = None
    callback_context.state["detailed_plant_timeseries_agent_output"] = None
    callback_context.state["problematic_daily_inverter"] = []
    callback_context.state["problematic_detailed_inverter_performance"] = []
    callback_context.state["problematic_five_minutes_pr"] = []


root_agent = SequentialAgent(
    name="problem_finder",
    sub_agents=[
        planner_agent,
        orchestrator_agent,
    ],
    before_agent_callback=setup,
)
