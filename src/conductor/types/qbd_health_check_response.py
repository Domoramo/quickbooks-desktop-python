# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["QbdHealthCheckResponse"]


class QbdHealthCheckResponse(BaseModel):
    duration: float
    """The time, in milliseconds, that it took to perform the health check."""
