from datetime import date

from google.adk.agents import Agent, ParallelAgent, SequentialAgent
from google.adk.agents.callback_context import CallbackContext
from google.adk.models.llm_response import types
from google.adk.tools.tool_context import ToolContext
from solar_investigator.tools import tools
from .prompts import return_instruction_planner
from .sub_agents import (
    daily_pr_agent,
    detailed_inverter_performance_agent,
    detailed_plant_timeseries_agent,
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

def setup(callback_context: CallbackContext):
    callback_context.state["daily_pr_agent_output"] = None
    callback_context.state["detailed_inverter_performance_agent_output"] = None
    callback_context.state["detailed_plant_timeseries_agent_output"] = None
    callback_context.state["problematic_detailed_inverter_performance"] = []
    callback_context.state["problematic_five_minutes_pr"] = []
    callback_context.state["inverter_device_id_and_capacity_peak"] = []
    callback_context.state["plant_id"] = None
    callback_context.state["inverter_date_to_check"] = []
    callback_context.state["filtered_plant_timeseries_df"] = None
    callback_context.state["date_requested"] = None
    callback_context.state["date_today"] = date_today


def initial_config(
    plant_id: str,
    inverter_date_to_check: list,
    inverter_device_id_and_capacity_peak: dict,
    date_requested: list,
    tool_context: ToolContext,
):
    """tools to store the information needed for diagnose steps afterwards

    Parameters:
    string plant_id : plant_id of the plant
    list date : date to check for inverters of the specific plant
    dictionary device id and capacity peak : id for the inverters of the specific plants and its capacity peak , kilowatt peak .Example: {'1jrn3i2 jr32':'130.5kwp'}
    list date : list of dates requested to check
    """
    tool_context.state["plant_id"] = plant_id
    tool_context.state["inverter_date_to_check"] = inverter_date_to_check
    tool_context.state["inverter_device_id_and_capacity_peak"] = (
        inverter_device_id_and_capacity_peak
    )
    tool_context.state["date_requested"] = date_requested


parallel_pipeline = ParallelAgent(
    name="parallel_pipeline",
    sub_agents=[
        detailed_plant_timeseries_agent,
        detailed_inverter_performance_agent,
    ],
)

planner_agent = Agent(
    name="planner_agent",
    model="gemini-2.5-flash-preview-05-20",
    instruction=return_instruction_planner(),
    description="You are an expert planner",
    output_key="planner_agent_output",
    generate_content_config=types.GenerateContentConfig(temperature=0.1),
    tools=[
        tools[5],
        tools[6],
        initial_config,
        ],
)
root_agent = SequentialAgent(
    name="problem_finder2",
    sub_agents=[
        planner_agent,
        daily_pr_agent,
        parallel_pipeline,
    ],
    before_agent_callback=setup,
)
