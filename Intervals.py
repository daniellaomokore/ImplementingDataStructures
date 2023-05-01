def meeting_rooms(intervals: List[Interval]) -> bool:
    # intervals: [(0,30),(5,10),(15,20)]
    # Write your code here
    intervals.sort(key=lambda interval: interval[0])  # sort the intervals based on their start time

    for index in range(len(intervals) - 1):
        interval1 = intervals[index]  # (0,30)
        interval2 = intervals[index + 1]  # (5,10)

        if interval2[0] < interval1[1]:  # if the start time of interval 2 is smaller than the end time of interval 1, they overlap
            return False
    return True