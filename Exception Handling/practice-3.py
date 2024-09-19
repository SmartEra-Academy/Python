numbers = [1, 2, [1, 2, 3], 4, 'a', 5]

for num in numbers:
    try:
        result = num + 2
        print(f"Result: {result}")

    except TypeError:
        print(f"Can't add two different data types together")

    except Exception as e:
        print(f"Unexpected Error: {e}")
