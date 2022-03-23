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

	for (index, char) in enumerate(guess):
		if char in word and guess_status[index] == NOT_FOUND and char_count[char] > 0:
			char_count[char] -= 1
			guess_status[index] = PRESENT

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

print()
if found:
	print(Fore.GREEN + '¡Enhorabuena!' + Style.RESET_ALL)
else:
	print(Back.RED + '¡Perdiste!' + Style.RESET_ALL)