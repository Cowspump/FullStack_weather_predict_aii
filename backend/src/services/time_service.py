from datetime import datetime, timedelta
from typing import List

def get_current_time() -> List[str]:
    hours = []
    now = datetime.now().astimezone().replace(minute=0, second=0, microsecond=0)

    for hour_later in range(6):
        cur_time = now + timedelta(hours=hour_later)
        hours.append(cur_time.isoformat())

    return hours
