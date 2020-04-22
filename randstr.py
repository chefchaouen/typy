#Generate an ostensibly random string.
import random

def main():
	pw = ""
	for i in range(1,22):
		pw += chr(random.randrange(48,126))
	print(pw)

if __name__=="__main__":
	main()	
