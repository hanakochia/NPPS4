import pydantic

from . import item_model
from .. import const

from typing import Any


class UnitSupportItem(item_model.Item):
    add_type: const.ADD_TYPE = const.ADD_TYPE.UNIT
    new_unit_flag: bool = False
    is_support_member: bool = False
    is_hit: Any | None = None
    item_id: int
    unit_rarity_id: int

    @pydantic.computed_field
    @property
    def unit_id(self) -> int:
        return self.item_id


class UnitInfoBase(pydantic.BaseModel):
    unit_owning_user_id: int
    unit_rarity_id: int
    exp: int
    next_exp: int
    level: int
    level_limit_id: int
    max_level: int
    rank: int
    max_rank: int
    love: int
    max_love: int
    unit_skill_level: int
    max_hp: int
    favorite_flag: bool
    display_rank: int
    unit_skill_exp: int
    unit_removable_skill_capacity: int
    is_love_max: bool
    is_level_max: bool
    is_rank_max: bool
    is_signed: bool
    is_skill_level_max: bool
    is_removable_skill_capacity_max: bool
    insert_date: str = ""

    @pydantic.computed_field
    @property
    def skill_level(self) -> int:
        return self.unit_skill_level


class UnitInfoData(UnitInfoBase):
    unit_id: int


class UnitItem(UnitSupportItem, UnitInfoBase):
    removable_skill_ids: list[int] = pydantic.Field(default_factory=list)


type AnyUnitItem = UnitItem | UnitSupportItem


class OwningRemovableSkillInfo(pydantic.BaseModel):
    unit_removable_skill_id: int
    total_amount: int
    equipped_amount: int
    insert_date: str


class EquipRemovableSkillInfoDetail(pydantic.BaseModel):
    unit_removable_skill_id: int


class EquipRemovableSkillInfo(pydantic.BaseModel):
    unit_owning_user_id: int
    detail: list[EquipRemovableSkillInfoDetail]


class RemovableSkillOwningInfo(pydantic.BaseModel):
    owning_info: list[OwningRemovableSkillInfo]


class RemovableSkillInfoResponse(RemovableSkillOwningInfo):
    equipment_info: dict[str, EquipRemovableSkillInfo]


class SupporterInfoResponse(pydantic.BaseModel):
    unit_id: int
    amount: int


class SupporterListInfoResponse(pydantic.BaseModel):
    unit_support_list: list[SupporterInfoResponse]
