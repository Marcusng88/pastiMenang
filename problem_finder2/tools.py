from google.adk.tools import ToolContext
from google.adk.tools.agent_tool import AgentTool

from .sub_agents import (
    daily_inverter_agent,
    daily_pr_agent,
    detailed_inverter_performance_agent,
    detailed_plant_timeseries_agent,
)


async def call_daily_pr_agent(
    question: str,
    tool_context: ToolContext,
):
    """Tools to call daily pr agent . Please provide date to be investigated

    Parameters
    String start time : time starting to be investigated
    String end time : time end to be investigated
    String plant name : name of the plant to be investigated
    String plant id : id of the plant

    """
    agent_tool = AgentTool(agent=daily_pr_agent)

    daily_pr_agent_output = await agent_tool.run_async(
        args={"request": question}, tool_context=tool_context
    )
    tool_context.state["daily_pr_agent_output"] = daily_pr_agent_output
    return daily_pr_agent_output


async def call_detailed_plant_timeseries_agent(
    question: str,
    tool_context: ToolContext,
):
    """Tools to call detailed plant timseries agent .

    Parameters
    list of target dates : target dates to be investigated
    String plant id : id of the plant

    """
    agent_tool = AgentTool(agent=detailed_plant_timeseries_agent)

    detailed_plant_timeseries_agent_output = await agent_tool.run_async(
        args={"request": question}, tool_context=tool_context
    )
    tool_context.state["detailed_plant_timeseries_agent_output"] = (
        detailed_plant_timeseries_agent_output
    )
    return detailed_plant_timeseries_agent_output


async def call_daily_inverter_agent(
    question: str,
    tool_context: ToolContext,
):
    """Tools to call daily inverter agent .

    Parameters
    list of target dates : target dates to be investigated
    String plant id : id of the plant

    """
    agent_tool = AgentTool(agent=daily_inverter_agent)

    daily_inverter_agent_output = await agent_tool.run_async(
        args={"request": question}, tool_context=tool_context
    )
    tool_context.state["daily_inverter_agent_output"] = daily_inverter_agent_output
    return daily_inverter_agent_output


async def call_detailed_inverter_performance_agent(
    question: str,
    tool_context: ToolContext,
):
    """Tools to call detailed inverter performance agent to get know the performance of specific device .

    Parameters
    dictionary : a dictionary of device id of the plant associated with the dates to check

    """
    agent_tool = AgentTool(agent=detailed_inverter_performance_agent)

    detailed_inverter_performance_agent_output = await agent_tool.run_async(
        args={"request": question}, tool_context=tool_context
    )
    tool_context.state["detailed_inverter_performance_agent_output"] = (
        detailed_inverter_performance_agent_output
    )
    return detailed_inverter_performance_agent_output
