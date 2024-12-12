# Python3 program for the above approach

# Function to obtain the length of
# the longest palindromic substring
def longestPalSubstr(str):
	
	# Length of given string
	n = len(str)

	# Stores the maximum length
	maxLength = 1
	start = 0

	# Iterate over the string
	for i in range(len(str)):

		# Iterate over the string
		for j in range(i, len(str), 1):
			flag = 1

			# Check for palindrome
			for k in range((j - i + 1) // 2):
				if (str[i + k] != str[j - k]):
					flag = 0

			# If string [i, j - i + 1]
			# is palindromic
			if (flag != 0 and
			(j - i + 1) > maxLength):
				start = i
				maxLength = j - i + 1
			
	# Return length of LPS
	return maxLength

# Driver Code

# Given string
str = "abcccdd"

# Function call
print(longestPalSubstr(str))

# This code is contributed by code_hunt
