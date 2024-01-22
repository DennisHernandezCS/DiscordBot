from random import choice, randint


def get_responses(user_input: str) -> str:
    """Return the bots response to the user input."""
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well, you\'re awfully quiet and dumb.'
    elif 'hello' in lowered or 'hi' in lowered:
        return 'Hello there!'
    elif 'bye' in lowered:
        return 'Bye!'
    elif 'how are you?' in lowered:
        return 'I am doing well, how about you?'
    elif 'roll dice' in lowered:
        return f'You rolled a {randint(1, 6)}'
    elif 'flip coin' in lowered:
        return choice(['Heads', 'Tails'])
    else:
        return choice(['I don\'t understand',
                       'What?',
                       'Huh?'])
