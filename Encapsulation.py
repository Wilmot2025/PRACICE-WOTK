class bank:
  bank_name = "ECO" #public variable
  __bank_name = "ECO" #private variable
  _bank_name = "ECO" #protected variable

  def bank_details(self):# public method
    print("bank details") #public method

  def bank_details(self):# private method
    print("bank details")# public method

  def __bank_details(self):# private method
    print("bank details")# public method

  def _bank_details(self):# protected method
    print("bank details")# public method

obj_bank = bank() # object creation.
print(obj_bank.bank_name) # public variable access
print(obj_bank._bank_name) # protected variable access
print(obj_bank.__bank_name) # private variable access

