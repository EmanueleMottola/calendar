from uuid import UUID
from datetime import datetime
import Tag


class Activity:
    """
        A class to represent an Activity.

        ...

        Attributes
        ----------
        identifier : UUID
            the identifier of the activity
        name : str
            the name of the activity
        from_time: datetime
            the starting time of the activity
        end_time: datetime
            the ending time of the activity
        tag: Tag
            the associated tag of the activity
        """
    def __init__(self, identifier: UUID, name: str, from_time: datetime, end_time: datetime, tag: Tag):
        self.identifier: UUID = identifier
        self.name: str = name
        self.from_time: datetime = from_time
        self.end_time: datetime = end_time
        self.tag: Tag = tag
