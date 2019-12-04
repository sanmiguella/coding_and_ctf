#!/usr/bin/python
from pwn import *
import operator

#http://docs.pwntools.com/en/stable/tubes.html
conn = remote('10.0.2.83', 1337)

#https://stackoverflow.com/questions/1740726/turn-string-into-operator
ops = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.div }

def main():
	for count in range(1,1002): # Loops 1001 times
		banner(count) # Prints info on the current loop
		
		question = conn.recvrepeat(0.2) # Get the current question
		answer(question) # Pass the answering of the current question to a function
	
	# After 1001 loops prints `gift` to the output
	gift = conn.recvrepeat(0.2) 
	print "\n" + gift
		
			
def banner(message):
	# Banner to know the number of time we have answered the question
	print "\n" + "=" * 15
	print "Attempt : " + str(message)
	print "=" * 15	

def answer(question):
	#https://github.com/sanmiguella/coding_and_ctf/blob/master/Memory_corruption/Intermediate/aslr_multistage/exploit.py
	for line in question.split("\n"): # If there are multiple lines in the question, splits it.
		if ", " in line: # Format: (5, '*', 7)
		    first_operand = int( line[1 : 2] ) # Get the first number, convert from str to int
		    second_operand = int( line[-2 : -1] ) # Get the second number, convert from str to int
		    operator = line[5 : 6] # Get the math operator

		    result = str( ops[operator](first_operand, second_operand) )

		    # Prints the calculated result to the output
		    print str(first_operand) + ' ' + operator + ' ' + str(second_operand) + ' = ' + str(result)

		    conn.sendline(result) # Sends the calculated answer back to the server

if __name__ == "__main__": 
	main()
