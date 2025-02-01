def get_nested_value(obj, key):
    keys = key.split("/")
    for k in keys:
        if not isinstance(obj, dict) or k not in obj:
            return None
        obj = obj[k]
    return obj

# Test cases
def test_get_nested_value():
    test_cases = [
        ("Test 1", {"a": {"b": {"c": "d"}}}, "a/b/c", "d"),
        ("Test 2", {"x": {"y": {"z": "a"}}}, "x/y/z", "a"),
        ("Test 3", {"p": {"q": {"r": {"s": "t"}}}}, "p/q/r/s", "t"),
        ("Test 4", {"a": {"b": {"c": "d"}}}, "a/b/x", None),
        ("Test 5", {"a": {"b": {"c": "d"}}}, "a", {"b": {"c": "d"}}),
        ("Test 6", {}, "a/b/c", None),
    ]

    for test_name, obj, key, expected in test_cases:
        result = get_nested_value(obj, key)
        print(f"{test_name}: Key='{key}' -> Expected: {expected}, Got: {result}")
        assert result == expected, f"{test_name} failed"
    print("All test cases passed!")

test_get_nested_value()