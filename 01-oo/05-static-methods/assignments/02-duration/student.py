class Duration:
    def __init__(self, total_seconds):
        self._total_seconds = total_seconds

    @staticmethod
    def from_seconds(seconds):
        return Duration(seconds)

    @staticmethod
    def from_minutes(minutes):
        return Duration(minutes * 60)

    @staticmethod
    def from_hours(hours):
        return Duration(hours * 3600)

    @property
    def seconds(self):
        return self._total_seconds

    @property
    def minutes(self):
        return self._total_seconds / 60

    @property
    def hours(self):
        return self._total_seconds / 3600

    def __repr__(self):
        return f"Duration({self._total_seconds} seconds)"
