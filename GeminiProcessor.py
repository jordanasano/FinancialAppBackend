class GeminiProcessor:
	@staticmethod
	def convertStringToHtmlString(text):
		textList = text.split("\n")

		for index, value in enumerate(textList):
			while "**" in value:
				value = value.replace("**", "<strong>", 1)
				value = value.replace("**", "</strong>", 1)
			textList[index] = f"<p>{value}</p>"
		
		htmlString = f"<div>{''.join(textList)}</div>"

		return htmlString