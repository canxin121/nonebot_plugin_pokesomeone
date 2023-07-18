from typing import List

from nonebot import get_driver
from pydantic import BaseSettings


class Config(BaseSettings):
    """白名单不可被戳"""
    po_white_list: List = []
    """黑名单不可使用,可为群或qq 号"""
    po_black_list: List = []
    """最多戳的次数"""
    po_max: int = 3

    class Config:
        extra = "ignore"


config = Config.parse_obj(get_driver().config)
