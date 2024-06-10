from flask import Flask, request, abort
import google.generativeai as genai
import os
from dotenv import load_dotenv
import requests
import json
from datetime import date
import MortgageCalculator

app = Flask(__name__)

load_dotenv()

# Initialize Gemini
genai.configure(api_key=os.environ["API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

@app.post('/monthlyTakeHomeForCA/<int:annualIncome>')
def getMonthlyTakeHomeForCA(annualIncome):
	taxApi = "https://paycheck-calculator.adp.com/api/pcc/v2/calculations"

	#region 
	data = {
	"calculationTypeCode": {
		"code": "GROSS_TO_NET"
	},
	"statutoryPolicyInputs": [
		{
			"id": "w4Form2020Indicator",
			"name": "w4Form2020Indicator",
			"value": True,
			"type": "boolean",
			"templateID": "e01a6863-4fc7-4c2a-ac8c-f8d896c6fba2"
		},
		{
			"id": "nonResidentAlienIndicator",
			"name": "nonResidentAlienIndicator",
			"value": False,
			"type": "boolean",
			"templateID": "e01a6863-4fc7-4c2a-ac8c-f8d896c6fba2"
		},
		{
			"id": "filingStatus",
			"name": "filingStatus",
			"value": "SINGLE",
			"type": "string",
			"templateID": "e01a6863-4fc7-4c2a-ac8c-f8d896c6fba2"
		},
		{
			"id": "useHigherRateIndicator",
			"name": "useHigherRateIndicator",
			"value": False,
			"type": "boolean",
			"templateID": "e01a6863-4fc7-4c2a-ac8c-f8d896c6fba2"
		},
		{
			"id": "claimedDependentsAmount",
			"name": "claimedDependentsAmount",
			"value": 0,
			"type": "amount",
			"templateID": "e01a6863-4fc7-4c2a-ac8c-f8d896c6fba2"
		},
		{
			"id": "otherIncomeAmount",
			"name": "otherIncomeAmount",
			"value": 0,
			"type": "amount",
			"templateID": "e01a6863-4fc7-4c2a-ac8c-f8d896c6fba2"
		},
		{
			"id": "deductionsAmount",
			"name": "deductionsAmount",
			"value": 0,
			"type": "amount",
			"templateID": "e01a6863-4fc7-4c2a-ac8c-f8d896c6fba2"
		},
		{
			"id": "additionalWithholdingAmount",
			"name": "additionalWithholdingAmount",
			"value": 0,
			"type": "amount",
			"templateID": "e01a6863-4fc7-4c2a-ac8c-f8d896c6fba2"
		},
		{
			"id": "federalTax",
			"name": "withholdingStatus",
			"value": "SUBJECT",
			"type": "string",
			"templateID": "e01a6863-4fc7-4c2a-ac8c-f8d896c6fba2"
		},
		{
			"id": "medicare",
			"name": "withholdingStatus",
			"value": "SUBJECT",
			"type": "string",
			"templateID": "8b2a4033-22a2-452b-b2fb-33606c891238"
		},
		{
			"id": "socialSecurity",
			"name": "withholdingStatus",
			"value": "SUBJECT",
			"type": "string",
			"templateID": "c560a4be-f8a7-4fdb-a0e9-61920ec81c92"
		},
		{
			"id": "filingStatus",
			"name": "filingStatus",
			"value": "SINGLE",
			"type": "string",
			"templateID": "591baa3b-5d81-40fa-aac1-609aac5ab758"
		},
		{
			"id": "numberOfAllowances",
			"name": "numberOfAllowances",
			"value": 0,
			"type": "number",
			"templateID": "591baa3b-5d81-40fa-aac1-609aac5ab758"
		},
		{
			"id": "numberOfAdditionalAllowances",
			"name": "numberOfAdditionalAllowances",
			"value": 0,
			"type": "number",
			"templateID": "591baa3b-5d81-40fa-aac1-609aac5ab758"
		},
		{
			"id": "additionalWithholdingAmount",
			"name": "additionalWithholdingAmount",
			"value": 0,
			"type": "amount",
			"templateID": "591baa3b-5d81-40fa-aac1-609aac5ab758"
		},
		{
			"id": "withholdingStatus",
			"name": "withholdingStatus",
			"value": "SUBJECT",
			"type": "string",
			"templateID": "591baa3b-5d81-40fa-aac1-609aac5ab758"
		},
		{
			"id": "withholdingStatus_SDI",
			"name": "withholdingStatus",
			"value": "SUBJECT",
			"type": "string",
			"templateID": "1c569bfa-33bd-4107-8a49-27ccb3397a5e"
		}
	],
	"jurisdictions": {
		"workedInJurisdictions": [
			{
				"jurisdictionID": "dea07e6d-9432-4f65-958b-25f09e18117e",
				"jurisdictionCode": {
					"name": "United States Federal",
					"code": "US"
				},
				"jurisdictionLevelCode": {
					"code": "FEDERAL"
				}
			},
			{
				"jurisdictionID": "aa4c44ae-c32c-4a5a-a59f-fcbcfe564b1c",
				"jurisdictionCode": {
					"name": "California",
					"code": "CA"
				},
				"jurisdictionLevelCode": {
					"code": "STATE"
				}
			}
		],
		"livedInJurisdictions": [
			{
				"jurisdictionID": "dea07e6d-9432-4f65-958b-25f09e18117e",
				"jurisdictionCode": {
					"name": "United States Federal",
					"code": "US"
				},
				"jurisdictionLevelCode": {
					"code": "FEDERAL"
				}
			},
			{
				"jurisdictionID": "aa4c44ae-c32c-4a5a-a59f-fcbcfe564b1c",
				"jurisdictionCode": {
					"name": "California",
					"code": "CA"
				},
				"jurisdictionLevelCode": {
					"code": "STATE"
				}
			}
		]
	},
	"payDate": f"{date.today()}",
	"payFrequencyCode": {
		"code": "MONTHLY"
	},
	"businessPolicies": [
		{
			"id": "salary-1",
			"alias": "salary",
			"label": "SALARY",
			"inputs": [
				{
					"name": "appliedPayPeriodAmount",
					"value": annualIncome,
					"type": "amount"
				}
			]
		}
	],
	"additionalEarnings": {
		"payLines": []
	},
	"deductions": []
	}
	#endregion

	try:
		response = requests.post(taxApi, json = data)
		monthlyTakeHomePay = json.loads(response.text)["net"]["amount"]
		return { "monthlyTakeHomePay": monthlyTakeHomePay }
	except Exception as error:
		return abort(400, description = str(error))

@app.post('/calculateMaxLoan')
def calculateMaxLoan():
	try:
		data = json.loads(request.data)
		mortgageCalculator = MortgageCalculator.MortgageCalculator()
		maxLoan = mortgageCalculator.calculateMaxLoan(data)

		return { "maxLoan": maxLoan }
	except Exception as error:
		return abort(400, description = str(error))

@app.post("/calculateMonthlyPayment")
def calculateMonthlyPayment():
	try:
		data = json.loads(request.data)
		mortgageCalculator = MortgageCalculator.MortgageCalculator()
		monthlyPayment = mortgageCalculator.calculateMonthlyPayment(data)

		return { "monthlyPayment": monthlyPayment }
	except Exception as error:
		return abort(400, description = str(error))
		
@app.get("/affordableCities/<int:maxHomeLoan>/<int:downPayment>/<string:profession>/<string:desiredCity>/<int:allowableMilesFromCity>")
def findAffordableCities(maxHomeLoan, downPayment, profession, desiredCity, allowableMilesFromCity):
	try:
		response = model.generate_content(f"As a {profession} with a budget of ${downPayment + maxHomeLoan}, I'm seeking recommendations for the top 5 cities within {allowableMilesFromCity} miles of {desiredCity}, California. Please include {desiredCity} in the suggestions. Can you provide details on average home prices, property sizes, and home sizes for 2 bedroom, 1 bath single-family homes in these areas?")
		return response.text
	except Exception as error:
		return abort(429, description = "Gemini's request limit has been reached. Try again later.'")