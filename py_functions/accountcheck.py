'''
from py_functions.decipher import Decipher
from py_functions.accountdb import AccountDB
class account_check:
	def login_check(self, check_str):
		temp = self.process_num(check_str)  # temp是列表[]
		db_login_check = AccountDB()
		dbreturn = db_login_check.login_search(temp)
		if dbreturn == 0:
			print('>>>' + '\033[0;33m' + 'dbcheck false' + '\033[0m', end="")
			print('\033[0;36m' + '(User NotFound)' + '\033[0m', end="")
			return 'usernotfound'
		elif dbreturn == 1:
			print('>>>' + '\033[0;33m' + 'password incorrect' + '\033[0m', end="")
			return 'passwderr'
		elif dbreturn == 2:
			print('>>>' + '\033[0;33m' + 'dbcheck false' + '\033[0m', end="")
			print('>>>' + '\033[1;31;40m' + 'dbcheck false(too many item)' + '\033[0m', end="")
			return 'toomany'
		elif dbreturn == 10:
			print('>>>' + '\033[0;32m' + 'dbcheck success' + '\033[0m', end="")
			return 'success'

	def register_check(self, check_str_object):
		temp = self.process_num(check_str_object)
		if len(temp[1]) < 6:
			print('\033[0;31m' + 'invailed password length!!!' + '\033[0m')
			return "passwdlengtherr"
		temp_accpsw = [temp[0], temp[2]]
		registercheck = AccountDB()
		dbreturn = registercheck.register_search(temp_accpsw)
		if (dbreturn[0] and dbreturn[1]):
			return registercheck.register_write(temp)
		elif (dbreturn[0] == False):
			print("User Registed")
			return 'userregisted'
		elif (dbreturn[1] == False):
			print("Email Registed")
			return 'mailregisted'

'''