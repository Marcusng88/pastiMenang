from google.adk.tools.tool_context import ToolContext


def append_problematic_rows(rows: str, tool_context: ToolContext):
    """tools to store problematic inverter rows
    parameters
    String rows : the json response for the problematic five minutes data eg. "{problematic_daily_inverter : [row_data_here] ,analysis : "A general explaination on why you think these inverters is abnormal}"
    """
    if "problematic_daily_inverter" not in tool_context.state:
        problematic_daily_inverter_settings = []
        tool_context.state["problematic_daily_inverter"] = (
            problematic_daily_inverter_settings
        )

    problematic_daily_inverter_settings = tool_context.state[
        "problematic_daily_inverter"
    ]
    problematic_daily_inverter_settings.append(rows)
    tool_context.state["problematic_daily_inverter"] = (
        problematic_daily_inverter_settings
    )
