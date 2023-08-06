from pydantic import BaseModel, Field, confloat, conint


class DimenssionDTO(BaseModel):
    height: conint(gt=0, lt=1000) = Field(
        gt=0,
        lt=1000,
        description="O valor da altura precisa ser maior do que 0 e menor do que 1000",
        examples=[102, 140],
    )
    width: conint(gt=0, lt=1000) = Field(
        gt=0,
        lt=1000,
        description="O valor da largura precisa ser maior do que 0 e menor do que 1000",
        examples=[40, 90],
    )


class ShippingRequestDTO(BaseModel):
    dimension: DimenssionDTO
    weight: conint(gt=0) = Field(
        gt=0,
        description="O valor do peso precisa ser maior do que 0",
        examples=[400],
    )


class ShippingOutputDTO(BaseModel):
    name: str = Field(title="Modalidade do frete")
    value: confloat(ge=0.0) = Field(
        ge=0.0, description="Valor do frete", examples=[12.0]
    )
    shipping_deadline: conint(gt=0) = Field(
        gt=0, description="Prazo de entrega", examples=[6]
    )


class ShippingInputDTO(BaseModel):
    name: str
    shipping_rate: confloat(ge=0.1)
    minimum_height: conint(gt=0, lt=1000)
    maximum_height: conint(gt=0, lt=1000)
    minimum_width: conint(gt=0, lt=1000)
    maximum_width: conint(gt=0, lt=1000)
    shipping_deadline: conint(gt=0, lt=1000)
