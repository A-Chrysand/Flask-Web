from py_functions.account.account_decipher import Decipher


class UrlDecode:
	@staticmethod
	def Decode(strings):
		tempDecipher = Decipher()
		temp = tempDecipher.process_num(strings)
		return temp
