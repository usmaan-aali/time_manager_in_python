import helpers as h
from timeRange import TimeRange
from friend import Friend


def main():
    available_minutes = list(range(1440))
    f1 = Friend("ali")
    f1.add_busy_ranges(TimeRange(start_time="08:00",end_time="10:00"))
    f2 = Friend("jim")
    f2.add_busy_ranges(TimeRange(start_time="11:00",end_time="12:00"))
    for m in available_minutes[:]:
        for r in Friend.all_busy_minutes_ranges:
            if m in r:
                # if the minutes range is already removed from available minutes the except will handle the error and pass 
                try:
                    available_minutes.remove(m)
                except ValueError:
                    pass

    for tr in h.prettify_available_minutes(available_minutes):
        print(f"You can meet in {tr}")
if __name__ == "__main__":
    main()