# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["BillCheckPaymentDeleteResponse"]


class BillCheckPaymentDeleteResponse(BaseModel):
    id: str
    """The QuickBooks-assigned unique identifier of the deleted bill check payment."""

    deleted: bool
    """Indicates whether the bill check payment was deleted."""

    object_type: Literal["qbd_bill_check_payment"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"qbd_bill_check_payment"`."""

    ref_number: Optional[str] = FieldInfo(alias="refNumber", default=None)
    """
    The case-sensitive user-defined reference number of the deleted bill check
    payment.
    """
