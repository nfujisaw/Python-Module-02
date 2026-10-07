#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    return int(temp_str)


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


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    test_temperature()
    print()
    print("All tests completed - program didn't crash!")
