def Graduation_Probability(n, m=4):
	"""n is the total days to the graduation and m is the max number of leaves"""
        
	#Empty nested arrays
	days_present = [[0] * (m + 1) for _ in range(n + 1)]
        
	#Fill the first nested list with 1 as the base case
	for i in range(m):
		days_present[0][i] = 1
            
	for i in range(1, n + 1):
		for j in range(m - 1, -1, -1):
			days_present[i][j] = days_present[i - 1][0] + days_present[i - 1][j + 1]
        
    # The number of ways to attend classes over N days.
	x1 = days_present[n][0]
        
    # The probability that you will miss your graduation ceremony.  
	x2 = days_present[n - 1][1]  

	return f"{x2}/{x1}"

N = int(input("N days that needs to be checked for:"))    
x= Graduation_Probability(N)
print(x)
