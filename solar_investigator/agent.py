"""Top level agent for data agent multi-agents."""

from datetime import date
import os

from google.adk.agents import Agent
from google.adk.tools import load_artifacts
from google.genai import types

from .prompts import return_instructions_root
from .tools import call_investigator_agent

date_today = date.today()

model_name = os.getenv("ROOT_AGENT_MODEL")
if model_name is None:
    raise ValueError("Environment variable 'ROOT_AGENT_MODEL' must be set.")

root_agent = Agent(
    model=model_name,
    name="db_ds_multiagent",
    instruction=return_instructions_root(),
    global_instruction=(
        f"""
        You are a Data Science and Data Analytics Multi Agent System.
        Todays date: {date_today}
        """
    ),
    tools=[
        call_investigator_agent,
        load_artifacts,
    ],
    # before_agent_callback=setup_before_agent_call,
    generate_content_config=types.GenerateContentConfig(temperature=0.01),
)
