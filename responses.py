from random import choice, randint


def advanced_dice_roll(user_input: str) -> str:
    """
    Return the result of a die roll with modifiers.
    ":param user_input: The user's input.
        Acceptable inputs:
        - 1d6
        - 1d20
        - 3d6
    ":return: The result of the dice roll.
    """
    if user_input == '1d6':
        return f'You rolled a {randint(1, 6)}'
    elif user_input == '1d20':
        return f'You rolled a {randint(1, 20)}'
    elif user_input == '3d6':
        d1 = randint(1, 6)
        d2 = randint(1, 6)
        d3 = randint(1, 6)
        return f'You rolled a {d1 + d2 + d3} ({d1}, {d2}, {d3})'
    else:
        return 'I don\'t understand'
    # future, maybe: add ability to roll any option of dice, but don't care right now


def get_greeting() -> str:
    """Return a greeting."""
    return choice(['Hello there!',
                   'Hi!',
                   'Hey!'])


def get_responses(user_input: str) -> str:
    """Return the bots response to the user input."""
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well, you\'re awfully quiet and dumb.'
    elif 'hello' in lowered or 'hi' in lowered:
        return get_greeting()
    elif 'bye' in lowered:
        return 'Bye!'
    elif 'how are you?' in lowered:
        return 'I am doing well, how about you?'
    elif 'roll' in lowered:
        lowered = lowered.replace('roll', '').strip()
        return advanced_dice_roll(lowered)
    elif 'flip coin' in lowered:
        return choice(['Heads', 'Tails'])
    else:
        return choice(['I don\'t understand',
                       'What?',
                       'Huh?'])
