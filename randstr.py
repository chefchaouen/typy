import random, sys, argparse

def main():
	nums = [chr(i) for i in range(48,58)]
	upper_case_letters = [chr(i) for i in range(65,91)]
	lower_case_letters = [chr(i) for i in range(97,123)]
	symbols = [chr(i) for i in range(33,48)]
	symbols += [chr(i) for i in range(59,64)]
	pw = ""
	pw_char_lists = []
	pw_char_lists += nums
	if args.character_set[0] >= 1:
		pw_char_lists += upper_case_letters
		pw_char_lists += lower_case_letters
	if args.character_set[0] > 1:
		pw_char_lists += symbols
	
	for i in range(1,args.length[0]):
		selected_pw_char_list = random.choice(pw_char_lists)
		pw_char = random.choice(selected_pw_char_list)
		pw += pw_char

	print(pw)

if __name__ == "__main__":
	parser = argparse.ArgumentParser(prog="TyRandString", description="Generates"
						+ " a string containing random characters that can be"
						+ "used for passwords.")
	parser.add_argument("length", help="specify length of string to generate.",
						nargs=1, type=int, action="store")
	parser.add_argument("character_set", help="set the types of characters"
						+ " you want to include in the string. You can choose"
						+ " from letters (includes upper and lower case)"
						+ " only (0), or to also include numbers (1), or to"
						+ " also further include symbols (2). Use 0, 1, and 2" 
						+ " correspondingly to choose the desired character set.",
						nargs=1, type=int, action="store")
	args = parser.parse_args()
	main()