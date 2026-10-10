from datetime import datetime
import pytz

def run_pytz():
    tz = pytz.timezone("Europe/Kyiv")
    current_time = datetime.now(tz)
    print("[Pytz] Час у Києві:", current_time.strftime("%Y-%m-%d %H:%M:%S"))
