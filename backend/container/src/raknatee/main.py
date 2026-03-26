from typing import TypedDict


class Car(TypedDict):
    serial_number: str
    n_door: int
    color: str

def main()->None:
    data = plus(1, 2)
    print(data)
    car: Car = {
        "color": "red",
        "n_door": 4,
        "serial_number": "ad1234"
    }
    print(car)


def plus(a: int|float, b: int|float)->int|float:
    return a+b


main()



