all_letters= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
def is_valid_word(word):
    """
    Check if the word is valid.
    A valid word contains only letters and is not empty.
    """
    return all(letter in all_letters for letter in word) and len(word) > 0
def test_is_valid_word():
    """
    Test the is_valid_word function.
    """
    assert is_valid_word("hello") == True, "Test Case 1 Failed"
    assert is_valid_word("HelloWorld") == True, "Test Case 2 Failed"
    assert is_valid_word("123") == False, "Test Case 3 Failed"
    assert is_valid_word("") == False, "Test Case 4 Failed"
    assert is_valid_word("hello123") == False, "Test Case 5 Failed"
    print("All test cases passed!")
if __name__ == "__main__":
    test_is_valid_word()
    print("Testing completed successfully.")
# This code defines a function to check if a word is valid and tests it with various cases.
# If the function passes all tests, it prints a success message.
# The function checks if the word contains only letters and is not empty.
# The test cases cover different scenarios to ensure the function works correctly.
# The code is structured to be run as a script, executing the tests when run directly.
# The code is designed to validate words based on specific criteria and includes a set of tests to ensure correctness.
print("hello world")
print("this is a test")