from google.adk.tools.tool_context import ToolContext


def append_problematic_rows(rows: str, tool_context: ToolContext):
    """tools to store problematic rows
    parameters
    String rows : the json response for the problematic five minutes data eg. "{problematic_five_minutes_pr : [row_data_here] ,analysis : "A general explaination on why you think these data is abnormal}"
    """
    if "problematic_five_minutes_pr" not in tool_context.state:
        problematic_five_minutes_pr_settings = []
        tool_context.state["problematic_five_minutes_pr"] = (
            problematic_five_minutes_pr_settings
        )

    problematic_five_minutes_pr_settings = tool_context.state[
        "problematic_five_minutes_pr"
    ]
    problematic_five_minutes_pr_settings.append(rows)
    tool_context.state["problematic_five_minutes_pr"] = (
        problematic_five_minutes_pr_settings
    )
