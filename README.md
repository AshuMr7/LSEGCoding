# Explanation

Retrieves the value from a nested dictionary based on a '/' separated key.

:param obj: The nested dictionary object <br>
:param key: The '/' separated key path <br>
:return: The value at the specified key path or None if not found <br>

# Output:

python3 test.py <br>

Test 1: Key='a/b/c' -> Expected: d, Got: d <br>
Test 2: Key='x/y/z' -> Expected: a, Got: a <br>
Test 3: Key='p/q/r/s' -> Expected: t, Got: t <br>
Test 4: Key='a/b/x' -> Expected: None, Got: None <br>
Test 5: Key='a' -> Expected: {'b': {'c': 'd'}}, Got: {'b': {'c': 'd'}} <br>
Test 6: Key='a/b/c' -> Expected: None, Got: None <br>
All test cases passed! <br>

## Note: Added a few tests and this doesn't use any libraries.
