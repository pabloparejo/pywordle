from secrets import choice
from colorama import Back, Fore, Style;

CORRECT = 0
PRESENT = 1
NOT_FOUND = 2

ROUNDS = 6
WORD_LEN = 5

word = choice([
    'juego', 'avion', 'plaza', 'solar', 'fresa', 'aguas', 'playa', 'monte', 'nieve',
    'avion', 'musgo', 'patos', 'suelo', 'dolor', 'peine', 'piano', 'papel'
]).upper();

rounds = 0;
found = False;

used_chars = {
    CORRECT: set(),
    PRESENT: set(),
    NOT_FOUND: set()
}

while not found and rounds <= ROUNDS:
    correct_chars_count = 0
    guess_status = [NOT_FOUND] * WORD_LEN;
    guess = input('Dime una palabra: ').upper()
    
    if not len(guess) == WORD_LEN:
        print('La palabra tiene que tener {} letras'.format(WORD_LEN))
        continue

    char_count = {}

    for char in word:
        char_count[char] = char_count.get(char, 0) + 1

    for (index, char) in enumerate(guess):
        if char == word[index]:
            char_count[char] -= 1
            guess_status[index] = CORRECT
            used_chars[CORRECT].add(char)
            try:
                used_chars[PRESENT].remove(char)
            except KeyError:
                pass

    for (index, char) in enumerate(guess):
        if char in word and guess_status[index] == NOT_FOUND and char_count[char] > 0:
            char_count[char] -= 1
            guess_status[index] = PRESENT
            used_chars[PRESENT].add(char)
        elif not char in word:
            used_chars[NOT_FOUND].add(char)

    word_to_print = ''
    for (index, status) in enumerate(guess_status):
        if status == CORRECT:
            correct_chars_count += 1
            word_to_print += Back.GREEN + ' ' + guess[index] + ' '
        elif status == PRESENT:
            word_to_print += Back.YELLOW + ' ' + guess[index] + ' '
        else:
            word_to_print += Back.RED + ' ' + guess[index] + ' '

    print(word_to_print + Style.RESET_ALL)

    if correct_chars_count == WORD_LEN:
        found = True
    else:
        rounds += 1
        help = ''
        if len(used_chars[CORRECT]) > 0:
            help += 'Correct: {} {} {} \t'.format(Back.GREEN, f' {Style.RESET_ALL} {Back.GREEN} '.join(sorted(used_chars[CORRECT])), Style.RESET_ALL)
        if len(used_chars[PRESENT]) > 0:
            help += 'Present: {} {} {} \t'.format(Back.YELLOW, f' {Style.RESET_ALL} {Back.YELLOW} '.join(sorted(used_chars[PRESENT])), Style.RESET_ALL)
        if len(used_chars[NOT_FOUND]) > 0:
            help += 'Not found: {} {} {}'.format(Back.RED, f' {Style.RESET_ALL} {Back.RED} '.join(sorted(used_chars[NOT_FOUND])), Style.RESET_ALL)

        print('\r\n' + help)
    

print()
if found:
    print(Fore.GREEN + '¡Enhorabuena!' + Style.RESET_ALL)
else:
    print(Fore.RED + '¡Lo siento!' + Style.RESET_ALL)