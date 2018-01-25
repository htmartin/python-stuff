import sys
import random
if len(sys.argv) <2:
	print ("Please supply a flash card file.")
	exit(1)
flashcard_filename = sys.argv[1]
f = open(flashcard_filename, "r")
question_dict = {}
for line in f:
	entry = line.strip().split(",")
	question = entry[0]
	answer = entry[1]
	question_dict[question] = answer
f.close()