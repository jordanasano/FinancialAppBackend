class GeminiProcessor:
	@staticmethod
	def convertStringToHtmlString(text):
		textList = text.split("\n")

		for index, value in enumerate(textList):
			textList[index] = f"<p>{value}</p>"
		
		htmlString = f"<div>{''.join(textList)}</div>"

		return htmlString