class MortgageCalculator:
	def calculateMaxLoan(self, data):
		required_keys = { "mortgageRate", "grossMonthlyIncome", "loanLength", "monthlyDebt", "maxDti"}

		if not required_keys.issubset(data.keys()):
			raise ValueError("Missing required keys in the data dictionary")

		mortgageRate = data["mortgageRate"]
		grossMonthlyIncome = data["grossMonthlyIncome"]
		loanLength = data["loanLength"]
		monthlyDebt = data["monthlyDebt"]
		maxDti = data["maxDti"]

		monthlyInterestRate = mortgageRate / 12 / 100
		loanTermMonths = loanLength * 12

		maxMonthlyPayment = grossMonthlyIncome * maxDti - monthlyDebt

		maxLoanAmount = (maxMonthlyPayment * ((1 + monthlyInterestRate) ** loanTermMonths - 1)) / (monthlyInterestRate * (1 + monthlyInterestRate) ** loanTermMonths)
		
		return maxLoanAmount

	def calculateMonthlyPayment(self, data):
		required_keys = {'mortgageRate', 'loanAmount', 'loanLength'}

		if not required_keys.issubset(data.keys()):
			raise ValueError("Missing required keys in the data dictionary")

		mortgageRate = data["mortgageRate"]
		loanAmount = data["loanAmount"]
		loanLength = data["loanLength"]

		monthlyInterestRate = mortgageRate / 12 / 100
		loanTermMonths = loanLength * 12
	
		monthlyPayment = loanAmount * (monthlyInterestRate * (1 + monthlyInterestRate) ** loanTermMonths) / ((1 + monthlyInterestRate) ** loanTermMonths - 1)

		return monthlyPayment