import pytz
from datetime import datetime

STREAK_TTL_SECONDS = 24 * 60 * 60 # 24 hrs

def time_ago(uploadDate):
    tz = pytz.timezone("Asia/Kolkata")

    periods = ["s", "min", "h", "d", "w", "m", "y", "decade"]
    lengths = [60, 60, 24, 7, 4.35, 12, 10]
    now = datetime.strptime(datetime.now(tz=tz).strftime(
        "%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
    unix_date = datetime.strptime(uploadDate, "%Y-%m-%d %H:%M:%S") if isinstance(uploadDate, str) else uploadDate

    if now > unix_date:
        difference = now - unix_date
        tense = ""
    else:
        difference = unix_date - now
        tense = "from now"

    j = 0
    difference = difference.total_seconds()
    while difference >= lengths[j] and j < len(lengths) - 1:
        difference /= lengths[j]
        j += 1

    difference = round(difference)
    return f"{difference}{periods[j]} {tense}"

def str2date(strdate: str):
    return datetime.strptime(strdate, "%Y-%m-%d").date()
