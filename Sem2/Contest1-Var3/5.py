class TimeRange:
    def __init__(self, start, end):
        if start >= end:
            raise ValueError("Start should be less than end!")
        self.start = start
        self.end = end
        
    def overlaps(self, other: "TimeRange") -> bool:
        return (self.start >= other.start and self.start < other.end) or (self.end >= other.start and self.end <= other.end) or (self.start >= other.start and self.end <= other.end)
   
    def intersection(self, other: "TimeRange") -> "TimeRange" | None:
        start, end = max(self.start, other.start), min(self.end, other.end)
        if start < end:
            return TimeRange(start, end)
        return None