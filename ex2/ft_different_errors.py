#!/usr/bin/env python3

def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "abc" + 123
    else:
        return


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    i = 0
    while i < 5:
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
            print("Operation completed successfully")
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
        i += 1

    print("\nTesting multiple errors with one try block...")
    i = 0
    while i < 4:
        try:
            garden_operations(i)
        except (ValueError, ZeroDivisionError, FileNotFoundError,
                TypeError) as e:
            print(f"Caught an error in operation {i}: {e}")
        i += 1


if __name__ == "__main__":

    test_error_types()
    print()
    print("All error types tested successfully!")
