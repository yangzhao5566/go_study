# coding=utf-8
from dataclasses import dataclass
from typing import ClassVar
from typing import NewType
from typing import Dict
from typing import List

Vector = List[float]


def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]


print(scale(2.0, [1.0, 2.3, 3.4]))


UserId = NewType("UserId", int)

one_id = UserId(333)
print(one_id)
print(type(one_id))

@dataclass
class User:
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand


user = User("zhang", 22.22, 3)
print(user.total_cost())


def greeting(name:str) -> None:
    print("Hello " + name)

greeting("zhangsan")


def get_user_name(user_id: UserId) -> None:
    print(user_id)

get_user_name(one_id)

get_user_name(2)   # 这样不会报错

get_user_name("zhangsan")


import contextvars

my_var = contextvars.ContextVar("my_var", default=42)
print(my_var)
print(my_var.set("33"))

from fabric.api import local


