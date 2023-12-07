def reverse_string(input_string):
    return input_string[::-1]

def is_palindrome(input_string):
    reversed_str = reverse_string(input_string)
    return input_string == reversed_str

try:
    user_input = input("Enter a string: ")
    reversed_input = reverse_string(user_input)
    
    if is_palindrome(user_input):
        print(f"'{user_input}' is a palindrome.")
    else:
        print(f"'{user_input}' is not a palindrome.")
    
    print(f"Reversed string: '{reversed_input}'")
except ValueError:
    print("Invalid input.")
