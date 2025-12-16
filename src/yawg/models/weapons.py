from __future__ import annotations
from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional

from .attributes import AttributeDef

class WeaponSlot(Enum):
    PRIMARY = auto()
    SECONDARY = auto()
    MELEE = auto()
    MISC = auto()

class WeaponAttributeConfig:
    """How a global attribute behaves on this weapon archetype."""

    attribute: AttributeDef
    enabled: bool = True
    weight_multiplier: float = 1.0

@dataclass
class WeaponBase:

    id: str
    name: str
    slot: WeaponSlot
    base_numbers: dict[str, float]
    attributes: dict[str, WeaponAttributeConfig]


# TODO: define Shotgun