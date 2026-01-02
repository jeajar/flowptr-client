"""Filter models for Flow Production Tracking search operations.

These models represent filter conditions used in search and query operations.
They follow the Flow Production Tracking API filter specification.
"""

from collections.abc import Sequence
from typing import Any, Union

from pydantic import BaseModel, ConfigDict, Field


class FilterCondition(BaseModel):
    """Basic filter condition following Flow PTR specs.

    A filter condition specifies a field, comparison operator, and value
    to filter entity records.

    Examples:
        >>> # Filter for projects with status "Active"
        >>> FilterCondition(field="sg_status", relation="is", value="Active")
        >>>
        >>> # Filter for shots created after a date
        >>> FilterCondition(
        ...     field="created_at", relation="greater_than", value="2024-01-01"
        ... )

    Attributes:
        field: Field name to filter on
        relation: Comparison operator (is, is_not, contains, greater_than, etc.)
        value: Value to compare against (type depends on field)
    """

    field: str = Field(..., description="Field name to filter on")
    relation: str = Field(..., description="Comparison operator")
    value: Any = Field(..., description="Value to compare against")

    model_config = ConfigDict(frozen=True)


class ComplexFilter(BaseModel):
    """Complex filter with logical operators following Flow PTR specs.

    Complex filters allow combining multiple conditions with AND/OR logic
    and support nesting for advanced query construction.

    Examples:
        >>> # Projects: active AND have code starting with "DEMO"
        >>> ComplexFilter(
        ...     logical_operator="and",
        ...     conditions=[
        ...         FilterCondition(
        ...             field="sg_status", relation="is", value="Active"
        ...         ),
        ...         FilterCondition(
        ...             field="code", relation="starts_with", value="DEMO"
        ...         )
        ...     ]
        ... )
        >>>
        >>> # Nested: Active OR (Hold AND High priority)
        >>> ComplexFilter(
        ...     logical_operator="or",
        ...     conditions=[
        ...         FilterCondition(
        ...             field="sg_status", relation="is", value="Active"
        ...         ),
        ...         ComplexFilter(
        ...             logical_operator="and",
        ...             conditions=[
        ...                 FilterCondition(
        ...                     field="sg_status", relation="is", value="Hold"
        ...                 ),
        ...                 FilterCondition(
        ...                     field="sg_priority", relation="is", value="High"
        ...                 )
        ...             ]
        ...         )
        ...     ]
        ... )

    Attributes:
        logical_operator: Logical operator combining conditions ("and" or "or")
        conditions: List of filter conditions or nested complex filters
    """

    logical_operator: str = Field(
        ..., pattern="^(and|or)$", description="Logical operator (and/or)"
    )
    conditions: Sequence[Union["ComplexFilter", FilterCondition]] = Field(
        ..., min_length=1, description="Filter conditions to combine"
    )

    model_config = ConfigDict(frozen=True)
