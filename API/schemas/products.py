from pydantic import BaseModel, model_validator


class ProductResponseSchema(BaseModel):
    name: str
    description: str
    calories: float
    fats: float
    carbs: float
    protein: float
    unsaturated_fats: float
    sugar: float
    salt: float
    portion: float

    @model_validator(mode='before')
    def validate_non_negative_values(cls, values):
        for field, value in values.items():
            if isinstance(value, (int, float)) and value < 0:
                raise ValueError(f"{field} can't be negative")
        return values
