# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: MealPrepBox
from dataclasses import dataclass, field
from datetime import date
from typing import Optional, List


@dataclass
class Container:
    name: str
    capacity_ml: int
    material: str = "glass"
    is_freezer_safe: bool = True


@dataclass
class Batch:
    name: str
    recipe_id: int
    prepared_date: date
    container: Container
    servings: int
    notes: str = ""


@dataclass
class FreezerInventory:
    batch: Batch
    frozen_date: date
    thawed_date: Optional[date] = None
    reheating_instructions: Optional[str] = None
    consumed: bool = False


@dataclass
class MealPlan:
    date: date
    meals: List[Meal] = field(default_factory=list)


@dataclass
class Meal:
    batch: Batch
    portion: int
    reheating_instructions: Optional[str] = None
