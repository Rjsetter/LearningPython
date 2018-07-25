#_*_ encoding:utf-8_*_
def is_palindrome(st):
	if st == st[::-1]:
		print("It's a palindrome!")
	else:
		print("It's not a plindrome!")



sta=input("Please input the string:")
is_palindrome('sta')
