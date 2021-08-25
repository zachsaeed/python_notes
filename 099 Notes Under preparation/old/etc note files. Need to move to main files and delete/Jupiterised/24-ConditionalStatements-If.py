# Conditional logic using if statements represent different paths a 
# program can take based on dome type of comparision output
#
# Format:
# Note colon at the end of each conditional check
# if <boolean condition> : 	# start of conditional statement. mandatory
# 	execution
# elif <boolean condition> : # rest of the conditional logics. optional
# 	execution
# else: 					# end of conditional statement. Default incase all conditional logics above fail. optional
# 	execution	 	
#

color = input("Whats your favourite color?")
if color == 'purple':
	print("Excelent choice")
elif color == 'teal':
	print('o bad!')	
elif color == 'seafoam':
	print('mediocre')		
elif color == 'pure darkness':
	print('I like how you think')
else:
	print('YOU MONSTER')
