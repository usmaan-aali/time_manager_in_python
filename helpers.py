def timerange_to_minutes(time_str):
    """
    Return amount of minutes for given time range in HH:MM format
    """
    hour = int(time_str.split(":")[0])
    minutes = int(time_str.split(":")[1])
    
    hour_to_minutes = hour * 60
    return hour_to_minutes + minutes

def minutes_to_timerange(m):
    # Return a time range string in format: HH:MM for given integer
    # m = 90 -> 01:30
    hour = m // 60
    hour_str = f"{hour:02d}"
    minutes = m % 60
    minutes_str = f"{minutes:02d}"

    return f"{hour_str}:{minutes_str}"

def prettify_available_minutes(l:list):
    grouped_list = [] # nested list
    list_ressetable = []
    # Group the list so that: [[0,1,2],[60,61,62]]
    for element in l:
        if list_ressetable == []:
            list_ressetable.append(element)
            continue
        if list_ressetable[-1]+1 == element:
            list_ressetable.append(element)
        else:
            grouped_list.append(list_ressetable[:])
            list_ressetable.clear()
            list_ressetable.append(element)
    grouped_list.append(list_ressetable)

    time_ranges = []
    for group in grouped_list:
        start_time = minutes_to_timerange(m=group[0])
        end_time = minutes_to_timerange(m=group[-1])
        time_range_str = f"{start_time} - {end_time}"
        time_ranges.append(time_range_str)
    return time_ranges

