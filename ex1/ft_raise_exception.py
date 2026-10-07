#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    temperature = int(temp_str)

    if temperature > 40:
        raise ValueError(f"{temperature}°C is too hot for plants (max 40°C)")
    elif temperature < 0:
        raise ValueError(f"{temperature}°C is too cold for plants (min 0°C)")

    return temperature


def test_temperature() -> None:
    temperature = input_temperature("25")
    print("Input data is '25'")
    print(f"Temperature is now {temperature}°C")
    print()

    try:
        print("Input data is 'abc'")
        temperature = input_temperature("abc")
    except Exception as e:
        print("Caught input_temperature error:", e)
    print()

    try:
        print("Input data is '100'")
        temperature = input_temperature("100")
    except Exception as e:
        print("Caught input_temperature error:", e)
    print()

    try:
        print("Input data is '-50'")
        temperature = input_temperature("-50")
    except Exception as e:
        print("Caught input_temperature error:", e)


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    test_temperature()
    print()
    print("All tests completed - program didn't crash!")
