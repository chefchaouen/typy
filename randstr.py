# Generate an ostensibly random string
# with equal probability of each character
# being either a letter, number, or special
# character

import random
import sys

def main():
	nums = [chr(i) for i in range(48,58)]
	upper_case_letters = [chr(i) for i in range(65,91)]
	lower_case_letters = [chr(i) for i in range(97,123)]
	symbols = [chr(i) for i in range(33,48)]
	symbols += [chr(i) for i in range(59,64)]
	pw = ""
	pw_char_lists = [nums,upper_case_letters,lower_case_letters, symbols]
	
	for i in range(1,20):
		selected_pw_char_list = pw_char_lists[random.randrange(0,len(pw_char_lists))]
		pw_char = random.choice(selected_pw_char_list)
		pw += pw_char

	print(pw)

if __name__=="__main__":
		main()