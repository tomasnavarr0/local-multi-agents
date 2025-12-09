from datetime import datetime
from agent_framework import ai_function

@ai_function(name="time_tool", description="Retrieves the actual time")
def get_time() -> str:
    time = datetime.now()
    return f"The hour is {time.hour}:{time.minute}"