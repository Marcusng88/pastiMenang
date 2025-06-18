from io import BytesIO

from google.adk.agents import Agent, ParallelAgent, SequentialAgent
from google.adk.agents.callback_context import CallbackContext

from .prompts import (
    return_instruction_coding_1,
    return_instruction_coding_2,
    return_instruction_coding_3,
    return_instruction_coding_4,
)
from .tools import save_generated_report_local

code_agent_1 = Agent(
    name="code_agent_1",
    model="gemini-2.5-flash-preview-05-20",
    description="You are expert in coding",
    instruction=return_instruction_coding_1(),
    output_key="html_daily_inverter",
)
code_agent_2 = Agent(
    name="code_agent_2",
    model="gemini-2.5-flash-preview-05-20",
    description="You are expert in coding",
    instruction=return_instruction_coding_2(),
    output_key="html_detailed_inverter",
)
code_agent_3 = Agent(
    name="code_agent_3",
    model="gemini-2.5-flash-preview-05-20",
    description="You are expert in coding",
    instruction=return_instruction_coding_3(),
    output_key="html_daily_pr",
)
code_agent_4 = Agent(
    name="code_agent_4",
    model="gemini-2.5-flash-preview-05-20",
    description="You are expert in coding",
    instruction=return_instruction_coding_4(),
    output_key="html_detailed_plant_timeseries",
)

parallel_code_pipeline = ParallelAgent(
    name="parallel_code_pipeline",
    sub_agents=[code_agent_1, code_agent_2, code_agent_3, code_agent_4],
)
merger_agent = Agent(
    name="merger_agent",
    model="gemini-2.5-flash-preview-05-20",
    instruction="""your job is to merge four html code ,just concat it , do not add anything .
    first is {html_daily_pr}
    second is {html_detailed_plant_timeseries}
    third is {html_daily_inverter}
    fourth is {html_detailed_inverter}.
    After you merge , add <html> <body> <\body> <\\html> at start and end .ONLY return the html , do not add other content or words""",
    output_key="final_html",
)


def setup(callback_context: CallbackContext):
    """setup for coding agent"""
    callback_context.state["report_bytes"] = BytesIO()
    callback_context.state["html_daily_inverter"] = ""
    callback_context.state["html_detailed_inverter"] = ""
    callback_context.state["html_daily_pr"] = ""
    callback_context.state["html_detailed_plant_timeseries"] = ""


code_agent = SequentialAgent(
    name="code_agent",
    sub_agents=[parallel_code_pipeline, merger_agent],
    before_agent_callback=setup,
    after_agent_callback=save_generated_report_local,
)
