from uuid import UUID


class Tag:
    """
        A class to represent a Tag.

        ...

        Attributes
        ----------
        identifier : UUID
            the identifier of the tag
        name : str
            the name of the tag
        """
    def __init__(self, identifier: UUID, name: str):
        self.identifier: UUID = identifier
        self.name: str = name
