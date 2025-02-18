from dataclasses import dataclass


@dataclass
class ProductItem:
    name: str
    description: str
    calories: float
    fats: float
    carbs: float
    protein: float
    unsaturated_fats: float
    sugar: float
    salt: float
    portion: int
