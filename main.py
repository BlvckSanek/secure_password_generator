import argparse
import random
import string
from typing import Optional, Tuple, Union


def generate_password(length: int,
                      use_letters: bool = True,
                      use_numbers: bool = True,
                      use_symbols: bool = True) -> str:
    """Generate a random password based on the specified criteria.

    Args:
        length: Length of the password.
        use_letters: Whether to include letters in the password (default True).
        use_numbers: Whether to include numbers in the password (default True).
        use_symbols: Whether to include symbols in the password (default True).

    Returns:
        str: The generated password.
    """
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def evaluate_password_strength(password: str) -> str:
    """Evaluate the strength of a password.

    Args:
        password: The password to evaluate.

    Returns:
        str: The strength of the password (weak, medium, strong).
    """
    length = len(password)
    variety = len(set(password))

    if length < 8 or variety < 5:
        return "weak"
    elif length < 12 or variety < 8:
        return "medium"
    else:
        return "strong"


def main():
    parser = argparse.ArgumentParser(description="Generate a random password.")
    parser.add_argument("length", type=int, help="Length of the password")
    parser.add_argument("-l", "--letters", action="store_true", help="Include letters in the password")
    parser.add_argument("-n", "--numbers", action="store_true", help="Include numbers in the password")
    parser.add_argument("-s", "--symbols", action="store_true", help="Include symbols in the password")

    args = parser.parse_args()

    password = generate_password(args.length, args.letters, args.numbers, args.symbols)
    strength = evaluate_password_strength(password)

    print(F"Generated Password: {password}")
    print(F"Password Strength: {strength}")


if __name__ == "__main__":
    main()
