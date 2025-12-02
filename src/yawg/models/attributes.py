from __future__ import annotations
from dataclasses import dataclass
from enum import Enum, auto

#TODO: reseach actual in-game types
class StatValueType(Enum):
    PERCENT = auto()
    FLAT = auto()
    BOOL = auto()


@dataclass
class AttributeDef:
    """
    Generic Weaponm Attribute interface.
    Example: damage%, extra double jump, can random crit 
    """
    id: str
    name: str
    description: str
    value_type: StatValueType

    # Add min max?
    base_weight: float