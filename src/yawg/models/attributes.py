from __future__ import annotations
from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional


class StatValueType(Enum):
    PERCENT = auto()
    FLAT = auto()
    BOOL = auto()


@dataclass
class AttributeDef:
    """
    Generic Weapon Attribute interface.
    Example: damage%, extra double jump, can random crit 
    """
    id: str
    name: str
    description: str
    value_type: StatValueType
    min_value: Optional[float] = None
    max_value: Optional[float] = None
    base_weight: float = 1.0

    def get_description(self):
        return self.description

DAMAGE_PERCENT = AttributeDef(
    id="damage_percent",
    name="Damage modifier",
    description="Modifies the damage dealt by a percentage.",
    value_type=StatValueType.PERCENT,
)

CLIP_SIZE_PERCENT = AttributeDef(
    id="clip_size_percent",
    name="Clip size",
    description="Modifies the ammo count in the clip by a percentage.",
    value_type=StatValueType.PERCENT,
)

ATTRIBUTE_LIBRARY = {
    DAMAGE_PERCENT.id: DAMAGE_PERCENT,
    CLIP_SIZE_PERCENT.id: CLIP_SIZE_PERCENT,
}
