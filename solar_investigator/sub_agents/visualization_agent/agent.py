"""Data Science Agent V2: generate nl2py and use code interpreter to run the code."""

import os

from google.adk.agents import Agent

from .prompts import return_instructions_ds

model_name = os.getenv("ANALYTICS_AGENT_MODEL")
if model_name is None:
    raise ValueError("Environment variable 'ANALYTICS_AGENT_MODEL' must be set.")

root_agent = Agent(
    model=model_name,
    name="visualization_agent",
    instruction=return_instructions_ds(),
    # code_executor=VertexAiCodeExecutor( #TODO: setup code executor
    #     optimize_data_file=True,
    #     stateful=True,
    # ),
)
