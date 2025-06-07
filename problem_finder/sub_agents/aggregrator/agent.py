from google.adk.agents import Agent

from .prompts import return_instruction_aggregator

aggregrator_agent = Agent(
    name="aggregrator",
    model="gemini-2.0-flash-001",
    description="You are an expert in summarizing problems",
    instruction=return_instruction_aggregator(),
)
