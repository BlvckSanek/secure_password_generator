import argparse
import random
import string


def concoct_secret_formula_of_ultimate_power(length: int) -> str:
    """
    Concoct a secret formula of ultimate power (a.k.a. generate a random password).

    This function harnesses the mystical forces of randomness to create a password
    so powerful that even the most nefarious hackers would tremble in awe.

    Args:
        length (int): The desired length of the password.

    Returns:
        str: The mystical password of ultimate power.
    """
    magical_characters = string.ascii_letters + string.digits + string.punctuation
    magic_word = ''.join(random.choice(magical_characters) for _ in range(length))
    return magic_word


def gauge_password_strength(password: str) -> str:
    """
    Gauge the strength of a password.

    By analyzing the intricate patterns and complexities of the password,
    this function determines whether it possesses the strength of a mighty dragon
    or the feebleness of a newborn kitten.

    Args:
        password (str): The password to be evaluated.

    Returns:
        str: A poetic description of the password's strength.
    """
    length = len(password)
    entropy = len(set(password))  # Measure of chaos and unpredictability

    if length < 8 or entropy < 5:
        return "Your password is as weak as a dandelion in a hurricane."
    elif length < 12 or entropy < 8:
        return "Your password is as sturdy as a wooden sword."
    else:
        return "Your password is as mighty as the hammer of Thor!"


def main():
    """
    The main enchantment ceremony.

    This enchantment ceremony invokes the powers of the password generator,
    harnessing its arcane magic to summon forth a password of unparalleled strength
    and security.

    """
    incantation_parser = argparse.ArgumentParser(description="Summon forth a mighty password!")
    incantation_parser.add_argument("length", type=int, help="Length of the password")
    incantation_parser.add_argument("-l", "--letters", action="store_true", help="Include letters in the password")
    incantation_parser.add_argument("-n", "--numbers", action="store_true", help="Include numbers in the password")
    incantation_parser.add_argument("-s", "--symbols", action="store_true", help="Include symbols in the password")

    magic_words = incantation_parser.parse_args()

    magic_password = concoct_secret_formula_of_ultimate_power(magic_words.length)
    enchantment_strength = gauge_password_strength(magic_password)

    print("Behold, the mystical password of ultimate power:", magic_password)
    print("Strength of the enchantment:", enchantment_strength)


if __name__ == "__main__":
    main()
