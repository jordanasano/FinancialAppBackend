class MortgageCalculator:
	@staticmethod
	def calculateMaxLoan(data):
		requiredKeys = { "mortgageRate", "grossMonthlyIncome", "loanLength", "monthlyDebt", "maxDti"}

		if not requiredKeys.issubset(data.keys()):
			raise ValueError("Missing required keys in the data dictionary. Required keys are: " + ", ".join(requiredKeys))

		mortgageRate = data["mortgageRate"]
		grossMonthlyIncome = data["grossMonthlyIncome"]
		loanLength = data["loanLength"]
		monthlyDebt = data["monthlyDebt"]
		maxDti = data["maxDti"]

		monthlyInterestRate = mortgageRate / 12 / 100
		loanTermMonths = loanLength * 12

		maxMonthlyPayment = grossMonthlyIncome * maxDti - monthlyDebt

		maxLoanAmount = (maxMonthlyPayment * ((1 + monthlyInterestRate) ** loanTermMonths - 1)) / (monthlyInterestRate * (1 + monthlyInterestRate) ** loanTermMonths)
		
		return round(maxLoanAmount)

	@staticmethod
	def calculateMonthlyPayment(data):
		requiredKeys = {'mortgageRate', 'loanAmount', 'loanLength'}

		if not requiredKeys.issubset(data.keys()):
			raise ValueError("Missing required keys in the data dictionary. Required keys are: " + ", ".join(requiredKeys))

		mortgageRate = data["mortgageRate"]
		loanAmount = data["loanAmount"]
		loanLength = data["loanLength"]

		monthlyInterestRate = mortgageRate / 12 / 100
		loanTermMonths = loanLength * 12
	
		monthlyPayment = loanAmount * (monthlyInterestRate * (1 + monthlyInterestRate) ** loanTermMonths) / ((1 + monthlyInterestRate) ** loanTermMonths - 1)

		return round(monthlyPayment, 2)