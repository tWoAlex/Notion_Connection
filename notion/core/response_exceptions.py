class BadRequest(ValueError):
    """4xx"""
    def __init__(self, *args: object) -> None:
        """4xx"""
        super().__init__(*args)


class Unauthorized(Exception):
    """401"""
    def __init__(self, *args: object) -> None:
        """401"""
        super().__init__('Your token is broken')


class Restricted(Exception):
    """403"""
    def __init__(self, *args: object) -> None:
        """403"""
        super().__init__('This object is restricted')


class NotFoundError(LookupError):
    """404"""
    def __init__(self, *args: object) -> None:
        """404"""
        super().__init__('Object with this id not found')


class NotionIsIll(Exception):
    """5xx"""
    def __init__(self, *args: object) -> None:
        """5xx"""
        super().__init__(*args)
