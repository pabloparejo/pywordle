from secrets import choice
from colorama import Back, Fore, Style;

word = choice([
    'JUEGO',
    'AVION',
    'CIELO',
    'COCHE',
    'TAZAS'
]);

rounds = 0;
found = False;

while not found and rounds <= 6:
	word_to_print = ''
	found_chars = 0
	guess = input('Dime una palabra: ').upper()
	for (index, char) in enumerate(guess):
		if char == word[index]:
			found_chars += 1
			word_to_print += Back.GREEN + f' {char} '
		elif char in word:
			word_to_print += Back.YELLOW + f' {char} '
		else:
			word_to_print += Back.RED + f' {char} '

	print(word_to_print + Style.RESET_ALL)

	if found_chars == len(word):
		found = True

print()
if found:
	print(Fore.GREEN + '¡Enhorabuena!' + Style.RESET_ALL)
else:
	print(Back.RED + '¡Perdiste!' + Style.RESET_ALL)